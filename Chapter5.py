#==================================== IF STATEMENTS ================================================

#cars = ['audi', 'bmw', 'subaru', 'toyota']

#for car in cars:
#    if car == 'bmw':
#        print(car.upper())
#    else:
#        print(car.title())

# At the heart of every "If Statement" is an expression that can be evaluated as "True" or "False"
#   This is call a "Conditional Test"


# Equality Operator (==)
#   The second '=' sign asks if the value is True. In this case, bmw is not equal to audi. Result returns false
#car = 'audi'
#print(car == 'bmw')

#car = 'Audi'
#print(car == 'audi') # This results in False since 'Audi' != 'audi'. Case sensitive 
#print(car.lower() == 'audi') # This results in True. This says that the lower case of 'Audi' is the same


# Inequality Operator (!=)
#   The exclamation mark with the equals sign represents 'NOT'

#requested_topping = 'mushroom'
#if requested_topping != 'anchovies':
#    print("Hold the anchovies!")


# Use 'AND' to check multiple conditions
#   Result will be 'True' if both conditions are met
#   Result will be 'False' if either both conditions are not met or when one of them isn't
#age_0 = 22
#age_1 = 18
#print(age_0 >= 21 and age_1 >= 21)

#age_0 = 22
#age_1 = 22
#print(age_0 >= 21 and age_1 >= 21) # Returns 'True' because both conditions pass


# Use 'OR' to check multiple conditions
#   Result will be 'True' when either both conditions are met or when one of them is met.
#   Result will be 'False' when both conditions are not met
#age_0 = 22
#age_1 = 18
#print(age_0 >= 21 or age_1 >= 21)


# Use 'IN' to check whether a Value is in a List
#requested_toppings = ['mushrooms', 'onions', 'pinnapple']
#print('mushrooms' in requested_toppings)
#print('pepperoni' in requested_toppings)


# Use 'NOT' to check where a Value is NOT in a List
#banned_users = ['andrew', 'carolina', 'david']
#user = 'marie'

#if user not in banned_users:
#    print(f"{user.title()}, you can post a response if you wish.")

# Boolean Expressions (another name for a conditional test)
# Boolean Value is either 'True' or 'False'

#game_active = True
#can_edit = False


# Getting into the IF statements & IF-ELSE statement

#age = 17
#if age >= 18:
#    print("You are old enough to vote!")
#    print("Have you registered to vote yet?")
#else:
#    print("You are not old enough to vote yet!")


# IF-ELIF-ELSE statements

# First way to write if-elif-else statement
#age = 18
#if age < 4:
#    print("Your admission cost is $0")
#elif age < 18:
#    print("Your admission cost is $25")
#else:
#    print("Your admission rate is $40")

# Second way to write if-elif-else statement
#age = 12
#if age < 4:
#    price = 0
#elif age < 18:
#    price = 25
#else:
#    price = 40
#print(f"Your admission cost is ${price}.")


#------------------------------------- PRACTICE PROBLEMS --------------------------------------------------

# 1a) Write an if statement that passes
#alien_color = 'green'
#if alien_color == 'green':
#    print("You just earned 5 points!")

# 1b) Write an if statement that fails
#alien_color = 'red'
#if  alien_color == 'green':
#    print("You just earned 5 points!")

# 2a) Write an if-else chain that runs on the if statement
#alien_color = 'green'
#if alien_color == 'green':
#    print("You just earned 5 points!")
#else:
#    print("You just earned 10 points!")

# 2b) Write an if-else chain that runs on the else statement
#alien_color = 'red'
#if alien_color == 'green':
#    print("You just earned 5 points!")
#else:
#    print("You just earned 10 points!")

# 3a) Turn if-else statement into an if-elif-else statement: Passes on if statement
#alien_color = 'green'
#if alien_color == 'green':
#    print("You just earned 5 points!")
#elif alien_color == 'red':
#    print("You just earned 10 points!")
#else:
#    print("You just earned 15 points!")

# 3b) Turn if-else statement into an if-elif-else statement: Passes on elif statement
#alien_color = 'red'
#if alien_color == 'green':
#    print("You just earned 5 points!")
#elif alien_color == 'red':
#    print("You just earned 10 points!")
#else:
#    print("You just earned 15 points!")

# 3c) Turn if-else statement into an if-elif-else statement: Passes on else statement
#alien_color = 'yellow'
#if alien_color == 'green':
#    print("You just earned 5 points!")
#elif alien_color == 'red':
#    print("You just earned 10 points!")
#else:
#    print("You just earned 15 points!")

# 4a) Write an if-elif-else statement that determines a person's stage of life
#age = 30
#if age < 2:
#    print("You are a baby.")
#elif age < 4:
#    print("You are a toddler.")
#elif age < 13:
#    print("You are a kid.")
#elif age < 20:
#    print("You are a teenager.")
#elif age < 65:
#    print("You are an adult.")
#else:
#    print("You are an elder.")

# 5) Write 5 if statements to check whether a certain fruit is in my list
#favorite_fruits = ['bananas', 'apples', 'kiwi', 'blueberries', 'grapes']
#for fruit in favorite_fruits:
#    if fruit == 'bananas':
#        print("I love bananas!")
#for fruit in favorite_fruits:
#    if fruit == 'apples':
#        print("I love apples!")
#for fruit in favorite_fruits:
#    if fruit == 'kiwi':
#        print("I love kiwi!")
#for fruit in favorite_fruits:
#    if fruit == 'blueberries':
#        print("I love blueberries!")
#for fruit in favorite_fruits:
#    if fruit == 'grapes':
#        print("I love grapes!")


# ----------------------------------- Using IF statments with Lists ---------------------------------------
#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#for requested_topping in requested_toppings:
#    print(f"Adding {requested_topping}.")

#print("\nFinished making your pizza!")

# adding IF statement inside the loop for Pizzeria if it runs out of an ingredient
#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print(f"Sorry, we are out of green peppers right now.")
#    else:
#        print(f"Adding {requested_topping}.")

#print("\nFinished making your pizza!")

# Checking that a List is Not empty
#requested_toppings = []

#if requested_toppings:
#    for requested_topping in requested_toppings:
#        print(f"Adding {requested_topping}.")
#    print("\nFinished making your pizza.")
#else:
#    print("Are you sure you want a plain pizza?")

# Using Multiple Lists
#available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
#requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

#for requested_topping in requested_toppings:
#    if requested_topping in available_toppings:
#        print(f"Adding {requested_topping}.")
#    else:
#        print(f"Sorry, we don't have {requested_topping}.")
#print("\nFinished making your pizza!")


#------------------------------------ PRACTICE PROBLEMS ---------------------------------------------------

# 1) Make a List w/5 usernames. Print a greeting for every username

#usernames = ['admin', 'john', 'jane', 'mary', 'steve']

#for username in usernames:
#    if username == 'admin':
#        print(f"Hello {username.title()}, would you like to see a status report?")
#    else:
#        print(f"Hello {username.title()}, thank you for logging in again.")

# 2) If statement to make sure the list of users is NOT empty
#usernames = []

#if usernames:
#    for username in usernames:
#        print(f"Hello {username.title()}, thank you for logging in again.")
#else:
#    print(" We need to find some users!")

# 3) Create a program that simulates how websites ensure that everyone has a unique username
#current_users = ['John', 'Susan', 'Steve', 'Aaron', 'Lisa']
#new_users = ['Kevin', 'Jared', 'John', 'Carol', 'Susan']


#for new_user in new_users:
#    if new_user in current_users:
#        print(f"Sorry, {new_user} is in use. Please enter a new username.")
#    else:
#        print("That username is available.")

# 4) IF-ELIF-ELSE statement for ordinal numbers (loop through them)
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"\n{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"\n{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"\n{ordinal_number}rd")
    else:
        print(f"\n{ordinal_number}th")
