# filepath: /rpi-voice-detect/rpi-voice-detect/src/detection/inference.py

import numpy as np
import torch
from src.detection.model import VoiceDetectionModel
from src.audio.preprocess import preprocess_audio

class Inference:
    def __init__(self, model_path):
        self.model = VoiceDetectionModel(model_path)
        self.model.load()

    def run(self, audio_data):
        preprocessed_data = preprocess_audio(audio_data)
        input_tensor = torch.tensor(preprocessed_data).float().unsqueeze(0)  # Add batch dimension
        with torch.no_grad():
            output = self.model(input_tensor)
        return output.numpy()

    def close(self):
        self.model.close()