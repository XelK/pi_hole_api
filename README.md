# pihole_api
[![Pylint](https://github.com/XelK/pihole_api/actions/workflows/pylint.yml/badge.svg)](https://github.com/XelK/pihole_api/actions/workflows/pylint.yml)

[![Build test](https://github.com/XelK/pi_hole_api/actions/workflows/Build-test.yml/badge.svg)](https://github.com/XelK/pi_hole_api/actions/workflows/Build-test.yml)


Python api module for pi-hole server (https://pi-hole.net/).
Permit to perform api calls from python code.

## Examples
### Create class
```python
import pihole_api as pi
pihole = pi.Pihole("PI_URL", "PI_PSW")
```
where:
- PI_URL: url of pi-hole page
- PI_PSW: password of pi-hole

or using environment variables "PI_URL" and "PI_PSW" set to pi-hole url and pi-hole password respectively:
```python
import os
from dotenv import load_dotenv
import pihole_api as pi
pihole = pi.Pihole(os.environ["PI_URL"], os.environ["PI_PSW"])
```
### Core module
Permit:
- enable/disable protection
```python
pihole.enable()
pihole.disable()
pihole.disable(30) # disable per 30 seconds
``` 
### Dns module
Permit:
- list dns records
- add/remove A record
- add/remove CNAME record
```python
pihole.dns("get") # print dns list
pihole.cname("get") # print cname list
# add domain to dns
pihole.dns("add", ip_address="1.1.1.1",domain="pippo.com"))
# remove domain to dns
pihole.dns("delete", ip_address="1.1.1.1",domain="pippo.com"))
# add cname from pippo.com to pluto.com
pihole.cname("add","pippo.com","pluto.com"))
# remove cname
pihole.cname("delete","pippo.com","pluto.com"))
``` 

## List module
Permit:
-  list/add/change/remove domains to white lists
-  list/add/change/remove domains to black lists
```python
# get white list
pihole.get_domains("white")
# add to white list
pihole.add_domain("white","pippo.it","add pippo")
# replace in white list
pihole.replace_domain("white","pippo.it","replace pippo")
# delete from white list
pihole.delete_domain("white","pippo.it","delete pippo")

# get black list
pihole.get_domains("black")
# add to black list
pihole.add_domain("black","pippo.it","add pippo")
# add change in black list
pihole.replace_domain("black","pippo.it","replace pippo")
# delete from black list
pihole.delete_domain("black","pippo.it","delete pippo")
```
