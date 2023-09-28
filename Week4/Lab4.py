# Lab3
# Author: Frank R. Leotta III

"""_summary_
This lab is designed to get you familiar with Python Boolean Expressions, Conditional Expressions, if-elif-else statements, and while / for loops.
"""

# 1. Write some code that asks the user for a number and prints out whether it is positive, negative, or zero.
number = int(input("Hello, please enter a whole number: "))
if number > 0:
        print("That number is positive")   
elif number < 0:
        print("That number is negative")
else:   
        print("That number is zero")
# remember floats are not exact, cannot be used for determining this accuratly if someone puts a 0 in there... maybe?
# 2. Write some code that asks the user for a number and prints out whether it is even or odd.
number_two = float(input("Hello, please enter another number to be determined if it is even or odd.  It will be rounded to the nearest whole number:"))
number_two_rounded = round(number_two, 0)
print(str(number_two_rounded) + " is the number you entered rounded to the nearest whole number")
if number_two_rounded %  2 == 0:
        print("That number is even when rounded to the nearest integer")   
else:   
        print("That number is odd when rounded to the nearest integer")
# alternate way of doing it from class
#remainder = number_two_rounded % 2
i#f remainder == 0:
  #      print("That number is even when rounded to the nearest integer")

## problem going forward :it regesters it as odd if its a decimal number so it needs to be rounded to
#    a whole number.... or an absolute vaue of the decimal number

# 3. Write some code that asks the user for a number and prints out all the numbers from 1 to that number using a while loop.
number_three = input("Hello again, please enter a positive whole number, I will count from 1 to that number: ")
number_three = int(number_three)
start_number = 1
start_number = int(start_number)
while start_number <= number_three:
        print(start_number)
        start_number += 1
print("done")
## kept on getting a error message ValueError: could not convert string to float... so i made it a float in another command. how odd

# 4. Use a for loop to ask a user for 5 numbers and print out the average of those 5 numbers.
number_four = 0 
for i in range(5):
        number_four += float(input("ok then, please enter a number, I will average it for you after I obtain 5 numbers: "))
average = number_four/5
print(str(average) + " is the average of the 5 numbers you entered"

#floats are not good for arrays and touple, they are not exact, so they are not good for this type of problem
## For X in range(), good for average questions or summery questions that have a defined amount of varibles.
# 5. Write some code that prints out all the numbers from 1 to 10 that are divisible by 3 or 5.
print("fun fact: the following numbers are not divisible by 3 or 5 without a remainder")
for i in range(1, 11):
        if i % 3 == 0 or i % 5 == 0:
                print(i)
#       IF I % 3 != 0: 
#                continue  
#        if i % 5 != 0: 
 #               continue
 #               print(i)

#need to watch the wording of the question, it says divisible by 3 or 5, I got it reversed by accident, fixed it before I turned it in.
# the % is pretty convienent for division problems..... I need to memorize this lesson more.
# 6. Write some code that asks the user for a number and then prints out a countdown from that number to 1 using a while loop. After the countdown, print "Blast off!".
number_five = (float(input("Hello, please enter a positive whole number for a countdown to 0:  ")))
while number_five > 0:
        print(number_five)
        number_five -= 1
print("Blast off!")
# 7. Write some code that asks the user for a number and then uses a for loop to iterate from 1 to that number. If the current number is divisible by 7, print "Lucky" and continue to the next iteration. If the current number is greater than 100, break the loop.
number_six = (float(input("Hello, please enter a positive whole number, I will count how many numbers \n there are from 0 to your number and lucky numbers divisable by 7... but i will not count past 100: ")))
number_six_int = int(number_six)
for number_six in range(1, number_six_int + 1):
        if number_six % 7 == 0:
                print("Lucky")
                continue
        if number_six > 100:
                break
        print(number_six)
print("Have a nice day, and thank you for using my program!")