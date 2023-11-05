#Lab 6 in python


# Creating Lists and Tuples

# Create a list named fruits with the following elements: "apple", "banana", "cherry".
fruits = ["apple", "banana", "cherry"]
print(fruits)
# Create a tuple named coordinates with three numbers representing a point in 3D space.
coordinates = (1, 2, 3)
print(coordinates)

# Accessing Elements

# Print the second element of the fruits list.
print(fruits[1])
# Print the last element of the coordinates tuple.
print(coordinates[-1])


# Modifying lists

# import gc  
# gc.collect() 
# garbage collector... it didn't work, the cell is still just inserting blueberry over and over again. so annoying

# # Add "orange" to the end of the fruits list.
# fruits.append("orange")
# print(fruits) #to show the change
# Insert "blueberry" at the beginning of the fruits list.
print(fruits)
fruits.insert(0, "blueberry")
print(fruits)
#  Remove "banana" from the fruits list.

remove = fruits.remove("banana")
print(fruits)
# Change the first element of the fruits list to "strawberry".
fruits[0] = "strawberry"
print(fruits)