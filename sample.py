import os
import requests

URL=""
try:
    r=requests.get(URL,timeout=5)
    if r.status_code==200:
        print("website is running")
    else:
        print("website is not running")
        os.system("sudo systemctl restart nginx")
except:
    print("Website is down. Restarting server...")
    os.system("sudo systemctl restart nginx")
