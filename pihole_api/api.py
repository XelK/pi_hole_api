"""
Pihole python API client.
Permit send commands to pihole server via http calls
Require set env variables:
@PI_URL: url of pihole server
@PI_PSW: password of pihole server
"""
import os
import re
import requests
from dotenv import load_dotenv


class Pihole:
    """
    Pihole class.
    Require:
        - url: pihole server url
        - psw: pihole password
    """

    def __init__(self, url, psw):
        self.url = url
        self.psw = psw
        self.session = requests.Session()
        self.token = self._login()

    def _login(self):
        """
        Create session token
        """
        log_url = self.url + "index.php?login"
        response = self.session.post(log_url, data={"pw": self.psw})
        regex = r'(<div id="token" hidden>)(\S+)(<\/div>)'
        if response.ok:
            return re.findall(regex, response.text, re.MULTILINE)[0][1]
        return None


def dns(pihole: Pihole, action: str, ip_address=None, domain=None) -> dict:
    """
    Execute dns calls. Return dictionary
        - get:
            - permit list dns entries
            - return: list of custom-dns configured
        - add:
            - permit add dns entry
            - require: ip address and domain
            - return: status of operation
        - del:
            - permit remove dns entry
            - require: ip address and domain
            - return: status of operation
    """
    dns_url = pihole.url + "scripts/pi-hole/php/customdns.php"
    params = {"action": action, "token": pihole.token}
    if action == "get":
        response = pihole.session.post(dns_url, params).json()
    if action in ("add", "delete"):
        if ip_address is None or domain is None:
            return False
        params.update({"ip": ip_address, "domain": domain})
        response = pihole.session.post(dns_url, params).json()
        # print(l["success"], l["message"])
    return response


if __name__ == "__main__":

    load_dotenv()
    pihole = Pihole(os.environ["PI_URL"], os.environ["PI_PSW"])

    dns(pihole, "get")
    dns(pihole, "get")
    print(dns(pihole, "add", ip_address="1.1.1.1"))
    print(dns(pihole, "add", ip_address="1.1.1.1", domain="pippo.com"))
    print(dns(pihole, "delete", ip_address="1.1.1.1", domain="pippo.com"))
