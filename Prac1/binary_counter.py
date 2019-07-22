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
    GPIO.setmode(GPIO.BCM) #Setting up the GPIO

    # Setup GPIO pins
    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Setting up input events
    #GPIO.add_event_detect(5, GPIO.FALLING)
    #GPIO.add_event_detect(6, GPIO.FALLING)

    # Declaring variables
    counter = 0
    bin_counter = bin(counter) + "00000"

    # Main while loop
    while(True):

        #if GPIO.event_detected(5):
         #   counter += 1
          #  if counter > 8:
           #     counter = 0

        #if GPIO.event_detected(6):
         #   counter -= 1
          #  if counter < 0:
           #     counter = 8

        GPIO.wait_for_edge(6, GPIO.FALLING)

        # Translate int to binary representation
        bin_counter = bin(counter) + "00000"

        if bin_counter[2] == '1':
            GPIO.output(21, GPIO.HIGH)
        else:
            GPIO.output(21, GPIO.LOW)

        if bin_counter[3] == '1':
            GPIO.output(20, GPIO.HIGH)
        else:
            GPIO.output(20, GPIO.LOW)

        if bin_counter[4] == '1':
            GPIO.output(16, GPIO.HIGH)
        else:
            GPIO.output(16, GPIO.LOW)



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