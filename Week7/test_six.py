## test.py



import pytest

""" TO DO PYTEST, 3 steps *** Type into terminal
1.)Save virtual environment to folder if you havent already
#python3 -m venv venv
"""
#2.)
# ACTIVATE VIRTUAL ENVIRONMENT
#venv\Scripts\activate


"""3.) In terminal enter this:
#pip install pytest


"""
###OK YORU DONE WITH PYTEST, follow tips below to use it

#-K DOES A FUZZY SEARCH FOR THE WORLD

# pytest <whatever the python file name is> - k  rectangle -v
# that will run all the tests that have "rectangle" in the name






"""
ERROR: file or directory not found: test_six.py

Found online
https://stackoverflow.com/questions/61490861/pytest-cannot-find-file-or-directory-when-running-test
For anyone stopping by and facing the same issues when using markers (e.g. pytest -m "not your-mark")

collects the items, deselects the items, and does nothing with it. So you have to explicitly tell it to run the tests with the markers you want.
I can do that by adding the -m flag to the pytest command:
pytest -m "not your-mark"

Yea, I need to figure this out later... it doesn't seem to be working for me
"""



###ok now for the actual work####

## add in functions from test.py's test statements here to make the pytest work

# Import the pytest library
#import pytest



# As you add functions to Lab6.py, import them here (uncomment the lines)
from Lab6 import calculate_rectangle_area, calculate_hypotenuse, is_even, find_maximum, grade_calculator

#or you do it individually next to it, but this is easier and cleaner
# from Lab6 import calculate_rectangle_area
# from Lab6 import calculate_hypotenuse
# from Lab6 import is_even
# from Lab6 import find_maximum
# from Lab6 import grade_calculator

# Example test cases

# Test cases for calculating the area of a rectangle
def test_rectangle_area():
    assert calculate_rectangle_area(3, 4) == 12
    assert calculate_rectangle_area(5, 5) == 25
    assert calculate_rectangle_area(0, 0) == 0
    assert calculate_rectangle_area(10, 20) == 200



# Test cases for the Pythagorean theorem
def test_pythagorean_theorem():
    assert calculate_hypotenuse(3, 4) == 5
    assert calculate_hypotenuse(5, 12) == 13
    assert calculate_hypotenuse(7, 24) == 25
    assert calculate_hypotenuse(8, 15) == 17

# Test cases for checking if a number is even
def test_is_even():
    assert is_even(2) is True, "Even calculation failed for 2"
    assert is_even(7) is False, "Even calculation failed for 7"
    assert is_even(0) is True, "Even calculation failed for 0"
    assert is_even(11) is False, "Even calculation failed for 11"

# Test cases for finding the maximum of two numbers
def test_find_maximum():
    assert find_maximum(3, 4) == 4, "Maximum calculation failed for 3 and 4"
    assert find_maximum(5, 12) == 12, "Maximum calculation failed for 5 and 12"
    assert find_maximum(7, 24) == 24, "Maximum calculation failed for 7 and 24"
    assert find_maximum(8, 15) == 15, "Maximum calculation failed for 8 and 15"

# Test cases for calculating a letter grade
def test_grade_calculator():
    assert grade_calculator(90) == "A", "Grade calculation failed for A"
    assert grade_calculator(80) == "B", "Grade calculation failed for B"
    assert grade_calculator(70) == "C", "Grade calculation failed for C"
    assert grade_calculator(60) == "D", "Grade calculation failed for D"
    assert grade_calculator(50) == "F", "Grade calculation failed for F"
    assert grade_calculator(105) == "Invalid Score", "Grade calculation failed for out-of-range score"
    assert grade_calculator(-5) == "Invalid Score", "Grade calculation failed for negative score"

# Run the tests when the script is executed
if __name__ == "__main__":
    pytest.main()
