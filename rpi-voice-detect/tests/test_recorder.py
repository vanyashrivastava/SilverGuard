import unittest
from src.audio.recorder import AudioRecorder

class TestAudioRecorder(unittest.TestCase):

    def setUp(self):
        self.recorder = AudioRecorder()

    def test_initialization(self):
        self.assertIsNotNone(self.recorder)

    def test_start_recording(self):
        self.recorder.start_recording()
        self.assertTrue(self.recorder.is_recording)

    def test_stop_recording(self):
        self.recorder.start_recording()
        self.recorder.stop_recording()
        self.assertFalse(self.recorder.is_recording)

    def test_recorded_audio(self):
        self.recorder.start_recording()
        audio_data = self.recorder.get_recorded_audio()
        self.recorder.stop_recording()
        self.assertIsNotNone(audio_data)
        self.assertGreater(len(audio_data), 0)

if __name__ == '__main__':
    unittest.main()