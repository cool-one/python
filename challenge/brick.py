  
"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and 
big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.
"""
def make_bricks(small, big, goal):
    # The bare minimum of small bricks for any condition to be eligible to pass.
    # If this case fails, goal requirement cannot be met.
    if(small < goal%5):
        return False
    # This case tests if the combination of bricks will meet the goal.
    # Does not cover condition of (big*5 > goal), but previous case overlaps and creates a complete assessment.
    if(goal - (big*5) > small):
        return False
    else:
        return True
