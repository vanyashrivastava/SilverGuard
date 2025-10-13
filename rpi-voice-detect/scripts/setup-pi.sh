#!/bin/bash

# This script automates the setup process for the Raspberry Pi, including system updates and configurations.

# Update and upgrade the system
echo "Updating and upgrading the system..."
sudo apt update && sudo apt upgrade -y

# Install necessary packages
echo "Installing necessary packages..."
sudo apt install -y python3 python3-pip python3-venv alsa-utils sox

# Set up a virtual environment
echo "Setting up a Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies from requirements.txt..."
pip install -r ../requirements.txt

# Additional setup instructions can be added here

echo "Setup complete! You can now activate the virtual environment using 'source venv/bin/activate'."