#!/usr/bin/env bash
# Sets the enviroment and the nginx alias for web static
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data 
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

echo "Test Test" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -fs /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data 

location="\n\tlocation /hbnb_static {\n\
		alias /data/web_static/current;\n\
\t}"

awk "NR==37{print \"${location}\"}1" /etc/nginx/sites-enabled/default \
	| sudo tee /etc/nginx/sites-enabled/default > /dev/null

sudo service nginx restart
