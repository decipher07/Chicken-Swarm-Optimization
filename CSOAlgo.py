import numpy as np 
import matplotlib 
import math
import random
''' 
    The Fitness Function Defines The Fitness of the indiviual in the Group. The Group's Leader ie Rooster is the most Fittest in The Group to Which it Accounts as the Reason
'''

# Defining the Total Noumber of Features in the Dataset 
Dn = 32 

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
    N = 32 # For an Example 
    
    sum = 0 # Sum For Countering The Total No Of Non Negative Numbers in The Dataset

    for i in x[0]:
        if i == 1 :
            sum+=1
    
    ''' 
        The Fitness Value is Defined by the Given Formula
        The Expression Yields Different Results for Different Value of w and E 
    '''

    fitness_value  = w*E + ((1-w)*sum)/N

    return fitness_value 

# x = np.random.randint(0, 2, (1, 32))
# fitness =  fitness_function(x)

''' 
    Understanding The Algo , We have 

    Species : Chicken 
    Members : Roosters (The Head Male Chicken)
              Hens (The Female Chickens)
              Chicks (The Baby Chickens )


    Thereby , A Class Containing Them Will Define Appropriate Properties and Updation Constraints .

    ------------------------------------------XXXXXXXXXXXXXXXXXX----------------------------------------------------

    Let Us Suppose We have A Population of 10 Chickens . Now , To Distribute Equally Among every Group. We need to have 2 Groups Therefore , The Appropriate Distribution will be 2 Roosters , Each Belonging to Different Groups and 4 Hens , Each Pair Belonging to Different Group and Rest Of Them as Chick .

    To Divide Chickens into Appropriate Groups , Let Us Divide Them by A Number , Which Yields Slightly Mean Equal Results .

    According To Chicken Swarm Nature , The Chicken are being Compared on their level of Fitness , The Category To which They belong , The Group it Belongs to and Position Which Changes After Every Iteration .
    

'''

class Chicken :

    # Defining Constructor

    def __init__(self):
        self.sample_chicken_comparing_stack = np.random.randint(0,2, (1, Dn)) # Sets the Basic Binary String of Length to The Number of Features, This is needed to Compare the New Generation with the Existting One , And Changing The Orderof Fitness 

        # Checking if the String is Totally Made up os 0's or Nor
        # If Yes , It Needs to Change , or It will give a Zero Feature Error 

        while (np.all(self.sample_chicken_comparing_stack == 0 )):
            self.sample_chicken_comparing_stack = np.random.randint(0, 2, (1, Dn))

        self.original_chicken_string = self.sample_chicken_comparing_stack # For Initial Setup 
        self.next_position_to_which_chicken_will_move = np.random.random((Dn,)) # For The Initial Setup , Later Will Store the Next Position which will be evaluated for Fitness and Storing in the string or Not 
        self.original_position = self.next_position_to_which_chicken_will_move
        self.fitness = -1 # Inititally Not Evaluating the Fitness
        self.group = -1 # Inirially Not Evaluating Any Group 
        self.species_name = "none" # Later Will change to Rooster, Chicken or Hen 

    ''' 
        A Function Which is Subjected to Get The Fitness Count of the Hen based on The Criteria
        The Function is Called Twice , First When The Assignment for Both Rooster and Chickens is done and At Last when All The Fitness is compared and the best is among to be chosen 
    '''

    def evaluate(self):
        self.original_position = self.next_position_to_which_chicken_will_move
        self.original_chicken_string = self.sample_chicken_comparing_stack
        self.fitness = fitness_function(self.original_chicken_string)
    
    
