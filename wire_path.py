#!/usr/bin/python3
"""
************************************************************************************************************
FILE:       wire_path.py
UPDATED:    11-22-19
AUTHOR:     RC
TOPIC:      Optimization Problem - Calculus
SUMMARY:    Calculates the minimum cost and best route for a crew needing to run a wire under a street to point B,
            which is located on the opposite side of the street and a distance down the street.  Takes user inputs
            to account for the different costs to run wire under the street vs. ground and also inputs for the 
            width and length of the street.
            *Requires SymPy symbolic mathematics library.
USAGE:      $ python3 wire_path.py            
************************************************************************************************************
"""
from sympy import *
x, y = symbols('x y')
init_printing(use_unicode=True)

def get_float(msg, lo, hi):
    """
    Function to take user input that falls in restricted range, casts to float.
        Input:
            msg - message displayed to user
            lo - lowest acceptable float value
            hi - highest acceptable float value
        Output:
            Returns a float value within restricted range.
    """
    while True:
        n = input(msg)         
        try:
            n = float(n)        
        except ValueError:      #CATCH wrong type
            print("It must be an number!")  
            continue
        if n < lo:               
            print("You can't use negative numbers...")
            continue            #needed, otherwise enters the else statement.
        if n > hi:              
            print("Think smaller")
        else:
            break               #exit to return if meets conditions.
    return n
#==============================================================================

# set range of input values
lo, hi = 0, 1000
street_cost = get_float('Enter the cost per meter under the street: ', lo, hi)
ground_cost = get_float('Enter the cost per meter under the ground: ', lo, hi)
street_width = get_float('Enter the width the street: ',lo, hi)
street_length = get_float('Enter the length of the street: ', lo, hi)

# Cost symbolic equation.  x: width of the diagonal path, street_width: street width, street_length: street length.
c = street_cost*(x**2 + street_width**2)**0.5 + ground_cost*(street_length - x)

# Find 1st derviative of equation c.
c_prime = diff(c)

# Solve for x with 1st derivative set equal to 0 to find a possible critical point/minimum.
x_min = solve(c_prime, x)

# declare variable to store possible critical point value of x.  Seeking a minimum.
x_critical = 0
if x_min:
    # Check if solve() returned an imaginary number from an input of street_cost < ground_cost.
    if x_min[0].is_real:
        x_critical = x_min[0]

# Set current optimum horizontal length from start point.
length = x_critical

def cost(x_diag, street_cost, ground_cost, street_width, street_length):
    """
    Cost numerical input function.  Returns the cost.
        Inputs:
            x_diag - Width of the diagonal path measured by x-axis.
            street_cost 
            ground_cost
            street_width
            street_length
        Output:
            Returns the total cost.
    """
    total = street_cost*(x_diag**2 + street_width**2)**0.5 + ground_cost*(street_length - x_diag)
    return total
#==============================================================================

# Find cost using x_critical value.
critical_cost = cost(x_critical, street_cost, ground_cost, street_width, street_length)

# Set current min cost.
min_cost = critical_cost

# check cost of endpoints at x=0 & x=street_length for a min
cost_left_end = cost(0, street_cost, ground_cost, street_width, street_length)
cost_right_end = cost(street_length, street_cost, ground_cost, street_width, street_length)

# Address critical points that are out of bounds.  Find the min_cost from C.P. and endpoints. 
if (length > street_length or cost_left_end < min_cost):
    length = 0
    min_cost = cost_left_end

if (cost_right_end < min_cost):
    length = street_length
    min_cost = cost_right_end

min_cost = round(min_cost, 2)
length = round(length, 2)

print(f'Minimum project cost: ${min_cost}')
print(f'Run wire directly to a point across the street {street_length-length} meters to the left of pt. B')
