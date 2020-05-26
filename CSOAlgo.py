import numpy as np
import math
import random
'''
    The Fitness Function Defines The Fitness of the indiviual in the Group. The Group's Leader ie Rooster is the most Fittest in The Group to Which it Accounts as the Reason
'''

# Defining the Total Noumber of Features in the Dataset
Dn = int(input('Please Enter the Number Of Dataset Feature To Which You want To Apply Algorithm : '))

def fitness_function (x):

    '''
        The Function Takes in an Chromosome and performs The Test Under a Selected Value of
         'w': Constant Controlling The Importance Of Classification
         'E': Classification Error
         'x': Vector
         'N': Total Number of Features In The Dataset To Which We Want To Apply The Algorithm
    '''

    print("The Random Set is as Follows : ", x[0])

    w = 0.00000001
    E = 0.00000002
    N = Dn # For an Example

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

    '''
        Group of Functions which need to update the position of Chickens.
        Note : The Position will be first stored in a different property ie next_position_to_which_chicken_will_move will store the next address . Moving on the lane , The Fitness Count Obtained from new Generation will help in Updating the solution
    '''

    '''
        All the Functions will take in a parameter as The Number of Groups the Population is Divied into , For Example , If the Total Population is 10 , The best suited Group will be 10/5 , ie 2. All the Roosters will be then updated to the count of the following Appropriate Distribution
    '''

    def update_location_rooster(self, number_of_groups_the_swarm_is_divided, rooster): # Integer , Class Rooster
        random_number_between_the_total_number_of_groups = np.random.randint(0, number_of_groups_the_swarm_is_divided) # Example as Like if the Population is divided into 2 Groups , and then Total Option is Limited to either 0 or 1 , 0 for the First Group and 1 For Other Group

        while (rooster[random_number_between_the_total_number_of_groups].group == self.group):
            ## Checking If It doesnt' Belong to the same Group
            random_number_between_the_total_number_of_groups = np.random.randint(0, number_of_groups_the_swarm_is_divided)

        ### Evaluating The Equation According to The Algorithm

        ## Initalizing Sigma
        sigma_square = 0
        e = 0.000000000000000000000000000000000001
        if rooster[random_number_between_the_total_number_of_groups].group != self.group :
            if rooster[random_number_between_the_total_number_of_groups].fitness >= self.fitness:
                sigma_square = 1
            else :
                sigma_square = np.exp((rooster[random_number_between_the_total_number_of_groups].fitness - self.fitness)/ (np.abs(self.fitness) + e ))

        # Create Gaussian Distribution  with Mean 0 and Standard Deviation is sigma_sqare
        random_distribution = np.random.normal(0, sigma_square)

        '''
            We are Only Updating The Next Position , And Not the Original Position , Because the Update is Valid only when The Original Fitness is found lowered to The Mutated Fitness
        '''

        for index in range (0, Dn):
            self.next_position_to_which_chicken_will_move[index] = self.original_position[index]*(1+random_distribution)


    def update_location_hen(self, number_of_groups_the_swarm_is_divided, rooster): # Integer , Class Rooster
        '''
            The Rooster being Passed as a Parameter is to locate the Group to which the particular Rooster Belongs To , Including The Various Other Position Avaiable
        '''

        for index in range (0, number_of_groups_the_swarm_is_divided):
            # Running a For Loop , Since THe The Number of Groups are meant to be less than the original Population Created
            # Check if the Rooster of that Group Matches , Our Hens Group or Not
            # Since According to Segragation of The Population in Group , It is meant that eqaul Population will be shared
            if rooster[index].group == self.group :
                position_rooster_1 = rooster[index].original_position # Same Group Rooster Position
                fitness_rooster_1 = rooster[index].fitness # Same Group Rooster Health

        # Generating A Random Number in range of Groups
        random_number_between_the_total_number_of_groups = np.random.randint(0, number_of_groups_the_swarm_is_divided) # Example as Like if the Population is divided into 2 Groups , and then Total Option is Limited to either 0 or 1 , 0 for the First Group and 1 For Other Group

        while (rooster[random_number_between_the_total_number_of_groups].group == self.group):
            random_number_between_the_total_number_of_groups = np.random.randint(0, number_of_groups_the_swarm_is_divided) ## More not Getting the same Rooster Group

        if rooster[random_number_between_the_total_number_of_groups].group != self.group :
            position_rooster_2 = rooster[random_number_between_the_total_number_of_groups].original_position # Some  K Rooster Index
            fitness_rooster_2 = rooster[random_number_between_the_total_number_of_groups].fitness # Some K Rooster's Fitness

        fitness_current_hen = self.fitness #Fitness of Current Hen
        position_current_hen = self.original_position # Position of Current Hen
        e = 0.000000000000000000000000000000000001 # Defining the Smallest Constant

        # Defining S1 and S2 For The Parameters Listed
        S1 = np.exp( (fitness_current_hen - fitness_rooster_1)/ (np.abs(fitness_current_hen) + e))
        S2 = np.exp( (fitness_rooster_2 - fitness_current_hen))

        # Defining a Uniform Random Number Between 0 and 1
        uniform_random_number_between_0_and_1 = np.random.rand()

        # Note , Changing the next position and not the original position for Comparing different fitness
        for index in range (0, Dn):
            self.next_position_to_which_chicken_will_move[index] = ( position_current_hen[index] + S1*uniform_random_number_between_0_and_1*( position_rooster_1[index] - position_current_hen[index] ) + S2*uniform_random_number_between_0_and_1*( position_rooster_2[index] - position_current_hen[index] ))


    def update_location_chick(self, FL, position_of_mother_hen):# A Floating Point Value Between 0 and 2 , Array Containing the Position of the Mother Hen
        '''
            According to the Algo, The Baby Chick , Moves Around the Mother Chicken By The Expression
        '''
        #Getting The Current Chick Position
        position_current_chick = self.original_position

        for index in range (0, Dn):
            self.next_position_to_which_chicken_will_move[index] = (position_current_chick[index] + FL*( position_of_mother_hen[index] - position_current_chick[index] ) )


'''
    The Main Class is ImplementingChickenSwarmOptimization . The Class Initialzes a List of Chicken Classes , Whereby a Group of Randomly Generated Binary String is Obtained . Each Generated Chicken Class is Sorted According to its Fitness . Since , The Population is Invariable, We need to form a Group in which equal amount of Members are Generated , Failing of which the Features Selection may get as The Fitness of the Roosters will be more Biased to a Particular Group .
'''


'''
    The Class Takes 3 Arguments for the constructor , ie , The Population, Maximum Generation and Index to which Every Update Needs to Take Place to Establish A New Group .The Later Steps Involve Initalizing The Data and Make Segragation for Rooster, Hen And Chicken based on the Group .

'''

'''
    To Update The Binary Value and Checking its Crossover , We Will define a function as to one which yields certain range of value between 0 and 1 and then we need to compare It with Random value interepreted to change the Values .
'''

def function_returning_values_between_0_and_1 (x): #float
    return 1 / ( 1 + math.exp(-x))


class ImplementingChickenSwarmOptimization :

    ### Constructor

    def __init__(self, population, maximum_generation, self_update_time, FL = 0.5 ):# int , int , int , float

        # Initializing the total number of Groups for the Population , Appropriate Will be Population in Multiple of 10's and Dividing It in Multiple of 5
        number_of_groups_the_swarm_is_divided = int (population/5)
        print("\nThe Number Of Group The Swarm Is Divided : ", number_of_groups_the_swarm_is_divided)

        population_list = [] # List Storing the Object of Chicken .

        for index in range (population):
            population_list.append(Chicken())
            population_list[index].evaluate()

        iteration_test_cases = 0

        while (iteration_test_cases < maximum_generation):

            # Updation After Every Certain Time
            if (iteration_test_cases%self_update_time == 0):
                population_list.sort(key = lambda x : x.fitness , reverse = True)

                # Assigning The Members Equally in a Group
                rooster_class = population_list[:number_of_groups_the_swarm_is_divided] # Assigning Equal Number of Roosters to Each Group
                chicks_class = population_list[-(2*number_of_groups_the_swarm_is_divided)] # Assigning the Last Remaining Classes as Chick
                hens_class = population_list[-(population - number_of_groups_the_swarm_is_divided) : -(2*number_of_groups_the_swarm_is_divided)]

                ### Group === Knowing Which Chicken Belongs to Which Group . Can Either be Done Through Going through each class and getting Group Number it Belongs to.

                group_list_containing_which_group_belongs = np.zeros(population)

                for index in range (number_of_groups_the_swarm_is_divided):
                      population_list[index].species_name = "Rooster" # Example of 10, First  2 being Roosters
                      population_list[-1-index].species_name = "Chick" # Example of 10 , index 9,8 being Chicks
                      population_list[-3-index].species_name = "Chick" # Example of 10 , index 7,6 being Chicks

                # Assigning Hens in the Group
                for index in range (number_of_groups_the_swarm_is_divided, (population - 2*number_of_groups_the_swarm_is_divided)):
                    population_list[index].species_name = "Hen" # Example of 10 , index of 2,3,4,5 being Hens

                '''
                    Based on the Total Population , The Population is divided into Group of 5 lets suppose. Now To each Group , We will have 1 Head Rooster , 2 Hens and 2 Chicks . Now , The Algorithm Validates to the  Position being Updated for each Row and The Validation successfully yields the nature Criteria for Identifying Weak as well as Strong . Thereby Performing Swarm Optimization
                '''

                # In Example of 10 , With 2 Groups [ 0. , 0.  ]
                roosters_in_each_group_counter = np.zeros(number_of_groups_the_swarm_is_divided)
                hens_in_each_group_counter = np.zeros(number_of_groups_the_swarm_is_divided)
                chicks_in_each_group_counter = np.zeros(number_of_groups_the_swarm_is_divided)


                '''
                    To Assign Roosters and Hens And Chickens , We will Try to Randomize as much as Possible , failing of which will indicate the Gain of a particular group every Time , Thereby Hampering Our Solution.
                '''

                # Assigning Roosters in the Group

                for index in range(number_of_groups_the_swarm_is_divided): # For Example of 10 , The index 0 and 1, Since we have only 2 groups present
                    random_integer_between_the_total_number_of_groups_we_can_have_minus_1 = np.random.randint(0, number_of_groups_the_swarm_is_divided)

                    # Keeping Track that There is only One Rooster Avaiable in the Swarm
                    while roosters_in_each_group_counter[random_integer_between_the_total_number_of_groups_we_can_have_minus_1] >= 1:
                        random_integer_between_the_total_number_of_groups_we_can_have_minus_1 = np.random.randint(0, number_of_groups_the_swarm_is_divided)

                    ## Putting it in an If statement , to Not Get any Undefined Declaration
                    if roosters_in_each_group_counter[random_integer_between_the_total_number_of_groups_we_can_have_minus_1] < 1 :
                        population_list[index].group = random_integer_between_the_total_number_of_groups_we_can_have_minus_1 + 1 #Going into The Index of Object , Then Accessing Group and Updating It
                        roosters_in_each_group_counter[random_integer_between_the_total_number_of_groups_we_can_have_minus_1] += 1 #Updating the Value at each Index ie in [0 , 0], if the random number is 1 then It will be [1, 0] for rooster count
                        group_list_containing_which_group_belongs[index] = random_integer_between_the_total_number_of_groups_we_can_have_minus_1+1 #Updating The Group List to avoid Getting into each Object Properties to get the Group Number

                ### Assigning The Hens and Relationship of Mother Hen with Chicks
                '''
                    For Establishing a Relationship for Hen And Mother , We would keep track of the index of the Mother hen . Since we need to randomize the solution to predict an Optimized Result , Therefore we would Store it in an array to which the index belongs to .
                '''

                for index in range(number_of_groups_the_swarm_is_divided, 3*number_of_groups_the_swarm_is_divided): #2, 3, 4, 5 in case of Example 10
                    # For Assigining Each Group That We can Assign the Hen .
                    random_integer_between_the_total_number_of_groups_we_can_have_minus_1 = np.random.randint(0, number_of_groups_the_swarm_is_divided)

                    # Checking If the Not More than 2 Hens Exist In the same Group , In Our Case [ 0, 3] is not Possible
                    while hens_in_each_group_counter[random_integer_between_the_total_number_of_groups_we_can_have_minus_1] >= 2:
                        random_integer_between_the_total_number_of_groups_we_can_have_minus_1= np.random.randint(0, number_of_groups_the_swarm_is_divided)


                    if hens_in_each_group_counter[random_integer_between_the_total_number_of_groups_we_can_have_minus_1] < 2 :
                        population_list[index].group = random_integer_between_the_total_number_of_groups_we_can_have_minus_1 + 1 # Going into Index , then Updating the Property Group so That In case for our Example 0 and 1 become Group 1 and Group 2
                        group_list_containing_which_group_belongs[index] = random_integer_between_the_total_number_of_groups_we_can_have_minus_1+1 # Updating the same in group list to make it easy for iterating in the later step
                        hens_in_each_group_counter[random_integer_between_the_total_number_of_groups_we_can_have_minus_1] += 1 # Upating [0,0] to [1, 0]

                    '''
                        The Next Process involves Mapping Mother Hen to Chicks in the Population , Therefore we Need to Randomize An Integer between 6, 7, 8, 9 , So that Mapping Occurs for Chicks and Not For Hens in the List

                        6 = 3*(number_of_groups_the_swarm_is_divided)
                        10 = 5*(number_of_groups_the_swarm_is_divided)
                    '''

                    random_integer_for_mapping_chicks = np.random.randint(3*number_of_groups_the_swarm_is_divided,5*number_of_groups_the_swarm_is_divided)

                    # Checking If the Chick is not already Mapped
                    while (group_list_containing_which_group_belongs[random_integer_for_mapping_chicks] != 0) :
                        random_integer_for_mapping_chicks=np.random.randint(3*number_of_groups_the_swarm_is_divided,5*number_of_groups_the_swarm_is_divided)

                    while chicks_in_each_group_counter[random_integer_between_the_total_number_of_groups_we_can_have_minus_1] >= 2:
                        random_integer_between_the_total_number_of_groups_we_can_have_minus_1= np.random.randint(0, number_of_groups_the_swarm_is_divided)

                    # Error Zone :- Starts
                    if chicks_in_each_group_counter[random_integer_between_the_total_number_of_groups_we_can_have_minus_1] < 2 :
                        chicks_in_each_group_counter[random_integer_between_the_total_number_of_groups_we_can_have_minus_1] += 1
                        group_list_containing_which_group_belongs[random_integer_for_mapping_chicks] = index ## New Error Zone
                        population_list[random_integer_for_mapping_chicks].group = random_integer_between_the_total_number_of_groups_we_can_have_minus_1+1
                    # Error Zone : Ends

                for i in range (0, population):
                    print ("\nFitness is ", population_list[i].fitness)
                print ("The Roosters Count is : ", roosters_in_each_group_counter, "The Hen Count is : ", hens_in_each_group_counter, "The Chick Count is ", chicks_in_each_group_counter)
                print ("The Group List Looks like ", group_list_containing_which_group_belongs)





            #### It Starts Here!!!!#####
            '''
                Once All The Roosters, Chickens and Hens are Initalized , We need to Update The Location for Every Fall Iteration Allowed in the Loop
            '''

            for index in range (0, population):

                if (population_list[index].species_name == "Rooster"):
                    print("\nThe Chicken is a Rooster at index ", index)
                    population_list[index].update_location_rooster(number_of_groups_the_swarm_is_divided, rooster_class)
                elif (population_list[index].species_name == "Hen"):
                    print("\nThe Chicken is a Hen at index ", index)
                    population_list[index].update_location_hen(number_of_groups_the_swarm_is_divided, rooster_class)
                elif (population_list[index].species_name == "Chick"):
                    print("\nThe Chicken is a Chick at index ", index)
                    mother_hen_index = int(group_list_containing_which_group_belongs[index])
                    position_of_mother_hen = population_list[mother_hen_index].original_position

                    population_list[index].update_location_chick(FL, position_of_mother_hen)


                '''
                Now Updation of the Value based on the fitness is needed as of now , Thereis No Particular Option to Change the All the feature Index , So We will have to Evaluate it Using a function and needs to compare it for fitness
                '''

                for iteration_to_features in range (0, Dn):
                    if (function_returning_values_between_0_and_1(population_list[index].next_position_to_which_chicken_will_move[iteration_to_features]) > np.random.random()):
                        population_list[index].sample_chicken_comparing_stack[0][iteration_to_features] = 1
                    else :
                        population_list[index].sample_chicken_comparing_stack[0][iteration_to_features] = 0

                if fitness_function(population_list[index].sample_chicken_comparing_stack) > population_list[index].fitness:
                    print("\n\nA Better Fitness Function is Found !!")
                    print ("\nThe Original Fitness Value for the ", population_list[index].fitness, " for the Solution as ", population_list[index].original_chicken_string)
                    population_list[index].evaluate()
                    print ("\nThe Fittest One is as Follows ", population_list[index].original_chicken_string)
                    ## Sorting For Finding If It Can Be the Best
                    population_list.sort(key = lambda x : x.fitness , reverse = True)


            iteration_test_cases += 1


input_population = int(input('Enter The Total Population in Multiple of 5 or 10 or 15 !'))
input_maximum_generation = int(input('Enter The Maximum Generation For The Population '))
input_time_updation = int(input('Enter The Time For Updation Of Population '))
input_a_value_between_for_mother_hen_and_chick_relationship = float(input('Enter A Close FL Value for Mother Hen and Chick Relationship '))
ImplementingChickenSwarmOptimization(input_population, input_maximum_generation, input_time_updation, input_a_value_between_for_mother_hen_and_chick_relationship) # int, int , int , float
