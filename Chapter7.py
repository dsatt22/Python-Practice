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


#-------------------------------