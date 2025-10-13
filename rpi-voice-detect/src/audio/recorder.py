# File: /rpi-voice-detect/rpi-voice-detect/src/audio/recorder.py

import pyaudio
import wave

class AudioRecorder:
    def __init__(self, channels=1, rate=44100, chunk=1024):
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.p = pyaudio.PyAudio()

    def start_recording(self, output_file):
        stream = self.p.open(format=pyaudio.paInt16,
                             channels=self.channels,
                             rate=self.rate,
                             input=True,
                             frames_per_buffer=self.chunk)

        print("Recording...")
        frames = []

        try:
            while True:
                data = stream.read(self.chunk)
                frames.append(data)
        except KeyboardInterrupt:
            print("Recording stopped.")
        finally:
            stream.stop_stream()
            stream.close()
            self.p.terminate()

            with wave.open(output_file, 'wb') as wf:
                wf.setnchannels(self.channels)
                wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
                wf.setframerate(self.rate)
                wf.writeframes(b''.join(frames))
            print(f"Recording saved to {output_file}")

    def close(self):
        self.p.terminate()