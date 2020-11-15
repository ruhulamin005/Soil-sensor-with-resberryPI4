from time import sleep
from gpiozero import InputDevice

signal = InputDevice(21)  #Pi pin 40

while True:
    if not signal.is_active:
        print("Moisture Detected")
    else:
        print("No moisture")
    sleep(1)

