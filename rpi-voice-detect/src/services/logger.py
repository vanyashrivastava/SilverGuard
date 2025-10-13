# filepath: /rpi-voice-detect/rpi-voice-detect/src/services/logger.py

import logging
import os

# Create a logger
logger = logging.getLogger("VoiceDetectionLogger")
logger.setLevel(logging.DEBUG)

# Create a file handler that logs debug and higher level messages
log_file_path = os.path.join(os.path.dirname(__file__), '../../logs/voice_detection.log')
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

# Create a console handler that logs warning and higher level messages
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message):
    logger.error(message)

def log_debug(message):
    logger.debug(message)