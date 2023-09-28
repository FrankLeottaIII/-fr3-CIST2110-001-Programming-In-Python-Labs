# Lab3
# Author: Frank R. Leotta III

"""_summary_
This lab is designed to get you familiar with Python Boolean Expressions, Conditional Expressions, if-elif-else statements, and while / for loops.
"""

# 1. Write some code that asks the user for a number and prints out whether it is positive, negative, or zero.
number = (float(input("Hello, please enter a whole number: ")))
if number > 0:
        print("That number is positive")   
elif number < 0:
        print("That number is negative")
else:   
        print("That number is zero")
# 2. Write some code that asks the user for a number and prints out whether it is even or odd.
number_two = float(input("Hello, please enter another whole number \n (note: the number will be rounded to the nearest integer regardless): "))
number_two_rounded = round(number_two, 0)
if number_two_rounded %  2 == 0:
        print("That number is even when rounded to the nearest number")   
else:   
        print("That number is oddwhen rounded to the nearest number")

## problem going forward :it regesters it as odd if its a decimal number so it needs to be rounded to
#    a whole number.... or an absolute vaue of the decimal number
#       Fill out later,  feel like doing something else right now
# 3. Write some code that asks the user for a number and prints out all the numbers from 1 to that number using a while loop.
number_three = (float(input("Hello, please enter a positive whole number \n (note: I recommend one between 1 and 50): ")))
start_number = 1
while start_number <= number_three:
        print(start_number)
        start_number += 1
print("done")
# 4. Use a for loop to ask a user for 5 numbers and print out the average of those 5 numbers.
number_four = 0 
for i in range(5):
        number_four += float(input("ok then, please enter a number, I will average it for you after I obtain 5 numbers: "))
print(number_four/5)    
## For X in range(), good for average questions or summery questions that have a defined amount of varibles.
# 5. Write some code that prints out all the numbers from 1 to 10 that are divisible by 3 or 5.
print("fun fact: the following numbers are not divisible by 3 or 5")
for i in range(1, 11):
        if i % 3 == 0:  
                continue
        if i % 5 == 0:
                continue
        print(i)
# the % is pretty convienent for division problems..... I need to memorize this lesson more.
# 6. Write some code that asks the user for a number and then prints out a countdown from that number to 1 using a while loop. After the countdown, print "Blast off!".
number_five = (float(input("Hello, please enter a positive whole number \n (note: I recommend one between 1 and 50): ")))
while number_five > 0:
        print(number_five)
        number_five -= 1
print("Blast off!")
# 7. Write some code that asks the user for a number and then uses a for loop to iterate from 1 to that number. If the current number is divisible by 7, print "Lucky" and continue to the next iteration. If the current number is greater than 100, break the loop.



## notes for later (copy out of lab homework elsewhere)
# Finding if something is even or odd
#print("% is the remainder of a division problem"")
#print("== is a comparison operator")
#    if number_two % 2 == 0:
#        print("That number is even")   
#   else:   
#       print("That number is odd")