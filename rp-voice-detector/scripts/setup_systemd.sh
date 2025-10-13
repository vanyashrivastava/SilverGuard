#!/bin/bash

# This script sets up the systemd service for the Raspberry Pi Voice Detector.

SERVICE_FILE="/etc/systemd/system/rp-voice-detector.service"

# Create the systemd service file
cat <<EOL | sudo tee $SERVICE_FILE
[Unit]
Description=Raspberry Pi Voice Detector
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/rp-voice-detector/src/main.py
WorkingDirectory=/path/to/rp-voice-detector
StandardOutput=journal
StandardError=journal
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd to recognize the new service
sudo systemctl daemon-reload

# Enable the service to start on boot
sudo systemctl enable rp-voice-detector.service

# Start the service
sudo systemctl start rp-voice-detector.service

echo "Systemd service for Raspberry Pi Voice Detector has been set up successfully."