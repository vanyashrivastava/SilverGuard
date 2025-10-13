#!/bin/bash

# This script installs necessary dependencies for the Raspberry Pi voice detection project.

# Update package list and upgrade installed packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip if not already installed
sudo apt install -y python3 python3-pip

# Install required Python packages
pip3 install pyaudio numpy scipy vosk pyttsx3 requests pytest

# Additional system dependencies for audio processing
sudo apt install -y portaudio19-dev

# Clean up
sudo apt autoremove -y

echo "All dependencies have been installed successfully."