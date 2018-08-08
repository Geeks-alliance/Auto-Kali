#!/usr/bin/env python3
# -*- coding=UTF8 -*-

import os
import time
import sys
import importlib
import Settings

from functions import *
from termcolor import *

def main(): 
    os.system('reset')
    print (colored('''   mm            m                  #             ""#      "   
   ##   m   m  mm#mm   mmm          #   m   mmm     #    mmm   
  #  #  #   #    #    #" "#         # m"   "   #    #      #   
  #mm#  #   #    #    #   #   """   #"#    m"""#    #      #   
 #    # "mm"#    "mm  "#m#"         #  "m  "mm"#    "mm  mm#mm ''',"green"))
    print (colored('\n##################################################\n本作品遵循GNU协议条款\n制作者：极客之眼团队_{"text":"json"}\n极客之眼团队群号：659155551\n本工具只适用与kali linux中\n如有错误请联系QQ：1945649519\n可以输入help查看帮助\ngithub仓库:https://github.com/nios34/Auto-Kali\n###########最后祝您使用愉快#######################',"green"))
    XX= input(colored('请写出您要执行的命令:',"yellow"))
    if XX == "help":
        print (colored("          install 安装程序","blue"))
        print (colored("          exit 退出","blue"))
        print (colored("          deb 修改安装源","blue"))
        print (colored("          gpg 修复apt-get时的数字签名错误","blue"))
        print (colored("          download 多线程下载","blue"))
        print (colored("          PATH 一键部署语言环境","blue"))
        print (colored("          iso Make-windows-boot-disk","blue"))
        print (colored("          Settings 设置","blue"))
        XX= input(colored('请写出您要执行的命令:',"yellow"))
    if XX == "exit":
        exit()
    if XX == "deb":
        deb()
    if XX == "install":
        install()
    if XX == "gpg":
        gpg()
    if XX == "download":
        download()
    if XX == "PATH":
        PATH()
    if XX == "Settings":
        Settings.main()

if __name__ == '__main__':
    main()
