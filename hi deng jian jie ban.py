name=raw_input("what is your name ?")
print "hi",name
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)

for i in range(4):
    gpio.output(7,gpio.HIGH)
    time.sleep(1)
    gpio.output(7,gpio.LOW)
    time.sleep(1)
for i in range(2):
    gpio.output(7,gpio.HIGH)
time.sleep(1)
gpio.output(7,gpio.LOW)
time.sleep(1)
