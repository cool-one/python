"""
************************************************************************************************************
FILE:       n_factorial.py
UPDATED:    11-22-19
AUTHOR:     RC
TOPIC:      Calculate n! w/ Input Restriction & User Controls - Discrete Math
USAGE:      $ python3 n_factorial.py            
************************************************************************************************************
"""

def get_int(lo, hi):
    """
    Acquire positive integer from user, return the int.
      Input:
        lo - lowest acceptable int value
        hi - highest acceptable int value
      Output: 
        Returns int within range of lo & hi
    """
    while True:
        n = input(f"Please enter an integer from {lo} to {hi}: ")
        try:
            n = int(n)          
        except ValueError:      
            print("It must be an integer!") 
            continue
        if n < lo:               
            print("You can't use negative numbers...")
            continue            # needed, otherwise enters the else statement.
        if n > hi:              
            print("Think smaller")
        else:
            break               # exit to return if meets conditions.
    return n

def n_factorial(n):
    """
    Calculates n! recursively
      Input:  
        n - integer value to find factorial of.
      Output:
        Returns factorial value as an integer
    """
    # BASE CASE
    if n in (0, 1):
        return 1
    answer = n_factorial(n-1)*n
    return answer

def control(message, the_function):
    """
    Control loop. Prompts user with message, calls function on Y, exits on N.
      Inputs:
        message         - String to ask user if they want to perform action, Y or N.
        the_function    - A task function to call if Y.
      Action:
        Calls function on Y, exits on N.
    """
    while True:
        user_choice = input(message)
        if user_choice in ('Y', 'y'):
            the_function()
        elif user_choice in ('N', 'n'):
            print("exiting program.....")
            print("Have a nice day!")
            break
        else:
            print("Not a valid option, try again")

def task_factorial():
    """
    Calls functions to obtain int from user, find its factorial.  Prints value.
    """
    # set range of factorials here
    lo, hi = 0, 11
    user_digit = get_int(lo, hi)                       
    solution = n_factorial(user_digit)           
    print("The factorial of %d is %d" % (user_digit, solution))    

def main():
    message = "Do you want to find a factorial? Y / N: "
    control(message, task_factorial)      

if __name__== "__main__":
    main()

