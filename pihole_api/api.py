import os
import requests
import re
from dotenv import load_dotenv

def login(s,url,psw):
    url+="index.php?login"
    p={'pw': psw}
    r=s.post(url,data=p)
    if r.ok:
        token=re.findall("(<div id=\"token\" hidden>)(\S+)(<\/div>)",r.text,re.MULTILINE)[0][1]
    return token


def dns(s,url,token,op,ip=None,domain=None):
    url+="scripts/pi-hole/php/customdns.php"
    if op == "get":
        p={'action': op,"token":token}
        l=s.post(url,p).json()
        print(l['data'])
    if op == "add" or op=="delete":
        p={"action":op, "token":token, "ip":ip, "domain":domain}
        l=s.post(url,p).json()
        print(l['success'],l["message"])
    return l



if __name__ == '__main__':

    load_dotenv()
    psw=os.environ['PI_PSW']
    url=os.environ['PI_URL']
    
    s = requests.Session()

    if not s.get(url).ok:
        print("Wrong url!")    
        
    token=login(s,url,psw)
    dns(s,url,token,"get")
    dns(s,url,token,"add",ip="1.1.1.1",domain="pippo.com")
    dns(s,url,token,"delete",ip="1.1.1.1",domain="pippo.com")



