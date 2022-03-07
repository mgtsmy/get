import RPi.GPIO as P
import time as t 
P.setmode(P.BCM)

LEDS = [21, 20, 16, 12 , 7, 8, 25, 24]

a = 3

for i in range(a):
    for items in LEDS: 
        P.setup(items , P.OUT)
        P.output(items, 1)
        t.sleep(0.2)
        P.output(items,0)
