# Lab6
# Author: Frank R. Leotta

import pytest

""" TO DO PYTEST, 4 steps *** Type into terminal
1.)Save virtual environment to folder if you havent already
#python3 -m venv venv
"""
#2.)
# ACTIVATE VIRTUAL ENVIRONMENT
#venv\Scripts\activate


"""3.) In terminal enter this:

#pip install pytest


"""
#  step 4
# in vs coder, import pytest



###OK YORU DONE WITH PYTEST, follow tips below to use it

#-K DOES A FUZZY SEARCH FOR THE WORLD

# pytest <whatever the python file name is> - k  rectangle -v
# that will run all the tests that have "rectangle" in the name

# if ERROR: file or directory not found: test.py
# then you need to run the test.py file first


## add in functions from test.py's test statements here to make the pytest work
###Funtion 1

def calculate_rectangle_area(length: float, width:float) -> float:
    """
    Calculates the area of a rectangle given its length and width.

    Arguments:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return float(length) * float(width)



    
#function 2    
def calculate_hypotenuse(side_a: float, side_b:float) -> float:
    """
    Calculates the hypotenuse of a right triangle given the lengths of the other two sides.
    
    Arguments:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    Parameters:
    A (float): The length of side A.
    B (float): The length of side B.
    
    multiplying by exponent 0.5 is the same as square root

    """

    side_a = float(side_a)
    side_b = float(side_b)

    # or this way
    # sides = float(side_a) ** 2 + float(side_b) ** 2
    # import math
    # return math.sqrt(sides)

    return (float(side_a) ** 2 + float(side_b) ** 2) ** 0.5


#function 2.5
def calculate_rectangle_area(length: float, width:float) -> float:
    """
    Calculates the area of a rectangle given its length and width.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return float(length) * float(width)


#function 3
def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False


#function 4
def find_maximum(x: float, y:float) -> float:
    """ summery
    finding the maximum of two numbers.  The bigger number is returned.

    arguments:
    x (float): first number
    y (float): second number

"""
    x = float(x)
    y = float(y)
    if x > y:
        return x
    else:
        return y


#function 5
def grade_calculator(x: int)-> str:
    """"Summery
    calculats a letter grade
    
        
    """
    if x >= 90 and x <= 100:
        return "A"
    elif x >= 80 and x < 90:
        return "B"
    elif x >= 70 and x < 80:
        return "C"
    elif x >= 60 and x < 70:
        return "D"
    elif x <= 59 and x >= 0:
        return "F"
    else:
        return "Invalid Score"

def main():
    pass


if __name__ == "__main__":
    main()

# NOTES FROM COPILOT
#-Q IS QUIET
#-R IS REPORTING
#-S IS CAPTURES THE STANDARD OUT
#-W IS WARNING
#-H IS HELP
#-M IS MARKING
#-N IS DRY RUN
#-P IS PROFILE
#-T IS TIME OUT
#-A IS ADDOPTS
#-B IS PYTHONPATH
#-C IS CHDIR
#-D IS DOCTEST
#-E IS ENVIRONMENT
#-F IS FAILED FIRST
#-G IS GENERATE REPORT
#-I IS INSTANT QUALITY
#-J IS JUNIT XML
#-L IS LAST FAILED
#-O IS DOCTEST REPORT
#-U IS UNORDERED
#-Y IS ASSERTION
#-Z IS EXIT FIRST
#-1 IS EXIT FIRST
#-2 IS EXIT FIRST
#ECT