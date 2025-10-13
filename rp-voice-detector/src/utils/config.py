# Contents of /rp-voice-detector/rp-voice-detector/src/utils/config.py

import os

class Config:
    def __init__(self):
        self.audio_config = self.load_audio_config()
        self.model_config = self.load_model_config()
        self.system_config = self.load_system_config()

    def load_audio_config(self):
        return {
            "microphone": {
                "device_index": 0,
                "sample_rate": 16000,
                "channels": 1,
                "buffer_size": 1024
            },
            "speaker": {
                "volume": 0.5,
                "output_device": "default"
            },
            "audio_format": "wav"
        }

    def load_model_config(self):
        return {
            "model_path": os.path.join(os.getcwd(), "models", "voice_detection_model.pb"),
            "wake_word": "hello",
            "confidence_threshold": 0.7,
            "preprocessing": {
                "noise_reduction": True,
                "normalization": True
            }
        }

    def load_system_config(self):
        return {
            "log_level": "INFO",
            "gpio_pins": {
                "led": 17,
                "button": 27
            },
            "error_handling": {
                "retry_attempts": 3,
                "timeout": 5
            }
        }