if [ "`id -u`" != 0 ]; then
	echo "The software Must be run as root.  Exiting."
	exit 1
fi
echo -e "\033[31m 检查依赖中......... \033[0m"
apt-get install -y python3-pip
pip3 install termcolor
echo -e "\033[31m 成功!3秒后打开程序...... \033[0m" 
sleep 3
python3 master.py
