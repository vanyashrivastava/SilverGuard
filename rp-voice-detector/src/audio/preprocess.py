from scipy.io import wavfile
import numpy as np

class AudioPreprocessor:
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate

    def load_audio(self, file_path):
        sample_rate, data = wavfile.read(file_path)
        if sample_rate != self.sample_rate:
            raise ValueError(f"Sample rate mismatch: expected {self.sample_rate}, got {sample_rate}")
        return data

    def normalize(self, audio_data):
        max_val = np.max(np.abs(audio_data))
        if max_val > 0:
            return audio_data / max_val
        return audio_data

    def remove_silence(self, audio_data, threshold=0.01):
        non_silent_indices = np.where(np.abs(audio_data) > threshold)[0]
        if non_silent_indices.size > 0:
            return audio_data[non_silent_indices[0]:non_silent_indices[-1] + 1]
        return audio_data

    def preprocess(self, file_path):
        audio_data = self.load_audio(file_path)
        audio_data = self.normalize(audio_data)
        audio_data = self.remove_silence(audio_data)
        return audio_data