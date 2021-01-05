# Python
import datetime

# [X] Virtual Environment
# [X] Version

# [X] Printing
#              012345678910
# console.log("Hello World")

greeting = "Hello world!"
first_name = "Michael"
last_name = "Moulton"
age = 32


# print(greeting, "My name is ", first_name, last_name)
# print(greeting + "My name is " + first_name + last_name + ", I am " + str(age) + " years old")

# [X] f-strings
full_greeting = f"{greeting} My name is  {first_name}, {last_name}, I am {age} years old"

# [X] variables
# left side -> variable
# (address in memory)
#                         right side -> value (gets evaluated)
full_name = first_name + " " + last_name

# what your interpreter does to evaluate:
# full_name = "Michael" + " " + last_name
# full_name = "Michael" + " " + "Moulton"

# [X] Data Types

# [X] Primitive types
# boolean -> True False
# string

# float --> decimal
# int --> integer


# [X] Composite (data types that hold multiple values)
# lists == arrays

nums = [3, 4, 5, 6, 7]
nums[2] = 8

# key words -- types:
# list
# str
# int

# print()
# len()
# range()

# dictionaries == objects --> 
    # key /value pairs

user = {
    "first_name": "Kermit",
    "last_name": "the Frog",
    "SSN": 123456789
}

# print(user["first_name"])
# print(user[0]) # ERROR


users = [
    {
    "first_name": "Jim",
    "last_name": "Reeder",
    "SSN": 123456789
    },
    {
    "first_name": "Sadie",
    "last_name": "Flick",
    "SSN": 123456799
    }
]

# tuples --> (1, 2)

print(users[1]["first_name"])

# [X] whitespace
#   ---> scope within if statements, for loops, 
#        or other scopes, and later class definitions
#        require indentation - 
#   ---> must be either all same amount of spaces, 
#        or tabs. Cannot mix spaces and tabs.
#   ---> Note VS code inserts 4 spaces when you press tab.
isRaining = True
outDoors = False

# if isRaining:
#     print("Remember to take an umbrella!")

#     if outDoors:
#         print("Remember to take an umbrella!")
    
#     else:
#         print("you're good.")

# elif isFoggy:
#     print("wear a coat")

# else:
#     print("You're good, go ahead!")




# [X] Conditionals

# [X] Loops

#        start | stop (exclusive) |  step (increment or decrement)
#        Must be integers
# for i in range(1, 21, 1):
#     i = i - 1
#     print(i)
#     i += 20
#     print(i)

# var   |    val
#    i          1 (-> 0 -> 20)-> 2 

# terminal:
# 0
# 20

#  default step is 1
# for i in range(1, 21):
#     print(i)

# # default start 0, deafault step 1
# for i in range(21):
#     print(i)

# i = 1

# while i <= 20:
#     print(i)

#do more stuff

# [ ] Functions

# function do_stuff(arr) {
#     // do stuff
# }

def make_smoothie(fruits):
    # do stuff
    smoothie = ""
    
    for fruit in fruits:
        print(fruit)
        smoothie += fruit

        if len(smoothie) > 10:
            return smoothie
    

my_fruits = ['banana', 'durian', 'papaya', "apple", "peach"]
my_smoothie = make_smoothie(my_fruits)

print(my_smoothie)