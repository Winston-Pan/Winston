import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance1= final*170
print distance1



gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance2= final*170
print distance2





gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance3= final*170
print distance3




gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance4= final*170
print distance4







gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance5= final*170
print distance5




gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance6= final*170
print distance6



gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance7= final*170
print distance7





gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance8= final*170
print distance8




gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance9= final*170
print distance9







gpio.setup(16,gpio.OUT)
gpio.setup(18,gpio.IN)

gpio.output(16,True)
time.sleep(1)
gpio.output(16,False)

while gpio.input(18)==False:
   pass
start=time.time()
while gpio.input(18)==True:
    pass
end=time.time()

final=end-start
distance10= final*170
print distance10

print (distance1+distance2+distance3+distance4+distance5+distance6+distance7+distance8
       +distance9+distance10)/10
gpio.cleanup()
