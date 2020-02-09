#This program will block facebook 4 AM to 10 AM IST

import time
from datetime import datetime as dt
host = "127.0.0.1"
websites = ["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,4) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,10):
        print("Working hour")
        with open("/etc/hosts","r+") as file:
            content = file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(host + " " + site+"\n")
    else:
        print("Non working hour")
        with open("/etc/hosts","r+") as file:
            content = file.readlines()
            file.seek(0)
            file.truncate()
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            file.truncate()    
    time.sleep(5)
