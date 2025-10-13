#!/bin/bash

# This script calibrates the microphone for optimal audio input.
# It records a short audio sample and analyzes the levels to adjust settings.

# Constants
MIC_DEVICE="default"  # Change this to your microphone device if necessary
RECORDING_DURATION=5   # Duration of the recording in seconds
OUTPUT_FILE="calibration.wav"

# Function to record audio
record_audio() {
    echo "Recording audio for $RECORDING_DURATION seconds..."
    arecord -D $MIC_DEVICE -f cd -t wav -d $RECORDING_DURATION $OUTPUT_FILE
    echo "Recording complete. Saved to $OUTPUT_FILE."
}

# Function to analyze audio levels
analyze_audio() {
    echo "Analyzing audio levels..."
    # Use sox to analyze the audio levels
    sox $OUTPUT_FILE -n stat 2>&1 | grep 'RMS'
}

# Main script execution
record_audio
analyze_audio

echo "Microphone calibration complete."