# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:18:03 2024

@author: Sully
"""


##############################################################################
# Name: Suleyman Erkan-Rijos | CST-121 | Y01

# Program: Lab 4

# Due Date: 10/08/2024
#
# Program Description: 
    
#A
#This program is made of 2 sub routines. Sub A will ask 
#user for input and make a multiplaction table based on selected integer.

#B
#This sub program will ask user to select an integer from a menu, 1- 6. 
#The system will randomly generate an array of 10 numbers for the program to
#use in its calculations. 
#Based off of the user selction, The system will perform the calculationa and
#ask user for another input until sentinal is used to terminate program. 

# 
#
# Inputs: A: 1 integer variable
#         B: input loop for numbers 1- 6 until sentinal is used.
#
# Outputs: A: a multiplication table based on the user input.
#          B: 1 of 6 possible calculations will be produced based off of a list
#             of 10 random numbers.
##############################################################################

import statistics

import random

################################ VARIABLES ####################################


################################ VARIABLES ####################################

#A
#collect an integer value entered in by the user.
userInput = int(input("please enter a number of which you wish to see a 10 x multiplication table: "))

print(f"\nMultiplication Table for {userInput}") #table header

print(f"\n{'Multiplier':>12} \t {'Result':>10}") #Column Headers

print() #spacer

for row in range(1,11):

    result = userInput * row
    print(f"{row:>12} {result:>14}")
    
    
print() #spacer
    
###############################################################################

#B

def randomTenNumSelector():
    
    randomNumList = []
    
    for n in range(10):
        randomNum = random.randint(1, 100)
        randomNumList.append(randomNum)
    return randomNumList


# Function to calculate range
def calculate_range(lst):
    return max(lst) - min(lst)



# Function to display the menu
def display_menu():
    print("######################################################")
    print() #spacer
    print("Choose from the MENU to perform a given task")
    print("1- Calculate the mean value for the List")
    print("2- Calculate the median value for the List")
    print("3- Calculate the mode value for the List")
    print("4- Calculate the Range value for the List")
    print("5- Sort the values in ascending order in the List")
    print("6- Calculate the standard deviation for the List")
    print("-1 To EXIT")
    print() #spacer
    print("######################################################")
  
###############################################################################

print() #spacer
    
randomNumList = randomTenNumSelector()  # Generate the list of random numbers

print("Here is the list of random numbers we will use: " ,randomNumList) #debugging line

print() #spacer
    
display_menu() #user sees menu



userSelect = 0 #initialize userSelect

#while loop to controlled with -1 sentinal
while userSelect != -1:
    
    #try / exept lines to act as check for correct input type
    try:
        userSelect = int(input("What is your selection? "))
        
    except ValueError:
        print("Please enter a valid integer.")
        print() #spacer
        continue     
          

    print("You have selected: " ,userSelect)

    print() #spacer
    
    # Perform the task based on user selection
    if userSelect == 1:
        mean_value = statistics.mean(randomNumList)
        print(f"Mean Value: {mean_value}")
            
    elif userSelect == 2:
        median_value = statistics.median(randomNumList)
        print(f"Median Value: {median_value}")
            
    elif userSelect == 3:
            
        mode_value = statistics.mode(randomNumList)
        print(f"Mode Value: {mode_value}")
            
    elif userSelect == 4:
        range_value = calculate_range(randomNumList)
        print(f"Range Value: {range_value}")
            
    elif userSelect == 5:
        sorted_list = sorted(randomNumList)
        print(f"List in Ascending Order: {sorted_list}")
            
    elif userSelect == 6:
        standardDeviation_value = statistics.stdev(randomNumList)
        print(f"Standard Deviation: {standardDeviation_value}")
            
    elif userSelect == -1:
        print("Exiting the program. Good-Bye Nerd!")
        break
            
    else:
        print("Invalid choice. Please choose from the menu.")
        display_menu()
        continue
    
