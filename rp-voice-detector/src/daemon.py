# Contents of /rp-voice-detector/rp-voice-detector/src/daemon.py

import time
import logging
from audio.capture import AudioCapture
from detection.vad import VoiceActivityDetector
from utils.logger import setup_logging

def main():
    setup_logging()
    logging.info("Starting voice detection daemon...")

    audio_capture = AudioCapture()
    vad = VoiceActivityDetector()

    try:
        while True:
            audio_data = audio_capture.capture_audio()
            if vad.is_voice_active(audio_data):
                logging.info("Voice detected!")
                # Process the audio data as needed
            else:
                logging.info("No voice detected.")
            time.sleep(0.1)  # Adjust sleep time as necessary
    except KeyboardInterrupt:
        logging.info("Daemon stopped by user.")
    finally:
        audio_capture.cleanup()

if __name__ == "__main__":
    main()