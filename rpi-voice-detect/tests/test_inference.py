# filepath: /rpi-voice-detect/rpi-voice-detect/tests/test_inference.py
import unittest
from src.detection.inference import run_inference
from src.audio.preprocess import preprocess_audio

class TestInference(unittest.TestCase):
    def setUp(self):
        self.test_audio_file = 'path/to/test/audio.wav'  # Replace with actual test audio file path
        self.preprocessed_audio = preprocess_audio(self.test_audio_file)

    def test_inference_output(self):
        result = run_inference(self.preprocessed_audio)
        self.assertIsNotNone(result)
        self.assertIn('detected', result)  # Assuming the output contains a 'detected' key

    def test_inference_with_invalid_input(self):
        with self.assertRaises(ValueError):
            run_inference(None)  # Test with None input

if __name__ == '__main__':
    unittest.main()