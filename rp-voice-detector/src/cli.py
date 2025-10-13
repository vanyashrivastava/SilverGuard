# File: /rp-voice-detector/rp-voice-detector/src/cli.py

import argparse
import sys
from audio.audio_input_handler import AudioInputHandler
from audio.audio_output_handler import AudioOutputHandler
from detection.vad import VoiceActivityDetector
from utils.logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description='Raspberry Pi Voice Detection CLI')
    parser.add_argument('--start', action='store_true', help='Start the voice detection service')
    parser.add_argument('--stop', action='store_true', help='Stop the voice detection service')
    parser.add_argument('--status', action='store_true', help='Get the status of the voice detection service')
    
    args = parser.parse_args()

    logger = setup_logger()

    if args.start:
        logger.info("Starting the voice detection service...")
        # Initialize components and start the service
        audio_input = AudioInputHandler()
        audio_output = AudioOutputHandler()
        vad = VoiceActivityDetector()
        # Start the main loop or service here
        # ...
        logger.info("Voice detection service started.")
    
    elif args.stop:
        logger.info("Stopping the voice detection service...")
        # Stop the service logic here
        # ...
        logger.info("Voice detection service stopped.")
    
    elif args.status:
        logger.info("Checking the status of the voice detection service...")
        # Check service status logic here
        # ...
        logger.info("Voice detection service is running.")  # or not running

    else:
        logger.error("No valid command provided. Use --start, --stop, or --status.")
        sys.exit(1)

if __name__ == '__main__':
    main()