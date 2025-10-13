from unittest import TestCase
from src.detection.vad import VoiceActivityDetector

class TestVoiceActivityDetector(TestCase):
    def setUp(self):
        self.vad = VoiceActivityDetector()

    def test_voice_activity_detection(self):
        # Simulate audio input for voice activity detection
        test_audio = "path/to/test/audio.wav"  # Replace with actual test audio path
        result = self.vad.detect_voice_activity(test_audio)
        self.assertTrue(result)

    def test_silence_detection(self):
        # Simulate audio input for silence detection
        test_audio_silence = "path/to/test/silence.wav"  # Replace with actual silence audio path
        result = self.vad.detect_voice_activity(test_audio_silence)
        self.assertFalse(result)

    def tearDown(self):
        self.vad = None

if __name__ == '__main__':
    unittest.main()