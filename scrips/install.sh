#!/usr/bin/env bash

if [ "`id -u`" != 0 ]; then
	whiptail --title "Install ERROR" --msgbox "The script Must be run as root.  Exiting." 7 60
	exit
fi

if (whiptail --title "AUTO-KALI STSRT"  --yesno '   mm            m                  #             ""#      "   \n   ##   m   m  mm#mm   mmm          #   m   mmm     #    mmm   \n  #  #  #   #    #    #" "#         # m"   "   #    #      #   \n  #mm#  #   #    #    #   #   """   #"#    m"""#    #      #   \n #    # "mm"#    "mm  "#m#"         #  "m  "mm"#    "mm  mm#mm\n\n                       是否安装Auto-kali?' 15 68) then
	exec wget -P /bin https://raw.githubusercontent.com/nios34/Auto-Kali/master/scrips/auto-kali
    apt install wget git python3 python3-termcolor -y
    git clone https://github.com/nios34/Auto-kali /usr/share/auto-kali
    chmod 777 /bin/auto-kali
    whiptail --title "Install finish" --msgbox "安装完成!    启动指令:auto-kali" 7 60
else
    exit
fi
