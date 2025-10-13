# Contents of /rp-voice-detector/rp-voice-detector/src/main.py

import sys
import signal
from audio.audio_input_handler import AudioInputHandler
from audio.audio_output_handler import AudioOutputHandler
from detection.vad import VoiceActivityDetector
from commands.command_router import CommandRouter
from utils.logger import setup_logger
from utils.config import load_config

logger = setup_logger()
config = load_config()

def signal_handler(sig, frame):
    logger.info("Gracefully shutting down...")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    
    logger.info("Initializing audio input handler...")
    audio_input_handler = AudioInputHandler(config['audio'])
    
    logger.info("Initializing audio output handler...")
    audio_output_handler = AudioOutputHandler(config['audio'])
    
    logger.info("Initializing voice activity detector...")
    vad = VoiceActivityDetector(config['vad'])
    
    logger.info("Initializing command router...")
    command_router = CommandRouter()
    
    logger.info("Starting main loop...")
    while True:
        audio_chunk = audio_input_handler.get_audio_chunk()
        if vad.is_voice_active(audio_chunk):
            command = vad.detect_command(audio_chunk)
            if command:
                command_router.route_command(command)
        else:
            logger.debug("No voice activity detected.")

if __name__ == "__main__":
    main()