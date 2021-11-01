import os
from dotenv import load_dotenv
import pihole_api as pi

if __name__ == "__main__":

    load_dotenv()
    pihole = pi.Pihole(os.environ["PI_URL"], os.environ["PI_PSW"])

    # print(pihole.dns())
    # print(pihole.dns("get"))
    # print(pihole.dns("add", ip_address="1.1.1.1"))
    # print(pihole.dns("add", ip_address="1.1.1.1", domain="pippo.com"))
    # print(pihole.dns("get"))
    # print(pihole.dns("delete", ip_address="1.1.1.1", domain="pippo.com"))
    # print(pihole.dns("get"))

    # print(pihole.cname("get"))
    # print(pihole.cname("add","bbb.com","dns.xelk.me"))
    # print(pihole.cname("delete","bbb.com","dns.xelk.me"))
    # print(pihole.cname("get"))

    # print(pihole.disable())
    # print(pihole.disable(30))
    # print(pihole.enable())

    print("\n\n----WHITE--------")
    print(pihole.get_domains("white"))
    print(pihole.add_domain("white","pippo.it","add pippo"))
    # print(pihole.get_domains("white"))
    print(pihole.replace_domain("white","pippo.it","replace pippo"))
    print(pihole.get_domains("white"))
    print(pihole.delete_domain("white","pippo.it","delete pippo"))
    print(pihole.get_domains("white"))

    print("\n\n----BLACK--------")
    print(pihole.get_domains("black"))
    print(pihole.add_domain("black","pippo.black","add pippo"))
    print(pihole.replace_domain("black","pippo.black","replace pippo"))
    print(pihole.get_domains("black"))
    print(pihole.delete_domain("black","pippo.black","delete pippo"))
    print(pihole.get_domains("black"))