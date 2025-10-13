# File: /rpi-voice-detect/rpi-voice-detect/src/main.py

"""
Raspberry Pi Voice Detection Project
Main entry point for the voice detection application.
"""

import logging
from src.audio.recorder import AudioRecorder
from src.audio.preprocess import preprocess_audio
from src.detection.inference import run_inference
from src.services.logger import setup_logging

def main():
    """Run the voice detection application."""
    setup_logging()
    logging.info("Starting the Raspberry Pi Voice Detection application.")

    try:
        # Initialize audio recorder
        recorder = AudioRecorder()
        logging.info("Audio recorder initialized.")

        while True:
            # Record audio
            audio_data = recorder.record()
            logging.info("Audio recorded.")

            # Preprocess audio
            processed_data = preprocess_audio(audio_data)
            logging.info("Audio preprocessed.")

            # Run inference on processed audio
            result = run_inference(processed_data)
            logging.info(f"Inference result: {result}")

    except KeyboardInterrupt:
        logging.info("Application interrupted by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()