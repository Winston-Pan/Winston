import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(12,gpio.OUT)

music=gpio.PWM(12,523)
music.start(50)
time.sleep(1)
music.ChangeDutyCycle(100)
time.sleep(0.2)
music.ChangeDutyCycle(50)
time.sleep(1)
music.ChangeDutyCycle(100)
time.sleep(0.2)

music.ChangeDutyCycle(50)
music.ChangeFrequency(784)
time.sleep(1)
music.ChangeDutyCycle(100)
time.sleep(0.2)
music.ChangeDutyCycle(50)
time.sleep(1)

gpio.cleanup()
