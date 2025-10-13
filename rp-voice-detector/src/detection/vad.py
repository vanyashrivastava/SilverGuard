def voice_activity_detection(audio_data, sample_rate):
    import numpy as np
    from scipy.signal import find_peaks

    # Parameters for VAD
    threshold = 0.02
    min_silence_length = 0.5  # in seconds
    min_voice_length = 0.1  # in seconds

    # Normalize audio data
    audio_data = audio_data / np.max(np.abs(audio_data))

    # Calculate energy of the audio signal
    energy = np.square(audio_data)

    # Find peaks in the energy signal
    peaks, _ = find_peaks(energy, height=threshold)

    # Convert peak indices to time
    peak_times = peaks / sample_rate

    # Filter peaks based on minimum silence and voice length
    voice_segments = []
    current_segment = []

    for i in range(len(peak_times)):
        if not current_segment:
            current_segment.append(peak_times[i])
        else:
            if peak_times[i] - current_segment[-1] <= min_voice_length:
                current_segment.append(peak_times[i])
            else:
                if len(current_segment) > 1:
                    voice_segments.append((current_segment[0], current_segment[-1]))
                current_segment = [peak_times[i]]

    # Add the last segment if it exists
    if current_segment and len(current_segment) > 1:
        voice_segments.append((current_segment[0], current_segment[-1]))

    return voice_segments


def main():
    import soundfile as sf

    # Load audio file
    audio_data, sample_rate = sf.read('path_to_audio_file.wav')

    # Perform voice activity detection
    voice_segments = voice_activity_detection(audio_data, sample_rate)

    # Print detected voice segments
    for start, end in voice_segments:
        print(f"Voice detected from {start:.2f}s to {end:.2f}s")


if __name__ == "__main__":
    main()