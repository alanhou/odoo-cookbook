#!/bin/bash
################################################################################
# Script for installing Odoo 14 on Ubuntu & Debian
# Author: Alan Hou
# Website: https://alanhou.org
#-------------------------------------------------------------------------------
# sudo chmod +x odoo-install.sh
# ./odoo-install.sh
################################################################################

# IP_ADDR=`ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"​|head -1`
IP_ADDR=`ip addr | grep 'state UP' -A2 | grep inet|grep -v docker|tail -n1 | awk '{print $2}' | cut -f1  -d'/'`

echo -e "\n---- Update Ubuntu ----"
sudo apt-get update

echo -e "\n---- Install main dependencies ----"
sudo apt install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools -y

echo -e "\n---- Install wkhtmltopdf ----"
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb 
sudo dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb
sudo apt-get install -f

echo -e "\n---- Configure PostgreSQL ----"
sudo apt install postgresql -y
sudo -u postgres createuser --superuser $(whoami)
# sudo -u postgres createuser --createdb $(whoami)
# createdb $(whoami)

# echo -e "\n---- Configure git ----"
# git config --global user.name "Your Name"
# git config --global user.email youremail@example.com

echo -e "\n---- Clone the Odoo code base ----"
mkdir ~/odoo-dev 
cd ~/odoo-dev 
git clone -b 14.0 --single-branch --depth 1 https://github.com/odoo/odoo.git

echo -e "\n---- Create & activate virtualenv ----"
sudo apt-get install python3-venv -y
python3 -m venv ~/venv-odoo-14.0 
source ~/venv-odoo-14.0/bin/activate

echo -e "\n---- Install Python dependencies  ----"
cd ~/odoo-dev/odoo/ 
# error: invalid command 'bdist_wheel'
pip3 install wheel
pip3 install -r requirements.txt

echo -e "\n---- Start Odoo instance  ----"
createdb odoo-test 
nohup python3 odoo-bin -d odoo-test -i base --addons-path=addons --db-filter=odoo-test$  >/dev/null 2>&1 &


echo "-----------------------------------------------------------"
echo "Done! Open your browser and visit http://localhost:8069 or http://${IP_ADDR}:8069"
echo "Default login & password: admin"
echo "Stop all Odoo proccesses: ps -ef | grep odoo | awk '{ print $2}' | xargs kill -9"
echo "To restart Odoo with logs enabled:  ~/odoo-14.0/bin/python3 ~/odoo-dev/odoo/odoo-bin -d odoo-test"
echo "-----------------------------------------------------------"