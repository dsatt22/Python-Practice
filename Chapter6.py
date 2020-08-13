#======================================== DICTIONARIES ==============================================

# A Simple Dictionary

#alien_0 = {'color': 'green', 'points': 5}

#print(alien_0['color'])
#print(alien_0['points'])


# Working with Dictionaries
    # A dictionary in Python is a collection of 'key-value pairs'.
    # Each 'key' is connected to a 'value'.
    # Use the 'key' to access the 'value' associated with it.
    # In Python, a dictionary is wrapped in braces {}
    # Every 'key' is connected to its value by a colon (;),
    # Individual key-value pairs are separated by commas (,)

#new_points = alien_0['points']
#print(f"\nYou just earned {new_points} points!")


# Adding in new key-values

#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)


# Modifying values in a dictionary
#-------------- Example 1 -----------------------------------------------------

#alien_0 = {'color': 'green'}
#print(f"The alien is {alien_0['color']}")

#alien_0['color'] = 'yellow'
#print(f"The alien is now {alien_0['color']}")

#-------------- Example 2 -----------------------------------------------------

#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
#print(f"Original position: {alien_0['x_position']}")

# Move alien to the right
# Determine how far to move the alien based on its current speed.
#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2
#else:
#    x_increment = 3

# The new position is the old position plus the increment.
#alien_0['x_position'] = alien_0['x_position'] + x_increment

#print(f"New position: {alien_0['x_position']}")


# A dictionary of similar objects

#favorite_languages = {
#    'jen': 'python',
#    'sara': 'javascript',
#    'phil': 'ruby',
#    'aaron': 'python',
#    }

#language = favorite_languages['jen'].title()
#print(f"Jen's favorite language is {language}.")


# Using get() to access values

#-------------- Example ------------------------------------
#alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points']) --- Will spit back an error because 'points' doesn't exist in the dictionary

#point_value = alien_0.get('points', 'No point value assigned.')
#print(point_value)


#------------------------------- PRACTICE PROBLEMS ----------------------------------------------------------

# 1) Store information about a person you know into a dictionary and then print out each piece of info
#person = {
#    'first_name': 'Caila',
#    'last_name': 'Anderson',
#    'age': 30,
#    'location': 'Jacksonville',
#    }

#print(person['first_name'])
#print(person['last_name'])
#print(person['age'])
#print(person['location'])

# 2) Store 5 people's favorite numbers in a dictionary

#favorite_numbers = {
#    'Joey': 19,
#    'Ryan': 10,
#    'Dustin': 22,
#    'Caila': 13,
#    'Jim': 69,
#    }

#print(favorite_numbers['Ryan'])
#print(favorite_numbers['Jim'])
#print(favorite_numbers['Caila'])
#print(favorite_numbers['Joey'])
#print(favorite_numbers['Dustin'])

#-----------------------------------------------------------------------------------------------------------

#------------------------------- Looping Through a Dictionary ----------------------------------------------

#user_0 = {
#    'username': 'dsattler',
#    'first_name': 'dustin',
#    'last_name': 'sattler',
#}

#for key, value in user_0.items():
#    print(f"\nKey: {key}")
#    print(f"Value: {value}")


# Looping Through All the Keys in a Dictionary----------------------------------------------

#favorite_languages = {
#    'jen': 'python',
#    'sara': 'javascript',
#    'phil': 'ruby',
#    'aaron': 'python',
#    }

#for name, languages in favorite_languages.items():
#    print(f"{name.title()}'s favorite language is {languages.title()}.")

#for name in favorite_languages.keys():
#    print(name.title())

#friends = ['phil', 'sara']
#for name in favorite_languages.keys():
#    print(f"Hi {name.title()}")

#    if name in friends:
#        language = favorite_languages[name].title()
#        print(f"\t{name.title()}, I see you love {language}!")

#if 'erin' not in favorite_languages.keys():
#    print("Erin, please take our poll!")


# Looping Through a Dictionary's keys in a Particular Order -------------------------------------------

#for name in sorted(favorite_languages.keys()):
#    print(f"{name.title()}, thank you for taking our poll!")


# Looping Through All the Values in a Dictionary ------------------------------------------------------

#print("The following languages were mentioned:")
#for language in favorite_languages.values():
#    print(language.title())

#for language in set(favorite_languages.values()):
#    print(language.title())


#---------------------------------- PRACTICE PROBLEMS --------------------------------------------------

#major_rivers = {
#    'nile': 'egypt',
#    'mississippi river': 'mississippi',
#    'ohio river': 'ohio & kentucky',
#}

#for key, value in major_rivers.items():
#    print(f"The {key.title()} runs through {value.title()}.")


#favorite_languages = {
#    'jen': 'python',
#    'sara': 'javascript',
#    'phil': 'ruby',
#    'aaron': 'python',
#    }
#pollers = ['caila', 'aaron', 'sarah', 'jared', 'dustin']

#friends = ['caila', 'jared', 'dustin']


#---------------------------------------------------------------------------------------------------------

#----------------------------------- Nesting -------------------------------------------------------------

#----------- A List of Dictionaries---------------------

# Manually create aliens

#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)


# Automatically generate 30 aliens

# first we make an empty list for storing aliens.
#aliens = []

# we then make 30 green aliens
#for alien_number in range(30):
#    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#    aliens.append(new_alien)

# to show the first 5 aliens, we are going to use the slice method
#for alien in aliens[:5]:
#    print(alien)
#print("...")

# now show how many aliens have been created.
#print(f"Total number of aliens: {len(aliens)}")


# Now to modify the list to change some aliens characteristics (add code between the 2nd and 3rd sections)
#aliens = []

#for alien_number in range(30):
#   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#    aliens.append(new_alien)

#Added new code here to modify the first 3 aliens
#for alien in aliens[:3]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['points'] = 10

#for alien in aliens[:5]:
#    print(alien)
#print("...")


# A List in a Dictionary

#First store information about a pizza being ordered
#pizza = {
#    'crust': 'thick',
#    'toppings': ['mushrooms', 'extra cheese'],
#}

#Then summarize the order
#print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

#for topping in pizza['toppings']:
#    print(f"\t{topping}")


#Personal practice problem w/nesting. creating lists inside a dictionary

#favorite_languages = {
#    'dustin': ['python', 'html', 'css'],
#    'aaron': ['swift', 'python', 'ruby'],
#    'caila': ['c', 'javascript'],
#    'josh': ['ruby', 'haskell'],
#}

#for name, languages in favorite_languages.items():
#    print(f"\n{name.title()}'s favorite languages are:")
#    for language in languages:
#        print(f"\t{language.title()}")


# A Dictionary in a Dictionary

#users = {
#    'aeinstein': {
#        'first': 'albert',
#        'last': 'einstein',
#        'location': 'princeton',
#    },
#    'mcurie': {
#        'first': 'mary',
#        'last': 'curie',
#        'location': 'paris',
#    },
#}

#for username, user_info in users.items():
#    print(f"\nUsername: {username}")
#    full_name = f"{user_info['first']} {user_info['last']}"
#    location = user_info['location']

#    print(f"\tFull name: {full_name.title()}")
#    print(f"\tLocation: {location.title()}")

#===================================== PRACTICE PROBLEMS ==================================================

# 1) Start with the program you wrote for Exercise 6-1. Make 2 new dictionaries representing different
#    people, and store all three dictionaries in a list called people. Loop through your list of people.
#    As you loop through, print everything you know about each person.

#people = {
#    'canderson': {
#        'first_name': 'caila',
#        'last_name': 'anderson',
#        'age': 30,
#        'location': 'florida',
#        },
#    'awaters': {
#            'first_name': 'aaron',
#            'last_name': 'waters',
#            'age': 30,
#            'location': 'california',
#            },
#    'jkirk': {
#            'first_name': 'jared',
#            'last_name': 'kirk',
#            'age': 27,
#            'location': 'washington',
#            },
#    }

#for username, user_info in people.items():
#    print(f"username: {username}")
#    full_name = f"{user_info['first_name']} {user_info['last_name']}"
#    age = f"{user_info['age']}"
#    location = f"{user_info['location']}"

#    print(f"\tFull name: {full_name.title()}")
#    print(f"\tAge: {age}")
#    print(f"\tLocation: {location.title()}")



# 2) Make Several dictionaries, where each dictionary represents a different pet. In each dictionary,
#    include the kind of animal and the owner's name. Store these dictionaries in a list called pets.
#    Next, loop through your list and print everything you know about each pet.

#pet_1 = {'owner': 'dustin', 'pet': 'dog',}
#pet_2 = {'owner': 'caila', 'pet': 'dog',}
#pet_3 = {'owner': 'josh', 'pet': 'cat',}
#pet_4 = {'owner': 'krystal', 'pet': 'fish',}

#pets = [pet_1, pet_2, pet_3, pet_4]

#for pet in pets:
#    print(f"\n{pet['owner'].title()} has a:")
#    print(f"\t{pet['pet']}")



# 3) Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
#    and store one to three favorite places for each person. Loop through the dictionary, and print each
#    person's name and their favorite places.

#favorite_places = {
#    'dustin': ['paris', 'rome', 'sydney'],
#    'caila': ['venice', 'berlin', 'london'],
#    'aaron': ['toronto', 'las angeles'],
#}

#for names, places in favorite_places.items():
#    print(f"\n{names.title()}'s favorite places are:")
#    for place in places:
#        print(f"\t{place.title()}")



# 4) Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then
#    print each person's name along with their favorite numbers.

#favorite_numbers = {
#    'Joey': [19, 43],
#    'Ryan': [10, 13],
#    'Dustin': [22, 4, 7],
#    'Caila': [13, 21],
#    'Jim': [69, 33],
#    }

#for names, numbers in favorite_numbers.items():
#    print(f"\n{names.title()}'s favorite numbers are:")
#    for number in numbers:
#        print(f"\t{number}")



# 5) Make a dictionary called CITIES. Use the name of three cities as keys in your dictionary. Create
#    a dictionary of information about each city and include the country that the city is in, its
#    approximate population, and one fact about the city. The keys for each city's dictionary should be
#    something like country, population, and fact. Print the name of each city and all info stored.





# 6) We're now working with examples that are complex enough that they can be extended in any number of ways.
#    Use one of the example programs from this chapter, and extend it by adding new keys and values,
#    changing the context of the program or improving the formatting of the output.