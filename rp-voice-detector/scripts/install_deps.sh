#!/bin/bash

# Update the package list
sudo apt update

# Upgrade installed packages
sudo apt upgrade -y

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install required Python packages
pip3 install pyaudio numpy scipy vosk pyttsx3 requests pytest

# Install additional dependencies for audio processing
sudo apt install -y portaudio19-dev

# Clean up
sudo apt autoremove -y

echo "All dependencies have been installed successfully."