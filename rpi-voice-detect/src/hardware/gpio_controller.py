# File: /rpi-voice-detect/rpi-voice-detect/src/hardware/gpio_controller.py

import RPi.GPIO as GPIO

class GPIOController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
        self.pins = {}

    def setup_pin(self, pin_number, direction):
        """Setup a GPIO pin as input or output."""
        if direction not in [GPIO.IN, GPIO.OUT]:
            raise ValueError("Direction must be GPIO.IN or GPIO.OUT")
        GPIO.setup(pin_number, direction)
        self.pins[pin_number] = direction

    def read_pin(self, pin_number):
        """Read the value of an input pin."""
        if pin_number not in self.pins or self.pins[pin_number] != GPIO.IN:
            raise ValueError("Pin not set up as input")
        return GPIO.input(pin_number)

    def write_pin(self, pin_number, value):
        """Write a value to an output pin."""
        if pin_number not in self.pins or self.pins[pin_number] != GPIO.OUT:
            raise ValueError("Pin not set up as output")
        GPIO.output(pin_number, value)

    def cleanup(self):
        """Clean up GPIO settings."""
        GPIO.cleanup()