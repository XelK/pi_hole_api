"""
Pihole python API client.
Module for black/white list management
"""

LIST_TYPES = ("white", "black")
ERR_MSG = "Not correct type, use: " + str(LIST_TYPES)


def get_domains(pihole, showtype) -> dict:
    """
    Return list of domains from white/black list
    """
    if showtype not in LIST_TYPES:
        return ERR_MSG
    _list_url = pihole.url + "scripts/pi-hole/php/groups.php"
    _params = {"action": "get_domains", "showtype": showtype, "token": pihole.token}
    return pihole.session.post(_list_url, _params).json()


def add_domain(pihole, showtype, domain, comment) -> dict:
    """
    Add domain to white/black list
    """
    if showtype not in LIST_TYPES:
        return ERR_MSG
    _list_url = pihole.url + "scripts/pi-hole/php/groups.php"
    _params = {
        "action": "add_domain",
        "type": LIST_TYPES.index(showtype),
        "domain": domain,
        "comment": comment,
        "token": pihole.token,
    }
    return pihole.session.post(_list_url, _params).json()


def replace_domain(pihole, showtype, domain, comment) -> dict:
    """
    Replace domains in white/black list
    """
    if showtype not in LIST_TYPES:
        return ERR_MSG
    _list_url = pihole.url + "scripts/pi-hole/php/groups.php"
    _params = {
        "action": "replace_domain",
        "type": LIST_TYPES.index(showtype),
        "domain": domain,
        "comment": comment,
        "token": pihole.token,
    }
    return pihole.session.post(_list_url, _params).json()


def delete_domain(pihole, showtype, domain, comment) -> dict:
    """
    Delete domain from white/black list
    """
    if showtype not in LIST_TYPES:
        return ERR_MSG
    _list_url = pihole.url + "scripts/pi-hole/php/groups.php"
    _params = {
        "action": "delete_domain",
        "type": LIST_TYPES.index(showtype),
        "domain": domain,
        "comment": comment,
        "token": pihole.token,
    }
    return pihole.session.post(_list_url, _params).json()
