# filepath: /rpi-voice-detect/rpi-voice-detect/src/cli.py

import argparse
from src.audio.recorder import Recorder
from src.detection.inference import Inference
from src.services.logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Voice Detection CLI")
    parser.add_argument('--record', action='store_true', help='Record audio')
    parser.add_argument('--detect', action='store_true', help='Detect voice in recorded audio')
    parser.add_argument('--calibrate', action='store_true', help='Calibrate microphone')
    
    args = parser.parse_args()
    logger = setup_logger()

    if args.record:
        logger.info("Starting audio recording...")
        recorder = Recorder()
        recorder.start_recording()
        logger.info("Recording... Press Ctrl+C to stop.")
        try:
            recorder.wait_for_stop()
        except KeyboardInterrupt:
            recorder.stop_recording()
            logger.info("Recording stopped.")

    if args.detect:
        logger.info("Starting voice detection...")
        inference = Inference()
        inference.run_detection()
        logger.info("Voice detection completed.")

    if args.calibrate:
        logger.info("Calibrating microphone...")
        # Add microphone calibration logic here
        logger.info("Microphone calibration completed.")

if __name__ == "__main__":
    main()