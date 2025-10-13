class VoiceActivityDetector:
    def __init__(self, threshold=0.01):
        self.threshold = threshold

    def is_speech(self, audio_chunk):
        """Determine if the given audio chunk contains speech."""
        return max(audio_chunk) > self.threshold

    def filter_speech(self, audio_stream):
        """Filter out non-speech segments from the audio stream."""
        speech_segments = []
        current_segment = []

        for chunk in audio_stream:
            if self.is_speech(chunk):
                current_segment.append(chunk)
            else:
                if current_segment:
                    speech_segments.append(current_segment)
                    current_segment = []

        if current_segment:
            speech_segments.append(current_segment)

        return speech_segments

    def process_audio(self, audio_stream):
        """Process the audio stream to extract speech segments."""
        return self.filter_speech(audio_stream)