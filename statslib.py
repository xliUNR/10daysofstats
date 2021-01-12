#!/usr/bin/python3

# This contains the stats library that I wrote for the exercises
# imports
import sys
import math
# calculates the mean of data
def mean(data, size):
    return float(sum(data)/size)
# calculate std_dev
def std_dev(data, size):
    dist_sum = 0
    u = mean(data, size)
    for i in range(size):
        dist_sum += (data[i] - u)**2
        
    return math.sqrt(dist_sum / size)
     
# median function 
# Data must be sorted
def median(sorted_data, start, end):
    m = int((end + start) / 2)
    
    if (end - start ) % 2 == 0:
        return int((sorted_data[m] + sorted_data[m-1]) / 2)
    else:
        return sorted_data[m]
    
#Quartile function that returns a tuple of the three quartiles        
def quartiles(data, size):
    Q1 = Q2 = Q3 = 0
    m = int(size / 2)
    # First data must be sorted
    data.sort();

    # calculate Q2
    Q2 = median(data, 0, size)

    # calculate quartiles using the median function depending on if size of data is even or odd
    if size % 2 == 0:
        Q1 = median(data, 0, m)
        Q3 = median(data, m, size)
    else:
        Q1 = median(data, 0, m)
        Q3 = median(data, m+1, size)    
    
    return (Q1, Q2, Q3)

# returns the interquartile range        
def interquartile_range(data, size):
      Q1, Q2, Q3 = quartiles(data, size)
      return float(Q3 - Q1)
        
# simple recursive factorial function
def factorial(n):
    if( n < 0):
        raise Exception("Cannot take factorial of negative number.")
    elif( n > 1):
        return n * factorial(n-1)
    else:
        return 1
    
# Calculates probability of a combination given 
# n: number of trials
# x: number of successes

def combination(n, x):
    numerator = factorial(n)
    denom = factorial(x) * factorial((n-x))
    return float(numerator / denom)

# calculate binomial probabilities
# n: number of trials
# x: number of successes
# p: probability of success   
def binomial(n, x, p):
    return combination(n, x) * (p**x) * ((1 - p)**(n-x)) 
 
def geometric_dist(n, p, q):
    return (q**(n-1))*p

# poisson probability
# Where X is expected value 
# Where S is random value
def poisson(X, s):
    return ( (X**s) * math.exp(-X) ) / math.factorial(s)


