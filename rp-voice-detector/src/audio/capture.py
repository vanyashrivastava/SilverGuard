import pyaudio
import wave

class AudioCapture:
    def __init__(self, chunk=1024, format=pyaudio.paInt16, channels=1, rate=44100):
        self.chunk = chunk
        self.format = format
        self.channels = channels
        self.rate = rate
        self.p = pyaudio.PyAudio()
        self.stream = None

    def start_stream(self):
        self.stream = self.p.open(format=self.format,
                                   channels=self.channels,
                                   rate=self.rate,
                                   input=True,
                                   frames_per_buffer=self.chunk)

    def stop_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

    def record(self, seconds):
        frames = []
        self.start_stream()
        for _ in range(0, int(self.rate / self.chunk * seconds)):
            data = self.stream.read(self.chunk)
            frames.append(data)
        self.stop_stream()
        return frames

    def save_to_file(self, frames, filename):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))

    def __del__(self):
        self.p.terminate()