import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

for url in open("章管家 Druid.txt"):
    try:
        url = url.replace("\n", "")
        print(url+"检测中----\n\n")
        jiaoyan = requests.get(url+"/druid/index.html", headers=headers, verify=False, timeout=5)
        if ("版本" in jiaoyan.text) and ("驱动" in jiaoyan.text):
            with open("章管家 Druid未授权访问 vul.txt", "a+") as f:
                f.write(url+"\n")
    except:
        continue