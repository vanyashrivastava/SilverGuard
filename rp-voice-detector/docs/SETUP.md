# SETUP.md

# Raspberry Pi Voice Detection Project Setup Guide

## Hardware Requirements
1. **Raspberry Pi** (Model 3 or later recommended)
2. **USB Microphone** or compatible microphone
3. **Speakers** (USB or 3.5mm jack)
4. **SD Card** (at least 16GB)
5. **Power Supply** for Raspberry Pi
6. **Internet Connection** (for downloading dependencies)

## Software Requirements
1. **Raspberry Pi OS** (preferably the latest version)
2. **Python 3.7 or later**
3. **pip** (Python package installer)
4. **git** (for version control)
5. **systemd** (for service management)

## Installation Steps

### Step 1: Prepare the Raspberry Pi
1. Flash the Raspberry Pi OS onto the SD card using tools like Balena Etcher or Raspberry Pi Imager.
2. Insert the SD card into the Raspberry Pi and boot it up.
3. Connect to the internet and update the system:
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

### Step 2: Install Dependencies
1. Clone the project repository:
   ```bash
   git clone <repository-url>
   cd rp-voice-detector
   ```
2. Run the installation script to install required packages:
   ```bash
   chmod +x scripts/install_deps.sh
   ./scripts/install_deps.sh
   ```

### Step 3: Configure Audio Devices
1. Run the audio setup script to configure your microphone and speakers:
   ```bash
   chmod +x scripts/setup_audio.sh
   ./scripts/setup_audio.sh
   ```

### Step 4: Set Up Systemd Service
1. Copy the systemd service file to the systemd directory:
   ```bash
   sudo cp systemd/rp-voice-detector.service /etc/systemd/system/
   ```
2. Enable and start the service:
   ```bash
   sudo systemctl enable rp-voice-detector.service
   sudo systemctl start rp-voice-detector.service
   ```

### Step 5: Verify Installation
1. Check the status of the service to ensure it is running:
   ```bash
   sudo systemctl status rp-voice-detector.service
   ```
2. If there are issues, refer to the troubleshooting section.

## Troubleshooting
- If the service fails to start, check the logs for errors:
  ```bash
  journalctl -u rp-voice-detector.service
  ```
- Ensure all hardware is properly connected and recognized by the system.
- Verify that all dependencies are installed correctly.

## Additional Notes
- For further configuration, refer to the `configs` directory for YAML configuration files.
- Consult the `docs` directory for detailed documentation on components and usage.