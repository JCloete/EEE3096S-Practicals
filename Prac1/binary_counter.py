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

# Global counter variable to be used in callbacks
counter = 0

# Callback to increase counter by 1
def increase_counter(channel):
    global counter  # global flag to allow counter variable to be adjusted
    
    if counter < 7:
        counter += 1
    else:
        counter = 0

# Callback to decrease counter by 1
def decrease_counter(channel):
    global counter  # global flag to allow counter variable to be adjusted
    
    if counter > 0:
        counter -= 1
    else:
        counter = 7


# Logic that you write
def main():

    #Setting up the GPIO
    GPIO.setmode(GPIO.BCM) 

    # Setup GPIO pins
    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Setting up input events
    GPIO.add_event_detect(6, GPIO.FALLING, callback=increase_counter, bouncetime=200)
    GPIO.add_event_detect(5, GPIO.FALLING, callback=decrease_counter, bouncetime=200)

    # Main while loop
    while(True):
        # Translate int to binary representation
        bin_counter = "00" + bin(counter)[2:]  # leading zeroes ensure that the array index is never out of bounds

        # [-1] is the least significant bit i.e 2^0....... [-2] 2^1....... [-3] 2^2
        # HIGHEST POSSIBLE NUMBER IS 7

        # Following statements check whether bit they represent is 1 or 0 and turn on accordingly
        # LSB
        if bin_counter[-1] == '1':
            GPIO.output(16, GPIO.HIGH)
        else:
            GPIO.output(16, GPIO.LOW)

        # Middle Bit
        if bin_counter[-2] == '1':
            GPIO.output(20, GPIO.HIGH)
        else:
            GPIO.output(20, GPIO.LOW)

        # MSB
        if bin_counter[-3] == '1':
            GPIO.output(21, GPIO.HIGH)
        else:
            GPIO.output(21, GPIO.LOW)

        time.sleep(0.05) # To ensure the pins transistion properly







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
    except Exception as e:
        print("An unusual error occured:")
        print(e)
        # Turn off GPIOs
        GPIO.cleanup()
