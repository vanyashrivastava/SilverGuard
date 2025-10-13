import logging
import os
from logging.handlers import RotatingFileHandler

# Create a logger
logger = logging.getLogger("VoiceDetector")
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
log_file_path = os.path.join(os.path.dirname(__file__), 'voice_detector.log')
handler = RotatingFileHandler(log_file_path, maxBytes=10*1024*1024, backupCount=5)
handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Optional: Add a console handler for output to the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)