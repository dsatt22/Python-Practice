#==================================== USER INPUT AND WHILE LOOPS ===========================================

# The input() function pauses your program and waits for the user to enter something

# Simple input() example
# here we will assign a variable to the input
#message = input("Please enter your name: ")

# here we will print out the variable
#print(f"\nHello, {message}!")

# Python will then repeat back what the user inputs

## Another example
#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "

#name = input(prompt)
#print(f"\nHello, {name}!")

# Using int() to Accept Numerical Input
#   -If you don't add the int() function, Python will interpret the text as a string

## Example 1) Python interpreting a number as a string
#age = input("How old are you? ")
#age >= 18
#print(f"You are {age} years old!")

# By adding the int() function and entering a number inside the function will tell Python to run it as a #

## Example 2) Using int() function so Python doesn't misinterpret a number as a string
#age = input("How old are you? ")
#age = int(age)
#age >= 18

#print(f"\nYou are {age} years old!")

## An example of when using int() function works in the real world
#height = input("How tall are you, in inches? ")
#height = int(height)

#if height >= 48:
#    print("\nYou are tall enough to ride!")
#else:
#    print("\nSorry, you must be taller than 48 inches to ride this ride.")


#------------------------------ The Modulo Operator ----------------------------------------------------
# The modulo operator uses the % sign and it divides one number by another and prints the remainder

## Example
#print(18 % 9)

## Example #2
#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)

#if number % 2 == 0:
#    print(f"\nThe number {number} is even.")
#else:
#    print(f"\nThe number {number} is odd.")


#============================= PRACTICE PROBLEMS ==================================

## 1) Write a program that asks the user what kind of rental car they would like. Print a message about
#    that car, such as "Let me see if I can find you a Subaru."

#rental_cars = input("What kind of rental car would you like? ")
#print(f"Let me see if I can find you a {rental_cars}")


## 2) Write a program that asks the user how many people are in their dinner group. If the answer is more
#    than eight, print a message saying they'll have to wait for a table. Otherwise, report that their
#    table is ready.

#dinner_group = input("How many people are in your dinner group? ")
#dinner_group = int(dinner_group)
#if dinner_group > 8:
#    print(f"\nI'm sorry to inform you, but you will have to wait a little longer for a table.")
#else:
#    print(f"\nThank you, your table is ready!")


## 3) Ask the user for a number, and then report whether the number is a multiple of 10 or not.
###### Come back to later ################
#number = input("Enter a number between 1-1000, and I'll let you know if it is a multiple of 10 or not: ")
#number = int(number)

#if number % 10:
#    print(f"\nThe number you entered is a multiple of 10!")
#else:
#    print(f"\nThe number you entered is NOT a multiple of 10.")


#------------------------------- Introducing While Loops ---------------------------------------------------

## While Loop in Action ##
#current_number =  1
#while current_number <= 5:
#    print(current_number)
#    current_number += 1
## The += operator is shorthand for current_number = current_number + 1


## Letting the User Choose When to Quit ##
#prompt = "\nTell me something, and I will repeat it back to you: "
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit': 
#    message = input(prompt)
#    print(message)

## We don't want Python to print 'quit' once it is entered, so here is a quick fix for that
#    if message != 'quit':
#        print(message)


## Using a Flag ##

#prompt = "\nTell me something, and I will repeat it back to you: "
#prompt += "\nEnter 'quit' to end the program. "

#active = True
#while active: 
#    message = input(prompt)

#    if message == 'quit':
#        active = False
#    else:
#        print(message)


## Using break to Exit a Loop
#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\n(Enter 'quit' when you are finished.) "

#while True:
#    city = input(prompt)
    
#    if city == 'quit':
#        break
#    else:
#        print(f"I'd love to go to {city.title()}!")   


## Using continue in a Loop

#current_number = 0
#while current_number < 10:
#    current_number += 1
#    if current_number % 2 == 0:
#        continue
    
#    print(current_number)


#========================= PRACTICE PROBLEMS ============================

# 1) Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.

#prompt = "\nEnter what toppings you want to add to your pizza:"
#prompt += "\n(Enter 'quit' when you are finished.) "

#while True:
#    topping = input(prompt)

#    if topping == 'quit':
#        break
#    else:
#        print(f"Adding {topping} to your pizza.")


# 2) A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket. 

movie_tickets = input("How old are you? ")
age = int(movie_tickets)

while True:
    age = input(age)

    if age == 'quit':
         break
    elif age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("Your tickets are $10")
    else:
        print("Your ticket is $15")