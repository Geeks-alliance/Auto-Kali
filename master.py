# -*- coding: UTF-8 -*-  
#!/usr/bin/python3

import os
import time
import functions
import sys
import importlib
try:
    from termcolor import *
except ModuleNotFoundError:
    print ("\033[1;32;43m发现依赖问题，正在尝试自动修复\033[0m!")
    os.system("pip3 install termcolor")
    print ("\033[1;32;43m自动修复完成，3秒后重启(如还有错误请在终端输入'pip3 install termcolor')\033[0m!")
    time.sleep(3)
    os.system('python3 start-Tools.py')
os.system('reset')
print (colored('''   mm            m                  #             ""#      "   
   ##   m   m  mm#mm   mmm          #   m   mmm     #    mmm   
  #  #  #   #    #    #" "#         # m"   "   #    #      #   
  #mm#  #   #    #    #   #   """   #"#    m"""#    #      #   
 #    # "mm"#    "mm  "#m#"         #  "m  "mm"#    "mm  mm#mm ''',"green"))
print (colored('\n##################################################\n本作品遵循GNU协议条款\n制作者：极客之眼团队_{"text":"json"}\n极客之眼团队群号：659155551\n本工具只适用与kali linux中\n如有错误请联系QQ：1945649519\n可以输入help查看帮助\ngithub仓库:https://github.com/nios34/Auto-Kali\n###########最后祝您使用愉快#######################',"green"))
XX= input(colored('请写出您要执行的命令:',"yellow"))
if XX == "help":
    print ("          install 安装程序")
    print ("          exit 退出")
    print ("          deb 修改安装源")
    print ("          gpg 修复apt-get时的数字签名错误")
    print ("          download 多线程下载")
    print ("          PATH 一键部署语言环境")
    print ("          iso Make-windows-boot-disk")
    XX= input(colored('请写出您要执行的命令:',"yellow"))
if XX == "exit":
    exit()
if XX == "deb":
    functions.deb()
if XX == "install":
    functions.install()
if XX == "gpg":
    functions.gpg()
if XX == "download":
    functions.download()
if XX == "PATH":
    functions.PATH()
if XX == "iso":
    os.system("bash ./scrips/boot-disk.sh")
    os.system("python3 master.py")
	
