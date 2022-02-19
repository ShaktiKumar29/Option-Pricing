# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 22:27:12 2022

@author: skuma
"""

#Calculating the price of an European Option Via Binomial Trees
#Only 2-step scenario has been considered here

'''

                                  |------------(D)
                                  |
                                  |
                    |------------(B)
                    |             |
                    |             |------------
           (A)------                           (E)
                    |             |------------
                    |             |
                    |------------(C)
                                  |
                                  |
                                  |------------(F)
                                   
#(A) is the current time period
#(B) & (C) is at next time step and so on...
'''

#Importing the libraries
import numpy as np #numerical python
import pandas as pd #python dataframe
import math

#Returns the payoff of put/call option as per specification
def payoff(X, Y):
    return (max((1-2*option_type)*(X-Y), 0))

#Required Data
strike_price = 52
underlying_price = 50 #Price at t=0
time_step = 1
r = 0.05 #rate of interest
u = 1.2 # upward movement
d = 0.8 #downward movement

#Calculating risk-neutral probability of upward movement
p = (math.exp(r*time_step) - d)/(u-d)
print("Probability:", p)
#Subsequently (1-p) is the risk-neutral probability of downward movement

option_type = 0 #0 for put & 1 for call

#Pre-computing PV's of upward & downward
upward_pv = p*math.exp(-r*time_step)
downward_pv = (1-p)*math.exp(-r*time_step)

#Upward probability
B = underlying_price*u
D = B*u

#Downward probability
C = underlying_price*d
F = C*d
E = C*u

#print(F) 

#Calculating option price
B = upward_pv*payoff(strike_price,D) + downward_pv*payoff(strike_price,E)
C = upward_pv*payoff(strike_price,E) + downward_pv*payoff(strike_price,F)

print("B:", B)
print("C:", C)

option_price = B*p*math.exp(-r*time_step) + C*(1-p)*math.exp(-r*time_step)
print("Option Price:", option_price)    