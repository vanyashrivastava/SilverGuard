#!/bin/bash

# Start the Raspberry Pi Voice Detection Service

# Navigate to the project directory
cd "$(dirname "$0")/.."

# Activate the virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the main application
python3 src/main.py

# Deactivate the virtual environment
if [ -d "venv" ]; then
    deactivate
fi

echo "Voice detection service has been started."