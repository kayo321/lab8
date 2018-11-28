#!/bin/bash

sudo yum install python-pip
sudo pip install --upgrade pip
sudo pip install flask
sudo curl --fail -sSLo /etc/yum.repos.d/passenger.repo https://oss-binaries.phusionpassenger.com/yum/definitions/el-passenger.repo
sudo yum install -y mod_passenger || sudo yum-config-manager --enable cr && sudo yum install -y mod_passenger
sudo service httpd restart
sudo mkdir /var/www/lab8
**clone contents** cp -a * /var/www/lab8
sudo nano /etc/httpd/conf.d/myapp.conf
<VirtualHost *:80>
    DocumentRoot /var/www/lab8/
    PassengerAppRoot /var/www/lab8/
    PassengerAppType wsgi
    PassengerStartupFile passenger_wsgi.py
    
    <Directory /var/www/myapp>
      Allow from all
      Options -MultiViews
      Require all granted
    </Directory>
</VirtualHost>
sudo service httpd restart







