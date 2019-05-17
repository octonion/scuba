#!/usr/bin/env python3

from sys import argv
from math import log2

halftimes = [5,10,20,30,40,60,80,
             100,120,160,200,240,360,480]
m0 = [30.42,25.37,20.54,18.34,17.11,15.79,15.11,
      14.69,14.41,14.06,13.84,13.69,13.45,13.33]

d = float(argv[1])

P0 = 10.0 #-0.627
Pa = d+P0 #-0.627

# Nitrogen

N0 = 0.79*P0
Na = 0.79*Pa

#print("[h, m] = [%s, %s]" % (h, m))

t = []
for i in range(0,14):
    #print(Na,m0[i])
    if (Na-m0[i] <= 0):
        t += [1000]
    else:
        x = (Na-N0)/(Na-m0[i])
        t += [halftimes[i]*log2(x)]

ndl, idx = min((val, idx+1) for (idx, val) in enumerate(t))
print("NDL = %s" % ndl)
print("Controlling compartment = %s" % idx)

