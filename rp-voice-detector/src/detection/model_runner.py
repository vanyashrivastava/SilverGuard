# Contents of /rp-voice-detector/rp-voice-detector/src/detection/model_runner.py

import numpy as np
import pyaudio
from vosk import Model, KaldiRecognizer

class ModelRunner:
    def __init__(self, model_path):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

    def start_recognition(self, audio_stream):
        while True:
            data = audio_stream.read(4000, exception_on_overflow=False)
            if not data:
                break
            if self.recognizer.AcceptWaveform(data):
                result = self.recognizer.Result()
                self.process_result(result)
            else:
                partial_result = self.recognizer.PartialResult()
                self.handle_partial_result(partial_result)

    def process_result(self, result):
        print("Final Result:", result)

    def handle_partial_result(self, partial_result):
        print("Partial Result:", partial_result)

    def stop_recognition(self):
        self.recognizer = None
        print("Recognition stopped.")