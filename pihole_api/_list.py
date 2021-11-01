types=("white","black")
err="Not correct type, use: "+str(types)

def get_domains(pihole, type)->dict:
    if type not in types:
        return err
    _list_url = pihole.url + "scripts/pi-hole/php/groups.php"
    _params = {"action":"get_domains","showtype": type, "token": pihole.token}
    return pihole.session.post(_list_url,_params).json()

def add_domain(pihole, type, domain, comment)->dict:
    if type not in types:
        return err
    _list_url = pihole.url + "scripts/pi-hole/php/groups.php"
    _params = {"action":"add_domain","type": types.index(type), "domain":domain,"comment":comment,"token": pihole.token}
    return pihole.session.post(_list_url,_params).json()

def replace_domain(pihole, type, domain, comment)->dict:
    if type not in types:
        return err
    _list_url = pihole.url + "scripts/pi-hole/php/groups.php"
    _params = {"action":"replace_domain","type": types.index(type), "domain":domain,"comment":comment,"token": pihole.token}
    return pihole.session.post(_list_url,_params).json()

def delete_domain(pihole, type, domain, comment)->dict:
    if type not in types:
        return err
    _list_url = pihole.url + "scripts/pi-hole/php/groups.php"
    _params = {"action":"delete_domain","type": types.index(type), "domain":domain,"comment":comment,"token": pihole.token}
    return pihole.session.post(_list_url,_params).json()
