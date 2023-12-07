# Lab 11
# Author:Frank R. Leotta III

# Lab 11 will show basic understanding of Object Oriented Programming in Python.

import tabulate
# 1. Create a class called Product. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# price -> this should be a float
# product_id (this should be a unique number)
class Product:
    def __init__(self, name, price: float, product_id):# self is ref that varible  regular and optional varibles. assume name product price is required
        self.name = name # self is a ref to the object, name is a varible, self.name is a attribute
        self.price = price 
        self.product_id = product_id

# 2. Create a method called __str__ that returns a string with the following format:
# Product: <name>, Price: <price>, ID: <product_id>
# Hint: use f-strings to format the string.

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, ID: {self.product_id}" # could tpye haha  you will never get this, its always typing it up in the stirng format
    
# Great now that we have a Product lets create a Customer class.
# 3. Create a class called Customer. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# customer_id (this should be a unique number)
# cart -> this should be a list that contains Product objects.

class Customer:
    def __init__(self, name, customer_id): #all of these are required
        self.name = name #diff over time
        self.customer_id = customer_id # diff over time
        self.cart = [] # its going to be the same every time, so no need to pass it in as a paramiter

# also create a __str__ method that returns a string with the following format:
# Customer: <name>, ID: <customer_id>
# Hint: use f-strings to format the string.
    def __str__(self): #need to pass in self as paramiter
        return f"Customer: {self.name}, ID: {self.customer_id}" # this is a string, not a list, so no brackets, just a string

# 4. Create a method called add_to_cart that takes in a Product object and adds it to the cart list. print out the product that was added and the customer's name.
    def add_to_cart(self, product: Product): # self is the customer, product is the product  #taking a product and add it to cart.  List can hold anything inside of them.  sting as an object is, lists can hold objects. cart can hold product objects inside of it.
    #we can typehint the product.
        self.cart.append(product) # add the product to the cart class 
        print(f"{product.name} was added to {self.name}'s cart") # print out the product that was added and the customer's name.

# 5. Create a method called remove_from_cart that takes in a Product object and removes it from the cart list.
    def remove_from_cart(self, product: Product): # self is the customer, product is the product
    #.name is associated with that object.  Self.name is the associated with the customer
    # product name or product name
    #self.name
    #product.name for the product name# this is where encapsulation comes in.   getter and setter mentioned, but not covered due to time constraints
        self.cart.remove(product) # remove the product from the cart list
        print(f"{product.name} was removed from {self.name}'s cart") # print out the product that was removed and the customer's name.

# 6. Create a method called checkout calculates the total price of all the products in the cart and prints out the total. After printing out the total, empty the cart.
# Hint: you will need to loop through the cart and add up the prices.

    def checkout(self): # self is the customer
        total = 0 # create a total variable and set it to 0
        for product in self.cart:
            total += product.price  #all way upp  here the products have price associated with them, so you can add them up... remember datetime having . associated with that headach only different
        print(f"{self.name}'s total is {total}") # print out the customer's name and the total price of all the products in the cart. #api in website, take the total charge and add taxes to it. 
        self.cart = [] # empty the cart list

# 7. Create a method called display_products that prints out all the products in the cart list. (use the __str__ method from the Product class)
    def display_products(self): # self is the customer  
        print(f"{self.name}'s cart:") # print out the customer's name and the total price of all the products in the cart.  Self.name is whatever funtion you are currently in
        for product in self.cart:
            print(product)

# 8. **Extra** Create a method called display_products_pretty that prints out all the products in the cart list. 
# (use the tabulate library)
# Make a nice table table using the tabulate library.

    def display_products_pretty(self): # self is the customer  
    #NEED TO INSTALL TABULATE LIBRARY via pip install tabulate
        # import the tabulate library,  pip install first
        print(f"{self.name}'s cart:") # print out the customer's name and the total price of all the products in the cart.  Self.name is whatever funtion you are currently in
        print(tabulate.tabulate(
            [{"Name": Product.name, "Price": Product.price, "ID": Product.product_id} for Product in self.cart],
              headers="keys", tablefmt="fancy_grid"))
        #as long as it works and you dont tab, you can enter to see the next line... just don"t space or tab.

 # print out the cart list in a nice table fo  #pythonic way of looking at it



# 7. Create a class called Store. The class should have the following attributes in the __init__ method:
# products -> this should be a list that contains Product objects.
# customers -> this should be a list that contains Customer objects.
class Store:      
    def __init__(self): # self is the store
        self.products = [] # this should be a list that contains Product objects.
        self.customers = [] # this should be a list that contains Customer objects.


# 8. Create a method called add_product that takes in a Product object and adds it to the products list.
    def add_product(self, product: Product): # self is the store, product is the product
        self.products.append(product) # add the product to the products list
        print(f"{product.name} was added to the store") # print out the product that was added and the store name.

# 9. Create a method called add_customer that takes in a Customer object and adds it to the customers list.
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"{customer.name} was added to the store")

# 10. Create a method called display_products that prints out all the products in the products list.
    def display_products(self):
        print("Products:")
        for product in self.products:
            print(product)
# 11. Create a method called display_customers that prints out all the customers in the customers list.
    def display_customers(self):
        print("Customers:")
        for customer in self.customers:
            print(customer)

# Typically we would create another file and import the classes we created. For this lab, we will just create the objects in this file to show how its possible.

# 12. Create a store object called store.
store = Store() # create a store object called store

# 13. Create a product object called product1 with the following attributes:
# name: "iPhone 12"
# price: 799.99
# product_id: 1
product1 =  Product("iPhone 12", 799.99, 1) # this is how you create a product object, this is how you create a product object
# 14. Create a product object called product2 with the following attributes:
# name: "iPhone 12 Pro"
# price: 999.99
# product_id: 2
product2 = Product("iPhone 12 Pro", 999.99, 2) # this is how you create a product object

# 15. Create a product object called product3 with the following attributes:
# name: "iPhone 12 Pro Max"
# price: 1099.99
# product_id: 3
product3 = Product("iPhone 12 Pro Max", 1099.99, 3) # this is how you create a product object

# 16. Create a customer object called customer1 with the following attributes:
# name: "John"
# customer_id: 1
customer1 = Customer("John", 1) # this is how you create a customer object

# 17. Create a customer object called customer2 with the following attributes:
# name: "Jane"
# customer_id: 2
customer2 = Customer("Jane", 2)

## customer2.desplay_products() # this is how you print a customer object

# 18. Add product1 to the store using the add_product method.
store.add_product(product1)
# 19. Add product2 to the store using the add_product method.

# 20. Add product3 to the store using the add_product method.

# 21. Add customer1 to the store using the add_customer method.

store.add_customer(customer1) # this is how you add a customer to the store

# 22. Add customer2 to the store using the add_customer method.
store.add_customer(customer2)
# 23. Add product1 to customer1's cart using the add_to_cart method.
customer1.add_to_cart(product1)
# 24. Add product2 to customer1's cart using the add_to_cart method.
customer1.add_to_cart(product2)
# 25. Add product3 to customer2's cart using the add_to_cart method.
customer2.add_to_cart(product3)
# 26. Display current products in customer1's cart using the display_products method.
customer1.display_products_pretty()
####this seems wrong, need to fix

# 27. Display current products in customer2's cart using the display_products method.
customer2.display_products()
# 28. Checkout customer1's cart using the checkout method.
customer1.checkout()
# 29. Checkout customer2's cart using the checkout method.
customer2.checkout()
# 30. Display current products in customer1's cart using the display_products method. (should be empty)
customer1.display_products()