#!/bin/bash

# Configuration
APP_NAME="backend"
REPO_URL="https://github.com/ibrahzuma/emuslimBackend.git" # REPLACE THIS
USER="root"
PROJECT_DIR="/var/www/$APP_NAME"
SOCK_FILE="$PROJECT_DIR/gunicorn.sock"
SERVER_IP="69.164.193.109"

# 1. System Updates & Dependencies
echo "Installing system dependencies..."
apt-get update
# Added python3.12-venv based on user error
apt-get install -y python3-pip python3-venv python3.12-venv nginx git ufw

# 2. Firewall Setup
echo "Configuring firewall..."
ufw allow OpenSSH
ufw allow 'Nginx Full'
# Non-interactive enable
ufw --force enable

# 3. Project Setup
mkdir -p /var/www
if [ -d "$PROJECT_DIR" ]; then
    echo "Project exists, pulling latest..."
    cd $PROJECT_DIR
    git pull
else
    echo "Cloning project from $REPO_URL..."
    # Check if REPO_URL is set
    if [ "$REPO_URL" == "https://github.com/ibrahzuma/emuslimBackend.git" ]; then
        echo "ERROR: REPO_URL is still default. Please edit setup.sh!"
        exit 1
    fi
    git clone $REPO_URL $PROJECT_DIR
    cd $PROJECT_DIR
fi

# 4. Python Environment
echo "Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env file for production
echo "Creating .env file..."
echo "DJANGO_DEBUG=False" > .env
echo "DJANGO_ALLOWED_HOSTS=$SERVER_IP" >> .env
echo "DJANGO_SECRET_KEY=$(openssl rand -base64 50)" >> .env

python manage.py collectstatic --noinput
python manage.py migrate

# 5. Gunicorn Setup (Systemd)
echo "Configuring Gunicorn..."
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

systemctl daemon-reload
systemctl start gunicorn
systemctl enable gunicorn

# 6. Nginx Setup
echo "Configuring Nginx..."
cat > /etc/nginx/sites-available/$APP_NAME <<EOF
server {
    listen 80;
    server_name $SERVER_IP;

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

echo "Setup Complete!"
