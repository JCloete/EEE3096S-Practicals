#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Jason Cloete
Student Number: CLTJAS004
Prac: Practical 1
Date: 22/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time

# Logic that you write
def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, GPIO.HIGH)
	time.sleep(10)
	GPIO.output(21, GPIO.LOW)
	time.sleep(5)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
