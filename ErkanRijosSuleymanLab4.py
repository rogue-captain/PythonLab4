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

# 
#
# Inputs: 
#
# Outputs:
#
##############################################################################


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
    
###############################################################################

#B

    