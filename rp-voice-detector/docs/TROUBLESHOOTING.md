# TROUBLESHOOTING.md

## Troubleshooting Guide for Raspberry Pi Voice Detection Project

This document provides solutions to common issues encountered while setting up and running the Raspberry Pi Voice Detection project.

### 1. Installation Issues

**Problem:** Dependencies fail to install.

**Solution:** 
- Ensure your Raspberry Pi is connected to the internet.
- Run `scripts/install_dependencies.sh` to install all required packages. Check for any error messages during installation and resolve them accordingly.

### 2. Audio Input Problems

**Problem:** Microphone not detecting audio.

**Solution:**
- Verify that the microphone is properly connected and recognized by the system. Use the command `arecord -l` to list audio capture devices.
- Check the microphone settings in `config/audio_config.py` to ensure the correct device is selected.
- Test the microphone using `arecord -D plughw:1,0 -f cd test.wav` and play it back with `aplay test.wav`.

### 3. Audio Output Issues

**Problem:** No sound from speakers.

**Solution:**
- Ensure the speakers are connected and powered on.
- Check the speaker settings in `config/audio_config.py` to confirm the correct output device is selected.
- Test audio playback using `aplay /usr/share/sounds/alsa/Front_Center.wav`.

### 4. Voice Detection Not Triggering

**Problem:** The voice detection model does not respond to commands.

**Solution:**
- Verify that the model files are correctly placed in the `models/` directory and that the paths in `config/model_config.py` are accurate.
- Check the confidence thresholds in `config/model_config.py` and adjust them if necessary.
- Ensure that the audio preprocessing steps in `src/audio/audio_preprocessor.py` are functioning correctly.

### 5. System Performance Issues

**Problem:** The application is running slowly or crashing.

**Solution:**
- Monitor system resources using `top` or `htop` to check CPU and memory usage.
- Optimize the model inference settings in `src/models/model_inference.py` to reduce latency.
- Ensure that no other heavy applications are running simultaneously on the Raspberry Pi.

### 6. Service Not Starting

**Problem:** The systemd service fails to start.

**Solution:**
- Check the service status using `systemctl status rp-voice-detector.service` for error messages.
- Review the logs in the `logs/` directory for any relevant error messages.
- Ensure that the service file in `systemd/rp-voice-detector.service` is correctly configured.

### 7. General Debugging Tips

- Use the logging functionality in `src/utils/logger.py` to capture detailed logs of the application’s behavior.
- If you encounter unexpected behavior, consider adding print statements or logging at critical points in the code to trace execution flow.
- Consult the README.md and SETUP.md for additional guidance on configuration and usage.

For further assistance, consider reaching out to the project maintainers or checking online forums for similar issues.