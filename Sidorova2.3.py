import RPi.GPIO as P

P.setmode(P.BCM)
P.cleanup()

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

P.setup(leds, P.OUT)
P.setup(aux, P.IN)
while True:
    for i in range(8):
       P.output(leds[i], P.input(aux[i]))
P.cleanup()