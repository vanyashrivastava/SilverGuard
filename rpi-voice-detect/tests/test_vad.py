import unittest
from src.audio.vad import VoiceActivityDetector

class TestVoiceActivityDetector(unittest.TestCase):

    def setUp(self):
        self.vad = VoiceActivityDetector()

    def test_initialization(self):
        self.assertIsNotNone(self.vad)

    def test_process_audio(self):
        test_audio_data = b'\x00\x01\x02\x03'  # Example byte data
        result = self.vad.process_audio(test_audio_data)
        self.assertIsInstance(result, bool)  # Assuming process_audio returns a boolean

    def test_threshold_setting(self):
        self.vad.set_threshold(0.5)
        self.assertEqual(self.vad.threshold, 0.5)

    def test_voice_activity_detection(self):
        test_audio_data = b'\x00\x01\x02\x03'  # Example byte data
        self.vad.process_audio(test_audio_data)
        self.assertTrue(self.vad.is_voice_active())  # Assuming this method checks for voice activity

if __name__ == '__main__':
    unittest.main()