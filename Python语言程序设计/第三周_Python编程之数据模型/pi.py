from math import sqrt
from random import random
from time import clock

DARTS = 1500
hits = 0

clock()

for i in range(1, DARTS):
    x, y = random(), random()
    dist = sqrt(x**2+y**2)
    if dist <= 1.0:
        hits += 1
pi = 4*(hits/DARTS)
print("Pi is %s " % pi)
print("Time is %-5.5ss" % clock())
