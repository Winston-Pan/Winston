import RPi.GPIO as gpio
import time
import drive

gpio.setmode(gpio.BOARD)
#gpio.setup(35,gpio.OUT)
#gpio.setup(36,gpio.OUT)
#gpio.setup(37,gpio.OUT)
#gpio.setup(38,gpio.OUT)
gpio.setup(22,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

for i in range(100):
    gpio.output(16,True)
    time.sleep(0.00001)
    gpio.output(16,False)
    while gpio.input(18)==False:
        pass
    start=time.time()
    while gpio.input(18)==True:
        pass
    end=time.time()

    final=end-start
    distance=final*170
    print distance
    if distance<0.3:
        gpio.output(22,True)
        time.sleep(1)
        gpio.output(22,False)
        time.sleep(1)
    if distance>0.3:
        forward(1,35,36,37,38)
    else:
        gpio.output(16,True)
        time.sleep(0.00001)
        gpio.output(16,False)
    
        while gpio.input(18)==False:
                pass
        start=time.time()

        while gpio.input(18)==True:
            pass
        end=time.time()
    
        final=end-start
        distance=final*170
        print distance
gpio.cleanup()
