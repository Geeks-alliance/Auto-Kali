#!/usr/bin/env python3
# -*- coding=UTF8 -*-

import os
import time
import sys
import importlib
import Settings

from functions import *
from termcolor import *

def m_help():
    print (colored("┌───────────────────────────────────┐","blue"))
    print (colored("│        install 安装程序           │","blue"))
    print (colored("│        deb 修改安装源             │","blue"))
    print (colored("│        bug 错误修复               │","blue"))
    print (colored("│        download 多线程下载        │","blue"))
    print (colored("│        Settings 设置              │","blue"))
    print (colored("│        exit 退出                  │","blue"))
    print (colored("└───────────────────────────────────┘","blue"))
    main()
def b_help():
    print (colored("┌──────────────────────────────────────┐","blue"))
    print (colored("│  gpg 修复apt-get时的数字签名错误     │","blue"))
    print (colored("│  boot 引导修复(必须运行在Xsession上) │","blue"))
    print (colored("└──────────────────────────────────────┘","blue"))
    bug()
def bug():
    XXX = input(colored("请写出您要修复的错误 >>> ",'yellow'))
    if XXX == "gpg":
        gpg()
    elif XXX == "boot":
        boot()
    else:
        bug()
def main(): 
    XX= input(colored('请写出您要执行的命令 >>> ',"yellow"))
    if XX == "help":
        m_help()
    elif XX == "exit":
        exit()
    elif XX == "bug":
        b_help()
        bug()
    elif XX == "deb":
        deb()
    elif XX == "install":
        install()
    elif XX == "download":
        download()
    elif XX == "Settings":
        Settings.main()
    else:
        main()
if __name__ == '__main__':
    os.system('reset')
    print (colored('''   mm            m                  #             ""#      "   
   ##   m   m  mm#mm   mmm          #   m   mmm     #    mmm   
  #  #  #   #    #    #" "#         # m"   "   #    #      #   
  #mm#  #   #    #    #   #   """   #"#    m"""#    #      #   
 #    # "mm"#    "mm  "#m#"         #  "m  "mm"#    "mm  mm#mm ''',"green"))
    print (colored('\n##################################################\n本作品遵循GNU协议条款\n制作者：极客之眼团队_{"text":"json"}\n修改者:极客之眼团队_无忧Parker\n极客之眼团队群号：659155551\n本工具只适用与kali linux中\n如有错误请联系QQ：1945649519\n可以输入help查看帮助\ngithub仓库:https://github.com/nios34/Auto-Kali\n###########最后祝您使用愉快#######################',"green"))
    print (colored('Ps.本工具支持序号和中文还有拼音命令',"red"))
    main()
