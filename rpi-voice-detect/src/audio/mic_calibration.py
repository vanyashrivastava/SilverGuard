def calibrate_microphone():
    """Calibrate the microphone to ensure optimal audio input."""
    import pyaudio
    import numpy as np

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Microphone settings
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    # Open the microphone stream
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    print("Calibrating microphone... Please speak into the microphone.")

    # Collect audio data for calibration
    audio_data = []
    for _ in range(0, int(RATE / CHUNK * 5)):  # Collect for 5 seconds
        data = stream.read(CHUNK)
        audio_data.append(np.frombuffer(data, dtype=np.int16))

    # Close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Process the collected audio data
    audio_data = np.concatenate(audio_data)
    mean_volume = np.mean(np.abs(audio_data))

    print(f"Calibration complete. Mean volume: {mean_volume:.2f}")

    return mean_volume


if __name__ == "__main__":
    calibrate_microphone()