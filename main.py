import time
from datetime import datetime

start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9)
finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 16)

# on Linux hosts file look like " hosts = 'etc\hosts' " 
hosts = r"C:\Windows\System32\drivers\etc\hosts"
redirect_url = "127.0.0.1"
blocked_sites = ["www.youtube.com", "youtube.com"]

while True:
    if start_time < datetime.now() < finish_time:
        print("Доступ ограничен")
        with open(hosts, "r+") as file:
            src = file.read()
            
            for website in blocked_sites:
                if website in src:
                    pass
                else:
                    file.write(f"{redirect_url} {website}\n")
    else:
        print("Доступ открыт")
        with open(hosts, "r+") as file:
            src = file.readlines()
            file.seek(0)
            
            for line in src:
                if not any(website in line for website in blocked_sites):
                    file.write(line)
            file.truncate()
            
    time.sleep(5)