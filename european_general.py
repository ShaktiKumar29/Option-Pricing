# -*- coding: utf-8 -*-

#Calculating the price of an European Option Via Binomial Trees
#Attempting to code for various steps (2-step, 3-step, ....)

#Importing the libraries
import numpy as np #numerical python
import pandas as pd #python dataframe
import math

#Returns the payoff of put/call option as per specification
def payoff(X, Y):
    return (max((1-2*option_type)*(X-Y), 0))

#Required Data
strike_price = 21
underlying_price = 20 #Price at t=0
time_step = 0.25 #Frequency of each time step
r = 0.12 #rate of interest
u = 1.1 # upward movement
d = 0.9 #downward movement
option_type = 1 #0 for put & 1 for call

no_steps = 4 #Number of time-steps
no_nodes = (no_steps+1)*(no_steps+2)/2
print("No. of nodes: ", no_nodes)

#Creating a 2-D array to store the option price at each node & time stamp
rows, cols = (no_steps+1, no_steps+1)
a = [[0 for i in range(cols)] for j in range(rows)]
a[0][0] = underlying_price

for i in range(1, no_steps+1): #Iterating through each time step
    for j in range(i+1):
        if j < i/2:
            a[i][j] = a[i-1][j]*u
        else:
            a[i][j] = a[i-1][j-1]*d
#        print("a[",i,"][",j,"]:", a[i][j])
        

#Calculating the risk-neutral probability
p = (math.exp(r*time_step)-d)/(u-d)
print("\nRisk-Neutral Probability:", round(p, 4),"\n")

#Calculating the payoff at each node
for i in range(no_steps+1):
    for j in range(i+1):
        a[i][j] = round(payoff(strike_price, a[i][j]), 4)
        print("a[",i,"][",j,"]:", a[i][j])

for i in range(no_steps, 0, -1):
    for j in range(i):
        if (a[i][j] == 0) & (a[i][j+1] == 0):
            a[i-1][j] = 0
        else:
            a[i-1][j] = round((a[i][j]*p + a[i][j+1]*(1-p))*math.exp(-r*time_step), 4)

print("\nOption Price: ", a[0][0])