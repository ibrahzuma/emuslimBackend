#!/bin/bash

# Configuration
APP_NAME="backend"
REPO_URL="YOUR_GITHUB_REPO_URL" # REPLACE THIS
USER="root" # Or your sudo user
PROJECT_DIR="/var/www/$APP_NAME"
SOCK_FILE="$PROJECT_DIR/gunicorn.sock"

# 1. System Updates & Dependencies
apt-get update
apt-get install -y python3-pip python3-venv nginx git ufw

# 2. Firewall Setup
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw --force enable

# 3. Project Setup
mkdir -p /var/www
if [ -d "$PROJECT_DIR" ]; then
    echo "Project exists, pulling latest..."
    cd $PROJECT_DIR
    git pull
else
    echo "Cloning project..."
    git clone $REPO_URL $PROJECT_DIR
    cd $PROJECT_DIR
fi

# 4. Python Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# 5. Gunicorn Setup (Systemd)
cat > /etc/systemd/system/gunicorn.service <<EOF
[Unit]
Description=gunicorn daemon for $APP_NAME
After=network.target

[Service]
User=$USER
Group=www-data
WorkingDirectory=$PROJECT_DIR
ExecStart=$PROJECT_DIR/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:$SOCK_FILE $APP_NAME.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

systemctl start gunicorn
systemctl enable gunicorn

# 6. Nginx Setup
cat > /etc/nginx/sites-available/$APP_NAME <<EOF
server {
    listen 80;
    server_name YOUR_DOMAIN_OR_IP; # REPLACE THIS

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root $PROJECT_DIR;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:$SOCK_FILE;
    }
}
EOF

ln -sf /etc/nginx/sites-available/$APP_NAME /etc/nginx/sites-enabled
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl restart nginx

echo "Setup Complete! Don't forget to:"
echo "1. Update ALLOWED_HOSTS in settings.py"
echo "2. Set DEBUG = False"
echo "3. Update REPO_URL and YOUR_DOMAIN_OR_IP in this script"
