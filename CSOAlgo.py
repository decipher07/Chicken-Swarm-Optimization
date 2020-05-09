import numpy as np 
import matplotlib 
import random 
import pandas as pd 
import sklearn

''' 
    The Fitness Function Defines The Fitness of the indiviual in the Group. The Group's Leader ie Rooster is the most Fittest in The Group to Which it Accounts as the Reason
'''
def fitness_function (x):
    
    ''' 
        The Function Takes in an Chromosome and performs The Test Under a Selected Value of
         'w': Constant Controlling The Importance Of Classification 
         'E': Classification Error
         'x': Vector 
         'N': Total Number of Features In The Dataset
    '''
    w = 0.00000001
    E = 0.00000002
    N = 32 
    
    sum = 0 # Sum For Countering The Total No Of Non Negative Numbers in The Dataset

    for i in x[0]:
        if i == 1 :
            sum+=1
    
    fitness_value  = w*E + ((1-w)*sum)/N

    return fitness_value 

x = np.random.randint(0, 2, (1, 32))
fitness =  fitness_function(x)

print (fitness)