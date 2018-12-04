#!/usr/bin/env python3
# -*- coding=UTF8 -*-

import os
import time
import sys
import importlib
import Settings

from functions import *
from termcolor import *

zwf=0

def help():
    print (colored("┌───────────────────────────────────┐","blue"))
    print (colored("│        install 安装程序           │","blue"))
    print (colored("│        deb 修改安装源             │","blue"))
    print (colored("│        bug 错误修复               │","blue"))
    print (colored("│        download 多线程下载        │","blue"))
    print (colored("│        settings 设置              │","blue"))
    print (colored("│        exit 退出                  │","blue"))
    print (colored("└───────────────────────────────────┘","blue"))
    pass

def bug():
    while(zwf==zwf):
        XXX = input(colored("请写出您要修复的错误 >>> ",'yellow'))
        if XXX == "gpg":
            bug_Manager.gpg(zwf)
        elif XXX == "boot":
            bug_Manager.boot(zwf)
        elif XXX == "help":
            bug_Manager.help(zwf)
        elif XXX == "gnome":
            bug_Manager.gnome_show_icon_on_desktp(zwf)
        elif XXX == "exit":
            exit()
            pass
        pass
    pass

def main(): 
    while(zwf==zwf):
        XX= input(colored('请写出您要执行的命令 >>> ',"yellow"))
        if XX == "exit":
            exit()
        elif XX == "help":
            help()
        elif XX == "bug":
            bug()
        elif XX == "deb":
            deb()
        elif XX == "install":
            install()
        elif XX == "download":
            download()
        elif XX == "settings":
            Settings.main()
            pass
        pass
    pass

if __name__ == '__main__':
    os.system('reset')
    print (colored('''   mm            m                  #             ""#      "   
   ##   m   m  mm#mm   mmm          #   m   mmm     #    mmm   
  #  #  #   #    #    #" "#         # m"   "   #    #      #   
  #mm#  #   #    #    #   #   """   #"#    m"""#    #      #   
 #    # "mm"#    "mm  "#m#"         #  "m  "mm"#    "mm  mm#mm ''',"green"))
    print (colored('\n##################################################\n本作品遵循GNU协议条款\n制作者：极客之眼团队_{"text":"json"}_无忧Parker\n极客之眼团队群号：659155551\n本工具只适用与kali linux中\n如有错误请联系QQ：1945649519\n可以输入help查看帮助\ngithub仓库:https://github.com/Geeks-alliance/Auto-Kali\n###########最后祝您使用愉快#######################',"green"))
    main()
