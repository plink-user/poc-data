import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

for url in open("蓝海卓越计费管理系统.txt"):
    try:
        url = url.replace("\n", "")
        print(url+"检测中----\n\n")
        jiaoyan = requests.get(url+"/debug.php", headers=headers, verify=False, timeout=5)
        if (("Execute Shell command" in jiaoyan.text) and (jiaoyan.status_code == 200)):
            with open("蓝海卓越计费管理系统 debug.php 远程命令执行 vul.txt", "a+") as f:
                f.write(url+"\n")
    except:
        continue

