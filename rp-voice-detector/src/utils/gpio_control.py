def setup_gpio(pin_number, mode):
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
    GPIO.setup(pin_number, mode)

def cleanup_gpio():
    import RPi.GPIO as GPIO
    GPIO.cleanup()

def read_gpio(pin_number):
    import RPi.GPIO as GPIO
    return GPIO.input(pin_number)

def write_gpio(pin_number, value):
    import RPi.GPIO as GPIO
    GPIO.output(pin_number, value)