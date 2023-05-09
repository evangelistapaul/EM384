# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:41:01 2023

@author: matthew.mogensen
"""

import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF
    
# A simple function to display a histogram
def simple_hist(values,num_bins,title):
    fig, axis = plt.subplots(figsize =(10, 5))
    axis.hist(values, bins = num_bins)
    plt.title(title)
    # Displaying the histogram
    plt.show()
    

#A simple function to display a line plot of x and y data
def simple_plot(x,y,x_label,title):
    fig, axis = plt.subplots(figsize=(10, 5))
    axis.plot(x,y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.show()
    
#A simple function to plot two line plots of x,y1,y2 data
def simple_two_plot(x,y1,y2,label1,label2,x_label,title):
     fig, ax_values = plt.subplots(figsize=(10, 5))
     plt.plot(x,y1)
     plt.plot(x,y2)
     plt.xlabel(x_label)
     plt.legend([label1,label2])
     plt.title(title)
     
#Problem 1: Bus Depot
#a)
arrivals = stats.poisson.rvs(mu = 30, size = 100000)

#b)
avg = np.mean(arrivals)
print('The mean number of arrivals is',avg)

#c)
simple_hist(arrivals,25,'Histogram of Arrivals')

#d)
x = np.linspace(10,50,1000)
ECDF_function = ECDF(arrivals)
y = ECDF_function(x)
simple_plot(x,y,'Arrivals','CDF and ECDF of arrivals')

#e)
p = ECDF_function(25)
print('The probability of 25 or fewer arrivals is',p)

#f)
p = ECDF_function(22) - ECDF_function(21)
print('The probability of exactly 22 arrivals is',p)

#Problem 2: Mr Cookie
#a)
profit = []
for i in range(0,100000):
    brownie_demand = np.random.randint(200,250)
    cookie_demand = np.random.randint(550,650)
    brownie_wholesale = np.random.rand()*(240-220)+220
    cookie_wholesale = np.random.rand()*(650-580)+580
    brownie_cost = stats.norm.rvs(loc = 1.50, scale = 0.20, size = 1)
    cookie_cost = stats.norm.rvs(loc = 0.40, scale = 0.03, size = 1)
    brownie_price = 2.50
    cookie_price = 1.00
    fixed_cost = 250
    
    #a few calculations, just like we did in Excel
    brownies_sold = min(brownie_demand, brownie_wholesale)
    cookies_sold = min(cookie_demand, cookie_wholesale)
    revenue = brownies_sold * brownie_price + cookies_sold * cookie_price
    cost = brownie_wholesale * brownie_cost[0] + cookie_wholesale * cookie_cost[0] + fixed_cost
    #add profit from this iteration to the end of our profit list
    profit.append(revenue - cost)

avg_profit = np.mean(profit)
print('the expected profit is',avg_profit)

#b)
simple_hist(profit,25,'Histogram of profit')

#c)
ECDF_function2 = ECDF(profit)
p = ECDF_function2(250)
print('The probability of making more than $250 in a day is',1-p)
    