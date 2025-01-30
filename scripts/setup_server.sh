#!/bin/bash

# Initialize database
sudo -u postgres psql -c "CREATE DATABASE terminusa;"
sudo -u postgres psql -c "CREATE USER terminusa WITH PASSWORD 'strongpass';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE terminusa TO terminusa;"

# Setup firewall
ufw allow 22
ufw allow 80
ufw allow 443
ufw enable

# Install dependencies
apt install -y python3-pip python3-venv nginx certbot
python3 -m venv /opt/terminusa-venv
/opt/terminusa-venv/bin/pip install -r requirements.txt