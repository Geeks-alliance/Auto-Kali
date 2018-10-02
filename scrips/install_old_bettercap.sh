if [ "`id -u`" != 0 ]; then
	echo "The software Must be run as root.  Exiting."
	exit 1
fi

apt-get update
apt-get install -f
apt-get install -y ruby-dev libpcap-dev ruby

gem install bettercap

mv /usr/local/bin/bettercap /usr/local/bin/bettercap1.6

echo "Tanks for your Use. by {'text':'json'} !"
echo "Start"
echo "Test start at 3s ago"

sleep 3

bettercap1.6
