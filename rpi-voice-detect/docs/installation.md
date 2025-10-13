# Installation Instructions for Raspberry Pi Voice Detection Project

## Prerequisites

Before you begin the installation, ensure that you have the following:

- A Raspberry Pi (preferably Raspberry Pi 3 or later)
- Raspbian OS installed and updated
- Internet connection for downloading dependencies

## Step 1: Update Your System

Open a terminal on your Raspberry Pi and run the following commands to update your system:

```bash
sudo apt update
sudo apt upgrade -y
```

## Step 2: Clone the Repository

Clone the project repository from GitHub (replace `<repository-url>` with the actual URL):

```bash
git clone <repository-url>
cd rpi-voice-detect
```

## Step 3: Install Dependencies

Run the installation script to install all necessary dependencies:

```bash
cd scripts
chmod +x install-deps.sh
./install-deps.sh
```

This script will install Python packages listed in `requirements.txt` and any additional system packages required for audio processing.

## Step 4: Configure Microphone Settings

Edit the `configs/microphone.yaml` file to set your microphone's sample rate and channels according to your hardware specifications. Ensure that the microphone is connected to the Raspberry Pi.

## Step 5: Set Up Hardware Components

Follow the instructions in `docs/hardware-setup.md` to connect any additional hardware components, such as GPIO devices or I2S audio interfaces.

## Step 6: Run the Application

You can start the voice detection application using the provided script:

```bash
cd scripts
chmod +x start.sh
./start.sh
```

This will initialize all components and start the voice detection service.

## Troubleshooting

If you encounter any issues during installation or while running the application, refer to the `docs/usage.md` for common problems and solutions.

## Conclusion

You have successfully installed the Raspberry Pi Voice Detection project. For further usage instructions, please refer to the documentation in the `docs` directory.