#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import socket
import re
import time
import os
import os.path
import  fileinput
from re import fullmatch
from pathlib import Path
from rich.console import Console
from rich.table import Table


#Path
path = os.getcwd()
core = (path+'/core')
config = (path+'/config')
logs = (path + '/logs')
#Configuration file
shodan_config = config + "/shodanapi.ini"
fofa_config = config + "/fofaapi.ini"
#Cycle call flag
flag = True

######
target = "NULL"
waf = "NULL"
cdn = "NULL"
cmslog = "NULL"
ipaddress = "NULL"
#Init
try:
    while flag:
        value = input("pef>")
        #print(value)  #debug

######## use
        try:
            value.split(" ")[1]
        except IndexError:
            pass
        else:
            if value.split(" ")[0] == "use":
                module_name = value.split(" ")[1]

                payload = path + module_name
                print(payload)
            else:
                pass
########
#####Print  INFO
        try:
            module_name
        except:
            pass
        else:
            console = Console()
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("MODULE IN USE")
            table.add_row(module_name)
            console.print(table)

        try:
            target_cookie
        except:
            pass
        else:
            console = Console()
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("COOKIE")
            table.add_row(target_cookie)
            console.print(table)


######## set target
        try:
            value.split(" ")[2]
        except IndexError:
            pass
        else:
            if value.split(" ")[0] == "set" and value.split(" ")[1] == "target":
                target = value.split(" ")[2]
                print("TARGET =>",target)
                with open(logs + '/target.log','w') as f:
                    f.write(target)
                try:
                    ipaddress = socket.gethostbyname(target)
                except:
                    print("\033[31m[ERROR]\033[0m","Failed to obtain IP address automatically.")
            else:
                pass
######### set Cookie
        try:
            value.split(" ")[2]
        except IndexError:
            pass
        else:
            if value.split(" ")[0] == "set" and value.split(" ")[1] == "cookie":
                target_cookie = value.split(" ")[2]
                print("COOKIE =>",target_cookie)
                with open(logs + '/cookie.log','w') as f:
                    f.write(target_cookie)

############## Show module info
        try:
            payload
        except:
            pass
        else:
            if value.split(" ")[0] == "show":
                from vul.poc.ruoyi from cnvd-2021-01931



#########

        if value == "shodan":
            #Check if Shodan configuration file exists
            status = os.path.exists(shodan_config)
            if status == False:
                print("\033[31m[ERROR]\033[0m","Shodan API is not set.")
            else:
                print("\033[32m[INFO]\033[0m","Congratulations! Now you can use Shodan.")
        if value == "shodan init":
            print("\033[32m[INFO]\033[0m","Please enter Shodan API information to complete the configuration.")
            shodanapi = input("API>")
            with open(config + '/shodanapi.ini','w') as f:
                f.write(shodanapi)
        if value == "fofa":
            status = os.path.exists(fofa_config)
            if status == False:
                print("\033[31m[ERROR]\033[0m","FOFA API is not set.")
            else:
                print("\033[32m[INFO]\033[0m","Congratulations! Now you can use FOFA.")

        if value == "help":
            print("++++++++++Help Documentation++++++++++")
            print("shodan              Check Shodan status")
            print("shodan init         Shodan initial configuration")
            print("shodan search       Query via Shodan")
            print("use [module]        Check shodan status")
            print("search              Query [module]/[payload]/[exploit] path")
            print("nmap                Use nmap scanner")
            print("rustscan            Use rustscan scanner")
            print("update              Update framework")
            print("cms                 Query target CMS information")
            print("cdn                 Query target CDN information")
            print("waf                 Query target WAF information")
            print("dirscan             Path scan")
            print("set LHOST(lhost)    Set the local listening IP address")
            print("set RHOST(rhost)    Set the target IP address")
            print("set LPORT(lport)    Set the local listening port")
            print("set LHOST(lhost)    Set the target port")
            print("set target          Set the target")
            print("set cookie          Set target cookie")
            print("status              View configuration status")
            print("exploit(run)        Run the exploit(poc) code.")
            print("anonnet             Use Tor anonymous network")
            print("socks5              Set up socks5 proxy")
            print("fofa                Check FOFA status")
            print("fofa init           FOFA initial configuration")
            print("fofa search         Query via FOFA")
            print("show                View the required information of the module")
            print("++++++++++Help Documentation++++++++++")

        if value == "exit":
            exit()
        if value == "clear":
            os.system("clear")
        if value == "cms":
            try:
                from core import cms
                cms.cmslog = cmslog
            except:
                print("\033[31m[ERROR]\033[0m","CMS recognition failed.")
        if value == "waf":
            try:
                tmp_waf = os.popen("wafw00f %s -o %s/waf.log" %(target,logs)).read()
                waf = os.popen("awk '{print $2}' %s/waf.log " %(logs)).read()
            except:
                print("\033[31m[ERROR]\033[0m","WAF recognition failed.")
            try:
                waf
            except:
                print("\033[31m[ERROR]\033[0m","CDN recognition failed.")
            else:
                cdn = waf  #CDN

        if value == "status":
            try:
                console = Console()
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("TARGET")
                table.add_column("CMS")
                table.add_column("WAF")
                table.add_column("CDN")
                table.add_column("REMOTE IP")
                table.add_column("LOCAL IP")
                table.add_column("LOCAL PORT")
                table.add_column("REMOTE PORT")
                table.add_column("GEOIP")
                table.add_column("TARGET PORT")



                table.add_row(target,cmslog,waf,cdn,ipaddress)
                console.print(table)
            except:
                print("\033[31m[ERROR]\033[0m","No data.")

        if value == "TARGET PORT":
            console = Console()
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("TARGET PORT")
            #table.add_row()
            console.print(table)






except KeyboardInterrupt:
    print("\n")
    print("\033[32m[INFO]\033[0m","The user manually exited the program.")
