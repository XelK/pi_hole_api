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

import dns


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

    def dns(self, action=None, ip_address=None, domain=None) -> dict:
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
        return dns.dns(self, action, ip_address, domain)


if __name__ == "__main__":

    load_dotenv()
    pihole = Pihole(os.environ["PI_URL"], os.environ["PI_PSW"])

    print(pihole.dns())
    print(pihole.dns("get"))
    print(pihole.dns("add", ip_address="1.1.1.1"))
    print(pihole.dns("add", ip_address="1.1.1.1", domain="pippo.com"))
    print(pihole.dns("get"))
    print(pihole.dns("delete", ip_address="1.1.1.1", domain="pippo.com"))
    print(pihole.dns("get"))
