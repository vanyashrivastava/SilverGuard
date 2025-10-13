# Usage Instructions for the Raspberry Pi Voice Detection Project

## Overview
This document provides detailed instructions on how to effectively use the Raspberry Pi Voice Detection system. It covers the basic commands, configuration settings, and operational guidelines to ensure optimal performance.

## Getting Started
1. **Setup**: Ensure that the Raspberry Pi is properly set up with the necessary hardware components as outlined in the `hardware-setup.md` document.
2. **Installation**: Follow the installation instructions in `installation.md` to install all required software dependencies.

## Running the Voice Detection System
To start the voice detection system, execute the following command in your terminal:

```bash
bash scripts/start.sh
```

This script will initialize all components of the voice detection system, including audio recording, model inference, and any necessary services.

## Configuration
Before running the system, you may want to adjust the configuration files located in the `configs` directory:

- **microphone.yaml**: Modify settings such as sample rate and channels to match your microphone specifications.
- **model.yaml**: Update the model path and parameters to ensure the voice detection model is correctly configured.

## Command-Line Interface
The system provides a command-line interface for interacting with various functionalities. You can access the CLI by running:

```bash
python3 src/cli.py
```

### Available Commands
- `start`: Begin the voice detection process.
- `stop`: Stop the voice detection process.
- `status`: Check the current status of the voice detection system.

## Voice Detection Process
Once the system is running, it will continuously listen for voice input. The voice activity detection (VAD) module will filter out non-speech segments, allowing the model to focus on relevant audio data.

### Output
The results of the voice detection will be logged and can be viewed in the console or in the log files managed by the logger service.

## Troubleshooting
If you encounter issues while using the system, consider the following steps:
- Check the microphone connections and ensure it is functioning properly.
- Review the logs for any error messages that may indicate what went wrong.
- Ensure that all dependencies are correctly installed as per the `requirements.txt` and `requirements-dev.txt`.

## Conclusion
This guide provides the essential information needed to operate the Raspberry Pi Voice Detection system effectively. For further assistance, refer to the other documentation files or reach out to the development team.