# Lab6
# Author: Frank R. Leotta


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
def find_maximum():
    x = float(x)
    y = float(y)
    if x > y:
        return x
    else:
        return y


#function 5
def grade_calculator(x: int)-> str:
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    elif x >= 50:
        return "F"
    else:
        return "Invalid Score"













def main():
    pass


if __name__ == "__main__":
    main()
