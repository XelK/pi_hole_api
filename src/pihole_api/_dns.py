"""
Pihole python API client.
Module for dns calls
"""


def dns(pihole, action: None, ip_address=None, domain=None) -> dict:
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
    _dns_url = pihole.url + "scripts/pi-hole/php/customdns.php"
    _params = {"action": action, "token": pihole.token}
    _actions = ("get", "add", "delete")
    if action not in _actions:
        return {"success": False, "message": "Action not permitted! Use " + str(_actions)}
    if action in _actions[0]:
        _response = pihole.session.post(_dns_url, _params).json()
    if action in _actions[1:]:
        if ip_address is None or domain is None:
            _response = {"success": False, "message": "Provide Ip and Domain"}
        else:
            _params.update({"ip": ip_address, "domain": domain})
            _response = pihole.session.post(_dns_url, _params).json()
    return _response


def cname(pihole, action: None, domain=None, target=None) -> dict:
    """
    Execute cname calls. Return dictionary
        - get:
            - permit list cnam entries
            - return: list of custom-cname configured
        - add:
            - permit add cname entry
            - require: ip address and domain
            - return: status of operation
        - del:
            - permit remove cname entry
            - require: ip address and domain
            - return: status of operation
    """
    _cname_url = pihole.url + "scripts/pi-hole/php/customcname.php"
    _params = {"action": action, "token": pihole.token}
    _actions = ("get", "add", "delete")
    if action not in _actions:
        return {"success": False, "message": "Action not permitted! Use " + str(_actions)}
    if action in _actions[0]:
        _response = pihole.session.post(_cname_url, _params).json()
    if action in _actions[1:]:
        if domain is None or target is None:
            _response = {"success": False, "message": "Provide Source/Target"}
        else:
            _params.update({"domain": domain, "target": target})
            _response = pihole.session.post(_cname_url, _params).json()
    return _response
