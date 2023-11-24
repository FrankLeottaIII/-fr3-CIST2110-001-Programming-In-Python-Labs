# Lab 10
# Author:

# Lab 10 will show demonstrate how Dictionary's work in Python.
"""unpacking a dictionary"""
# 1. Create a dictionary called my_dict with the following key value pairs:
# Key: "name", Value: "John"
# Key: "age", Value: 30
# Key: "city", Value: "Trenton"
# Key: "state", Value: "New Jersey"
my_dict = {"name": "John", "age": 30, "city": "Trenton", "state": "New Jersey"}
# a string and a string


# 2. Print out the dictionary.
print(my_dict)

# 3. Print out the value for the key "name".
for key, value in my_dict.items():
        if key == "name":
            print(value)
# 4. Lookup the key associated with the value "New Jersey" and print it out.
# Hint 1: You will need to loop through the dictionary.
# Hint 2: remember you can use the .items() method to get the key and value.

# 5. Add a new key value pair to the dictionary.
# Key: "country", Value: "USA"
my_dict{"country"} = "USA"

# 6. Print out the dictionary.
print(my_dict)
# 7. Remove the key value pair with the key "city".
del my_dict["city"]
# 8. Print out the dictionary.
print(my_dict)
# 9. Create a dictionary called cities with an key as the City name and values as a list that contains the state, population, and country.
# use the following data:
# Trenton, New Jersey, 84,913, USA
# New York City, New York, 8,336,817, USA
# Los Angeles, California, 3,979,576, USA
# Chicago, Illinois, 2,693,976, USA
# Houston, Texas, 2,320,268, USA
# Phoenix, Arizona, 1,680,992, USA
# Philadelphia, Pennsylvania, 1,584,138, USA
# San Antonio, Texas, 1,547,253, USA
# San Diego, California, 1,423,851, USA
# dictionary of dictionaries

cities = {
    "Trenton": {"state": "New Jersey", "Population": 84913, "Country": "USA"},# key and the value is another dicionary.   dictinary inside a dictionary
    "New York City": {"state": "New York", "Population": 8336817, "Country": "USA"},
    "Los Angeles": {"state": "California", "Population": 3979576, "Country": "USA"},
    "Chicago": {"state": "Illinois", "Population": 2693976, "Country": "USA"},
    "Houston": {"state": "Texas", "Population": 2320268, "Country": "USA"},
    "Phoenix": {"state": "Arizona", "Population": 1680992, "Country": "USA"},
    "Philadelphia": {"state": "Pennsylvania", "Population": 1584138, "Country": "USA"},
    "San Antonio": {"state": "Texas", "Population": 1547253, "Country": "USA"},
    "San Diego": {"state": "California", "Population": 1423851, "Country": "USA"}}

# print(cities) #will get confusing.   being able to search a key and get a value is important
# pandas is a good libary that will helpu us



# 10. Print a table of the data using the pandas library.   #used for transforming data, lists dicionarys.  bunch of data tro trnsform and data midles   pands is the go to for that type of wokrk.  simple one
# pip install pandas
import pandas as pd
#create a data frame, a word that holds you data
# will know how to handle dicinoary of dicionaries
df = pd.DataFrame(cities)
print(df)  #  it will look like a table, much different and more organized in a easier to read fasion, common to do ... at the dope, a symbol you want to transpose data(reverse rows and columbs)

# 11. Use the tabulate library to print out the table.
# pip install tabulate
from tabulate import tabulate # have the tabulate class here
#try to pass it through tabulate
""" impsort that tabluate muduple"""
pretty_table = tabulate(df, headers="keys,..........") #pass in the dictionary and the headers
#  sort of likes a sql table
#tabulate olnly takes in lists.   if you put a dict to it, it will get erros
#you need to convert the dict to a list if you want to use tabulate
print("------------------")
print(pretty_table)
print("------------------")
#pansas will covert your list
#both are valid, and wil work on project 2.  You can do pandas,  unpack method as well for project 2

# 11. Print out the population for the city of Chicago.
print (cities["Chicago"].get("Population") #reference ky , its chacago(city names, the values are the diconary.
       #inside the second ditionary, you can use.get()  to get value of population
#last value you want to get, use .get()  to get the value of the key
""" pandaz is slow, so might not be for ehtrythin g, """


# Dictionary unpacking is a new feature in Python 3.9 and allows you to unpack a dictionary into a list of dictionaries.
# You can then use tabulate to print out the table.

# In our case, {"City": city, **info} creates a new dictionary that includes a "City" key with the city name and all the key-value pairs from the info dictionary.

# For example, if city is "Chicago" and info is {"state": "Illinois", "Population": 2693976, "Country": "USA"}, the new dictionary will be {"City": "Chicago", "state": "Illinois", "Population": 2693976, "Country": "USA"}. This is the same as {"City": city, **info}.
# The ** operator unpacks the info dictionary into the new dictionary

# Transform the data
data = [{"City": city, **info} for city, info in cities.items()] #** going to deal with a dicionary within a dictionary... python knows
""" cleaner to do it in one line, but its compressed
it will end up returning a list of ditonarys.[ strubg comprension """
#city ,info = key, value  For loops you can name what you want
''' you can make it multible lines if you want it to'''


#Print the table using tabulate
#print(data)
print(tabulate(data, headers="keys")) #keys are the cities
'''a simple dable there
if you wanted to d sql pass it thorugha  paramiter
I am going to be using pandas alot, so it works for me.'''
# 12. How many cities have a population greater than 1 million? Use a for loop to iterate through the dictionary.

# counter valerible
counter = 0
for city, info in cities:  # for each line in the cities dictionary
    if info["Population"] > 1000000: # city is each of the lines, we are [1] 2 3...   grabing each  population of each cities 
        counter += 1 #if cities population is greater than 1 million, add 1 to the counter

print(f'citeis with poulation grater than 1 million: {counter}')

'''its a trial and error sort of think, it takes time to get used to it
 the trick of it is getting all the data at once'''

# 13.  How many cities are in the USA? Use .items() to get a list of tuples. Use a for loop to iterate through the list of tuples.
# Hint 1: You will need to use the second item in the tuple. The second item is a dictionary. IE. for city, info in cities.items():

#this is compared to the key valeu, another way to traverse a dicionary, , is the first way, this is the sencond way
counter = 0
cities.items() #this is a list of tuples
#key is trention cvalue is all that stuf
for city, info in cities.items(): #for each line in the cities dictionary
    if info["Country"] == "USA": #if the country is USA (want to see if the country is USA)
        counter += 1 #add 1 to the counter
#there are 9 cities in the USA
"""need to go through it again, missed the first part due to synch issues"""