name=raw_input("what is your name?")
print "hi",name
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)

gpio.output(7,gpio.HIGH)
time.sleep(0.1)
gpio.output(7,gpio.LOW)
time.sleep(0.1)
gpio.output(7,gpio.HIGH)
time.sleep(0.1)
gpio.output(7,gpio.LOW)
time.sleep(0.1)
gpio.output(7,gpio.HIGH)
time.sleep(0.1)
gpio.output(7,gpio.LOW)
time.sleep(0.1)
gpio.output(7,gpio.HIGH)
time.sleep(0.1)
gpio.output(7,gpio.LOW)
time.sleep(0.3)

gpio.output(7,gpio.HIGH)
time.sleep(0.1)
gpio.output(7,gpio.LOW)
time.sleep(0.1)
gpio.output(7,gpio.HIGH)
time.sleep(0.1)
gpio.output(7,gpio.LOW)
time.sleep(0.1)

gpio.cleanup()
