from unittest import TestCase
from src.audio.capture import AudioCapture

class TestAudioCapture(TestCase):
    def setUp(self):
        self.audio_capture = AudioCapture()

    def test_initialization(self):
        self.assertIsNotNone(self.audio_capture)

    def test_capture_audio(self):
        audio_data = self.audio_capture.capture()
        self.assertIsNotNone(audio_data)
        self.assertGreater(len(audio_data), 0)

    def test_audio_format(self):
        audio_data = self.audio_capture.capture()
        self.assertEqual(audio_data.format, 'PCM_16')
        self.assertEqual(audio_data.channels, 1)
        self.assertEqual(audio_data.rate, 44100)

    def tearDown(self):
        self.audio_capture.close()