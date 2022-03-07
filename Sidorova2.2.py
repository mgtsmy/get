import RPi.GPIO as P
import time as T  
P.setmode(P.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1,0,1,1,0,1,1,0]
for items in dac:
    P.setup(items,P.OUT)


P.output(dac, number)
T.sleep(15)
P.output(dac, 0)