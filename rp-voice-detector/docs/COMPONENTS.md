# COMPONENTS.md

# Raspberry Pi Voice Detection Project Components

## Overview
This document outlines the various components of the Raspberry Pi Voice Detection project, detailing their responsibilities and interactions within the system.

## Components

### 1. **Main Application**
- **File:** `src/main.py`
- **Description:** Orchestrates the entire application, initializing components, managing the main loop, and handling graceful shutdowns.

### 2. **Audio Handling**
- **Directory:** `src/audio/`
  - **Files:**
    - `audio_input_handler.py`: Manages microphone input and audio capture.
    - `audio_output_handler.py`: Handles speaker output and audio playback.
    - `audio_preprocessor.py`: Preprocesses audio for model inference, including noise reduction and voice activity detection.

### 3. **Voice Detection**
- **Directory:** `src/models/`
  - **Files:**
    - `voice_detection_model.py`: Defines the interface for voice detection models.
    - `model_loader.py`: Manages loading and verifying model files.
    - `model_inference.py`: Executes model inference efficiently.

### 4. **Command Handling**
- **Directory:** `src/commands/`
  - **Files:**
    - `command_router.py`: Routes detected commands to appropriate handlers.
    - `command_handlers.py`: Implements handlers for various voice commands.
    - `action_executor.py`: Executes actions based on detected commands.

### 5. **Utilities**
- **Directory:** `src/utils/`
  - **Files:**
    - `logger.py`: Sets up a logging system for the application.
    - `helpers.py`: Contains helper functions for common tasks.
    - `validators.py`: Implements validation functions for data integrity.

### 6. **Text-to-Speech**
- **Directory:** `src/tts/`
  - **File:** `text_to_speech.py`: Converts text responses into audio output using a TTS engine.

### 7. **Testing**
- **Directory:** `tests/`
  - **Files:**
    - `test_audio_input.py`: Tests for audio input functionality.
    - `test_model.py`: Tests for the voice detection model.
    - `test_commands.py`: Tests for command routing and execution.

### 8. **Scripts**
- **Directory:** `scripts/`
  - **Files:**
    - `setup_audio.sh`: Configures audio devices on the Raspberry Pi.
    - `install_dependencies.sh`: Automates the installation of necessary dependencies.
    - `start_service.sh`: Starts the voice detection service.

### 9. **Documentation**
- **Directory:** `docs/`
  - **Files:**
    - `ARCHITECTURE.md`: Documents the system architecture and data flow.
    - `SETUP.md`: Provides setup instructions and troubleshooting tips.
    - `API.md`: Documents public APIs and usage examples.

### 10. **Systemd Service**
- **File:** `systemd/rp-voice-detector.service`
- **Description:** Contains the configuration for running the voice detection application as a systemd service.

### 11. **Docker**
- **File:** `docker/Dockerfile.pi`
- **Description:** Dockerfile for building the application image for Raspberry Pi.

## Conclusion
This document serves as a guide to understanding the components of the Raspberry Pi Voice Detection project, their roles, and how they interact to create a cohesive voice detection system.