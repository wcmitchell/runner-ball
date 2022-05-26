#!/bin/bash

# Copy and enable the systemd unit file/service
sudo cp /home/pi/runner-ball/scripts/runner-ball.service /etc/systemd/system/
sudo systemctl enable runner-ball.service

# Install pipenv
pip install pipenv
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Update the .env file
sed -i 's/PREFERENCES_FILE_PATH=.*/PREFERENCES_FILE_PATH=\/home\/pi\/runner-ball\/data\/preferences.yml/' /home/pi/runner-ball/.env

# Start service
sudo systemctl start runner-ball.service
