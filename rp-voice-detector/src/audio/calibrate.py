def calibrate_microphone():
    import pyaudio
    import numpy as np

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Set parameters for audio input
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    # Open stream
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    print("Calibrating microphone... Please make some noise.")

    # Record for a short period
    frames = []
    for i in range(0, int(RATE / CHUNK * 5)):  # 5 seconds
        data = stream.read(CHUNK)
        frames.append(np.frombuffer(data, dtype=np.int16))

    # Close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Convert frames to a single array
    audio_data = np.hstack(frames)

    # Calculate calibration values
    mean_volume = np.mean(np.abs(audio_data))
    print(f"Mean volume: {mean_volume}")

    # Save calibration values to a file
    with open("calibration_values.txt", "w") as f:
        f.write(f"Mean Volume: {mean_volume}\n")

    print("Calibration complete. Values saved to calibration_values.txt.")

if __name__ == "__main__":
    calibrate_microphone()