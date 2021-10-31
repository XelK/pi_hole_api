import os
from dotenv import load_dotenv
import pihole_api as pi

if __name__ == "__main__":

    load_dotenv()
    pihole = pi.Pihole(os.environ["PI_URL"], os.environ["PI_PSW"])

    print(pihole.dns())
    print(pihole.dns("get"))
    # print(pihole.dns("add", ip_address="1.1.1.1"))
    # print(pihole.dns("add", ip_address="1.1.1.1", domain="pippo.com"))
    # print(pihole.dns("get"))
    # print(pihole.dns("delete", ip_address="1.1.1.1", domain="pippo.com"))
    # print(pihole.dns("get"))

    print(pihole.cname("get"))
    print(pihole.cname("add","bbb.com","dns.xelk.me"))
    print(pihole.cname("delete","bbb.com","dns.xelk.me"))
    print(pihole.cname("get"))

