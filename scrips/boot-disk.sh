#!/bin/bash

if [ "`id -u`" != 0 ]; then
	echo "The software Must be run as root.  Exiting."
	exit 1
fi

echo -e "#################################
#   \033[31m Auto make\033[0m                  #
#              \033[31mWindows boot disk\033[0m#
#################################

\033[36m-----------by Geekeyes {"text":"json"}-----------\033[0m \n"
echo "Enter the path to your device in /dev"
read -p "Device-Path : " path
read -p "Iso-Path : " iso
echo -e "\n        Test and Install dependence"
apt-get install -y lilo ntfs-3g
echo -e "\n        Format the Device and Write Device to mbr"
umount "$path"
mkfs.vfat "$path"
lilo -M "$path" mbr
echo -e "\n        Write Device to iso"
mkdir /tmp/iso
mkdir /tmp/usb
mount "$path" /tmp/usb
mount -o loop "$iso" /tmp/iso
cp -rf /tmp/iso/* /tmp/usb
echo -e "OK.\nThanks for your use. Press any key to End."
read
