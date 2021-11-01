"""
Pihole python API client.
Module for enable/disable protection
"""


def disable(pihole, time=None) -> dict:
    """
    Permit disable protection
    """
    _disable_url = pihole.url + "api.php"
    _params = {"disable": 0, "token": pihole.token}
    if time:
        _params.update({"disable": time})
        return pihole.session.get(_disable_url, params=_params).json()
    return pihole.session.get(_disable_url, params=_params).json()


def enable(pihole) -> dict:
    """
    Enable protection
    """
    _enable_url = pihole.url + "api.php"
    _params = {"enable": 0, "token": pihole.token}
    return pihole.session.get(_enable_url, params=_params).json()
