# generates random complex numbers on the unit circle, adds them up to make them into ICCNs,
# and then records if they landed inside the unit circle centered at the origin.
# This is repeated for a number of iterations, and the proportion of ICCNs that land is recorded.
# The entire process is then repeated to obtain multiple sample proportions.

import random
import math
import sys

M = 100 # number of samples taken of size n
m = 0 # index

N = 10000 # number of trials in a sample (sample size)
n = 0 #index

a = 0 # number of successes in one sample

b = int(input("Enter n, the number of complex numbers to iterate..."))

successes=[] # list of proportions of success for all samples

while(m<M): # run m samples
    while(n<N): # run n trials
        real_net = 0
        imaginary_net = 0
        i = 0
        while(i<b): # create ICCN by iterating b circular complex numbers
            alpha_i = random.random()*2*math.pi
            real = math.cos(alpha_i)
            imaginary = math.sin(alpha_i)
            real_net = real_net + real
            imaginary_net = imaginary_net + imaginary
            i = i + 1
        z_net = math.sqrt((real_net**2)+(imaginary_net**2))

        # success counter (with floating point error tolerance)
        if(z_net<0.999999999999999):
            a = a + 1
        n = n + 1
    
    print(a/n)
    successes.append(a/n)
    m = m+1
    n = 0
    a = 0

print(successes) # print all sample proportions of success in M samples
