#** WORKING WITH LISTS **

#---------------------------------* For loop *--------------------------------------------------------------

#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
#    print(magician)
#    print(f"{magician.title()}, that was a great trick!")

#friends = ['brandon', 'jared', 'aaron', 'josh', 'caila', 'joey']
#for friend in friends:
#    print(friend)
#    print(f"{friend.title()} is a great friend!")


#-------------------------------* Range() Function * -------------------------------------------------------

#for value in range(1, 6):
#   print(value)

#numbers = list(range(1, 6))
#print(numbers)

#evenNumbers = list(range(2, 11, 2))  #Third number (2) says to print out numbers by 2
#print(evenNumbers)

#squares = []
#for value in range(1,20):
#    square = value ** 2      #Asterisks (**) in Python represent exponents
#    squares.append(square)
#print(squares)

#squares =  []
#for value in range(1, 11):
#    squares.append(value**2)  #got rid of line 4 from above and combined it with line 3 and it performs the same way
#print(squares)

#------------------------List Comprehension-----------------------------------------------------------------
#squares = [value**2 for value in range(1,11)]
#print(squares)

#combined lines 2 &3 into line 1 and it performs like the 2 examples above
#first define the value (value**2), then write in the 'for loop' (for value in range).

#----------------------------PRACTICE PROBLEMS--------------------------------------------------------------

# 1) use a for loop to print the numbers from 1 20
#for value in range(1,21):
#    print(value)

# 2)make a list of the numbers from one to one million, and then use a for loop to print the numbers
#numbers = [1, 1000001]
#for numbers in range(1, 1000001):
#    print(numbers)

# 2a) use the min() & max() to make sure the list is accurate. Use the sum() function to see Python add a million numbers
#numbers = [1, 1000001]
#min(numbers)
#max(numbers)
#print(numbers)

#for value in range(1,20,2):
#    print(value)

#for value in range(3,30,3):
#    print(value)

#cubes = []
#for value in range(1,11):
#    cube = value ** 3
#    cubes.append(cube)
#print(cubes)

#cubes = [value**3 for value in range(1,11)]
#print(cubes)

#-------------------------------Looping through a Slice-----------------------------------------------------

#players = ['charles', 'martina', 'michael', 'florence', 'eli']
#for player in players[:3]:
#    print(player.title())

#-----------------------------Copying a List----------------------------------------------------------------

#my_foods = ['pizza', 'chicken', 'burgers']
#friend_foods = my_foods[:]

#print("My favorite foods are:")
#print(my_foods)

#print("\nMy friends favorite foods are:")
#print(friend_foods)

#my_foods.append('quesadillas')
#friend_foods.append('chili')

#print("My favorite foods are:")
#print(my_foods)

#print("\nMy friends favorite foods are:")
#print(friend_foods)

#------------------------------------Tuples----------------------------------------------------------------

#dimensions = (200, 50)
#print(dimensions[0])
#print(dimensions[1])

#dimensions[0] = 250  Unable to change values in a tuple. They are "Immutable"

#Looping through all values of a Tuple
#for dimension in dimensions:
#    print(dimension)

#Writing over a Tuple
#dimensions = (200, 50)
#print("Original dimensions:")
#for dimension in dimensions:
#    print(dimension)

#dimensions = (400, 100)
#print("\nModified dimensions:")
#for dimension in dimensions:
#    print(dimension)

#------------------------------Practice--------------------------------------------------------------------
#basicFoods = ('chicken', 'steak', 'seafood', 'potatoes', 'broccoli')
#print("Original food list:") #added in this line for the 3rd part of the practice to show original list
#for basicFood in basicFoods:
#    print(basicFood)

#basicFoods[2] = 'rice'  #python rejects this because a tuple is immutable

#basicFoods = ('chicken', 'pork', 'rice', 'potatoes', 'broccoli')
#print("\nModified food list:")
#for basicFood in basicFoods:
#    print(basicFood)

#-----------------------------------Styling Your Code------------------------------------------------------

# *PEP- Python Enhancement Proposal
    # PEP 8 is fairly lengthly and is one of the oldest
    #   - relates to more complex coding structures
    # Recommends using 4 spaces per indent level
# *Try to write code that is easier to read for other programmers
    # Programmers spend more time reading code then writing
