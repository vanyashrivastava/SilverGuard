# USAGE.md

# Raspberry Pi Voice Detection Project Usage Guide

## Overview
This document provides instructions on how to use the Raspberry Pi Voice Detection project. It covers the basic commands, configuration options, and troubleshooting tips to help you get started with the application.

## Prerequisites
Before using the voice detection application, ensure that you have completed the setup as outlined in the `SETUP.md` document. This includes hardware connections, software installations, and configuration settings.

## Starting the Application
To start the voice detection application, run the following command in your terminal:

```bash
python3 src/main.py
```

This command initializes the application and begins listening for voice commands.

## Command Usage
Once the application is running, you can interact with it using voice commands. The following commands are supported:

- **Turn On Light**: Activates the connected light.
- **Turn Off Light**: Deactivates the connected light.
- **Play Music**: Starts playing the predefined music playlist.
- **Stop Music**: Stops the music playback.

Make sure to speak clearly and at a moderate volume for the best recognition results.

## Configuration
The application can be configured by editing the configuration files located in the `configs` directory. Key configuration files include:

- `config.yaml`: General application settings.
- `pulse_audio.yaml`: Audio settings specific to PulseAudio.

Refer to the `config` directory files for detailed configuration options.

## Troubleshooting
If you encounter issues while using the application, consider the following steps:

1. **Check Microphone Connection**: Ensure that the microphone is properly connected and recognized by the system.
2. **Review Logs**: Check the logs in the `logs` directory for any error messages that may indicate what went wrong.
3. **Reconfigure Audio Settings**: If audio input/output is not functioning, revisit the `setup_audio.sh` script to ensure proper configuration.

For further assistance, refer to the `TROUBLESHOOTING.md` document or seek help from the community.

## Conclusion
This guide provides a basic overview of how to use the Raspberry Pi Voice Detection project. For more detailed information, please refer to the other documentation files in the `docs` directory. Happy voice detecting!