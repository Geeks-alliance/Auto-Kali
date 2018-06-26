if [ "`id -u`" != 0 ]; then
	echo "The software Must be run as root.  Exiting."
	exit 1
fi

apt-get update
apt-get install -f
apt-get install -y ruby-dev libpcap-dev ruby

gem install bettercap

mv /usr/local/bin/bettercap /usr/local/bin/bettercapj

echo "Tanks for your Use. by {'text':'json'} !"

echo "Test start at 1s ago"

sleep 1

bettercapj
