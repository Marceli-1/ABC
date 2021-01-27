import matplotlib.pyplot as plt
import random
import math
import numpy as np
import csv

lower_limit = -50 # lower limit of function
upper_limit = 50 # upper limit of function
swarm_size = 100 #
n_generations = 100 # number of generation to learn
trial_limit = 100


# Calculate f(x, y)
# This function you can edit
def given_function(x, y):
    return -1*math.floor(x*y)+x*x+y*y
# ___________________________________________

def generate_food_source_list(swarm_size):
    food_source_x_y_list = np.zeros(shape=(swarm_size, 2))
    for i in range(0, swarm_size):
        a = random.uniform(-50,50)
        b = random.uniform(-50,50)
        food_source_x_y_list[i][0] = a
        food_source_x_y_list[i][1] = b
    return food_source_x_y_list

# For array implementation
def calculate_maximize_list(x_y_list):
    maximize_list = []
    for i in range(0, swarm_size):
        maximize_list.append(given_function(x_y_list[i][0], x_y_list[i][1]))
    return maximize_list

# For single value
def calculate_maximize_listt(x, y):
    return given_function(x,y)

#Calculate minimum
def fitness(maximi):
    max_res = []
    for i in range(0, swarm_size):
        if maximi[i] >= 0:
            max_res.append(1/(1+maximi[i]))
        if maximi[i] <= 0:
            max_res.append(1+abs(maximi[i]))
    return max_res

#For single value
def fitnesss(maximi):
    if maximi >= 0:
        return (1 / (1 + maximi))
    if maximi <= 0:
        return (1 + abs(maximi))

#Initialization of first generation
source_x_y_list = generate_food_source_list(swarm_size) #generate food source list with random x, y
maximiz = calculate_maximize_list(source_x_y_list) #calculate f(x,y)
minim = fitness(maximiz)
trial = [0] * (swarm_size)



def print_table():
    print('{0: ^30}{1: ^30}{2: ^30}{3: ^30}{4: ^30}{5: ^30}'.format("Id", "X", "Y", "Maximize (Cost)", "Minimize (Fit)","trial"))
    for i in range(0, len(source_x_y_list)):
        #print (i, "\t\t", source_x_y_list[i][0], "\t\t", source_x_y_list[i][1], "\t\t", maximiz[i], "\t\t", minim[i], "\t\t", trial[i])
        print('{0: ^30}{1: ^30}{2: ^30}{3: ^30}{4: ^30}{5: ^30}'.format(i, source_x_y_list[i][0], source_x_y_list[i][1],
                                                                maximiz[i], minim[i], trial[i]))

#Learning algorithm
def employ(source_x_y_listt, maximizz, minimm):
    for i in range(0, swarm_size): #
        x_or_y = random.randint(0,1) #choose x or y from employed bee and partner

        partner_id = random.randint(0, swarm_size-1) #generate id of random partner
        while partner_id == i:
            partner_id = random.randint(0, swarm_size-1)

        #create new food location:
        employee = source_x_y_listt[i][x_or_y] #
        employee_partner = source_x_y_listt[partner_id][x_or_y]

        x_or_y_new = employee + random.uniform(-1, 1)*(employee - employee_partner) #

        x_or_y_new_max = 0


        if x_or_y == 0:
            x_or_y_new_max = calculate_maximize_listt(x_or_y_new, source_x_y_listt[i][1])

        elif x_or_y == 1:
            x_or_y_new_max = calculate_maximize_listt(source_x_y_listt[i][0], x_or_y_new)

        else:
            print("else: error")


        x_or_y_new_fit = fitnesss(x_or_y_new_max)


        if minimm[i] < x_or_y_new_fit:
            source_x_y_listt[i][x_or_y] = x_or_y_new
            minimm[i] = x_or_y_new_fit
            maximizz[i] = x_or_y_new_max
            trial[i] = 0
        elif minimm[i] > x_or_y_new_fit:
            trial[i] += 1

        if trial[i] > trial_limit:
            source_x_y_listt[i][0] = random.uniform(-50,50)
            source_x_y_listt[i][1] = random.uniform(-50, 50)
            maximizz[i] = calculate_maximize_listt(source_x_y_listt[i][0], source_x_y_listt[i][1])
            minimm[i] = fitnesss(maximizz[i])
            trial[i] = 0

#Looks for ID with the lowest cost
def find_lowest_cost(maximizz):
    cost = 2147483647
    j = 0
    index = 0
    for i in maximizz:
        if i < cost:
            cost = i
            index = j
        j+=1
    return index


def next_generation(n ,source_x_y_listt,maximizz,minimm, verbose = True):
    nn = n
    for _ in range(0, n): # number of generation
        employ(source_x_y_listt,maximizz,minimm) #employ new bee
        i = find_lowest_cost(maximizz)
        #print(i)
        if verbose is True:
            #print(i, "\t\t", source_x_y_list[i][0], "\t\t", source_x_y_list[i][1], "\t\t", maximiz[i], "\t\t", minim[i],
            #      "\t\t", trial[i])
            print('{0: ^30}{1: ^30}{2: ^30}{3: ^30}{4: ^30}{5: ^30}'.format(i, source_x_y_list[i][0], source_x_y_list[i][1],
                                                                    maximiz[i], minim[i], trial[i]))
            file = open('data_cost.csv', 'a+', newline='')

            # writing the data into the file
            with file:
                write = csv.writer(file)
                write.writerow(['{:.16f}'.format(maximiz[i])])





''''''
print("Starting data:")
print("______________________________________________________________________________________________________________")
print_table() # Array with starting values


print("Outprint best :")
print("______________________________________________________________________________________________________________")
print('{0: ^30}{1: ^30}{2: ^30}{3: ^30}{4: ^30}{5: ^30}'.format("Id", "X", "Y", "Maximize (Cost)", "Minimize (Fit)","trial"))
next_generation(n_generations, source_x_y_list,maximiz,minim, True)
print("______________________________________________________________________________________________________________")


''''''
print("Finish data:")
print("______________________________________________________________________________________________________________")
print_table() # Tablica z danymi koncowa

