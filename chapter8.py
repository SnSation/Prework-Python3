1#usr/bin/env python3
print("Chapter 8: Functions")

print("Exercise 1: Defining a Function")
# "function" A named block of code designe to do one job
# "call" When a function is asked to do a job
# "def" A keyword which defines a function
# Example
def greet():
    """Display a greeting."""
    print("Hello!")

greet()
# The parentheses hold information required by the function
# If the fuction does not require information, parentheses are still needed
# "function definition" The line in which "def" is in
# "body" The indented instructions after the function definition
print('\n')

print("Exercise 2: Passing Information to a Function")
# Data to be used by the function is entered within its parentheses
# Example:
def greet2(person):
    # Display a greeting with a person's name
    print("Nice to meet you, " + person.title() + "!")

greet2('james')
#introduction = input("\nWhat is your name?\n")
#greet2(introduction)

# "parameter" A piece of data function requires to work
# Parameters are created when a function is defined
# "argument" A piece of data passed to a function from a call
# Arguments are the variables which replace parameters when a function is called
# Example
def my_function(my_parameter):
    print("Function Variable: " + my_parameter + '\n')

print("def my_function(my_parameter):\n\tprint('Function Variable: ' + my_parameter)")
print("my_argument = 'my_variable'")
my_argument = 'my_variable'
print("my_function(my_argument)")
my_function(my_argument)

# "positional arguments" Arguments matched to the parameters of a function by their order
# Example
def describe_pet(animal_type, pet_name):
    # Display Pet Information
    print("Your " + animal_type.lower() + "'s name is " + pet_name.title() + ".")

#a_type = input("\nWhat kind of pet do you have?\n")
#p_name = input("\nWhat is your pet's name?\n")

#describe_pet(a_type, p_name)

# "keyword argument" A key-value pair passed to a function
# Keyword arguments allow the freedom to ignore order in a function call
# Example:
# The both blocks reverse the order in which arguments are passed to the function
print("Positional Arguments:\n1: 'Aeva', 'Dog'\n2: 'Dog', 'Aeva'")
describe_pet('Aeva', 'Dog')
describe_pet('Dog', 'Aeva')
print("Keyword Arguments:\n1: 'Aeva', 'Dog'\n2: 'Dog', 'Aeva'")
describe_pet(pet_name = 'Aeva', animal_type = 'Dog')
describe_pet
describe_pet(animal_type = 'Dog', pet_name = 'Aeva')
describe_pet
print('\n')
# "default value" A value used for a parameter should an argument not be provided
# Default values are created when a function is defined like a keyword argument
# Parameters with default values can NOT come before parameters without default values
# Example
def describe_pet2(pet_name, animal_type = 'dog'):
    print("The " + animal_type.lower() + "'s name is " + pet_name.title() + ".")
describe_pet2(pet_name = 'aeva')
describe_pet2('aeva')
describe_pet2('sophia', 'human')
# Default values are overwritten if arguments are explicitly passed to them
print('\n')

print("Exercise 3: Argument Errors")
# "unmatched arguments" An error that occurs when too few or too many arguments are passed to a function
# Example:
# The following block will return an error because
# there are not as many arguments as parameters, and no default values to fill in the rest
def describe_pet3(pet_name, pet_type, pet_age):
    print("The " + str(pet_age) + " year old " + pet_type + " is named " + pet_name.title() + ".")

#describe_pet3('aeva', 'dog')
# The following block will return an error because
# there are more arguments passed to the function than parameters
#describe_pet3('aeva', 'dog', 9 , 'colorado')

print('\n')

print("Exercise 4: Return Values")
# "return value" The value returned by a function
# Return values are not restricted to the direct output of a function
# "return" A statement which sends data from within the function to the line that called the function
# Example:
def get_formatted_name(first_name, last_name):
    # Return a Full Name, Formatted Properly
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# In the previous block, 
# 1: "get_formatted_name" is defined
# 2: "musician" calls get_formatted_name with arguments: 'jimi' and 'hendrix'
# 3: get_formatted_name stores "jimi hendrix" in the variable "full_name"
# 4: get_formatted_name returns (sends) the output of "full_name.title()" to the varaible "musician"
# get_formatted_name doesn't actually have any output of its own

print('\n')

print("Exercise 5: Optional Arguments")
# The following function will return errors if a middle name is not passed it
def get_formatted_name2(first_name, middle_name, last_name):
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

# To make arguments optional, if-else statements and default values must be written into the function
def get_formatted_name3(first_name, last_name , middle_name = " "):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician2 = get_formatted_name3('jimi', 'hendrix')
print(musician2)
musician3 = get_formatted_name3('john', 'riley', 'c')
print(musician3)

print('\n')

print("Exercise 6: Returning a Dictionary")
# The following block creates a function that returns dictionaries generated with the arguments provided
def build_person(first_name, last_name):
    person = {
        'first' : first_name,
        'last' : last_name,
    }
    return person

friend = build_person('sophia', 'klussi')
print(friend)
# Example:
def build_person2(first_name, last_name, age = ""):
    person = {
        'first' : first_name,
        'last' : last_name,
    }
    if age:
        person['age'] = age
    return person

friend2 = build_person2('alex', 'blair', age = 29)
print(friend2)
friend3 = build_person2('aeva', 'darling')
print(friend3)

print('\n')

print("Exercise 7: Functions and while Loops")
# Example
#example_flag = True
example_flag = False
while example_flag:
    f_name = input("What is your first name?\n")
    l_name = input("What is your last name?\n")
    m_name = input("What is your middle name?\n")

    formatted_name = get_formatted_name3(f_name, l_name, m_name)
    print("\nHello, " + formatted_name + "!")
    
    repeating = True
    while repeating:
        again = input("\nIs there another name you would like to use?\n")

        if again.lower() == 'no':
            print("OK, talk to you later!")
            example_flag = False
            repeating = False
        elif again.lower() != 'yes':
            print("I'm sorry, I didn't understand that.")
            continue
        else:
            repeating = False

print("\nExercise 8: Functions and Lists")
# Example
absences = []
def attendance(students):
    # Print the roll call
    for name, status in students.items():
        if status == 'present':
            print(name.title() + " is here.")
        else:
            print(name.title() + " is out.")
            absences.append(name)
            if absences.count(name) >= 3:
                print("\t" + name.title() + " gets detention!")
                while name in absences:
                    absences.remove(name)

print("\nRoll Call:\n")
roll_call = {
    'adam' : 'present',
    'eve' : 'present',
    'god' : 'absent',
    'satan' : 'absent',
    'charlie' : 'present',
    'karen' : 'absent',
}
attendance(roll_call)

print("\nRoll Call 2:\n")
roll_call2 = {
    'adam' : 'present',
    'eve' : 'present',
    'god' : 'absent',
    'satan' : 'absent',
    'charlie' : 'absent',
    'karen' : 'absent',
}
attendance(roll_call2)

print("\nRoll Call 3:\n")
roll_call3 = {
    'adam' : 'present',
    'eve' : 'present',
    'god' : 'absent',
    'satan' : 'absent',
    'charlie' : 'present',
    'karen' : 'present',
}
attendance(roll_call3)

print("\nRoll Call 4:\n")
roll_call4 = {
    'adam' : 'present',
    'eve' : 'present',
    'god' : 'absent',
    'satan' : 'absent',
    'charlie' : 'present',
    'karen' : 'absent',
}
attendance(roll_call4)

print("\nRoll Call 5:\n")
roll_call5 = {
    'adam' : 'present',
    'eve' : 'present',
    'god' : 'absent',
    'satan' : 'absent',
    'charlie' : 'present',
    'karen' : 'absent',
}
attendance(roll_call5)

print("\nRoll Call 6:\n")
roll_call6 = {
    'adam' : 'present',
    'eve' : 'present',
    'god' : 'absent',
    'satan' : 'absent',
    'charlie' : 'present',
    'karen' : 'absent',
}
attendance(roll_call6)

print("\nRoll Call 7:\n")
roll_call7 = {
    'adam' : 'present',
    'eve' : 'present',
    'god' : 'absent',
    'satan' : 'absent',
    'charlie' : 'present',
    'karen' : 'absent',
}
attendance(roll_call7)

print("\nRoll Call 8:\n")
roll_call8 = {
    'adam' : 'present',
    'eve' : 'present',
    'god' : 'absent',
    'satan' : 'absent',
    'charlie' : 'present',
    'karen' : 'absent',
}
attendance(roll_call8)

print("\nExercise 9: Passing Arbitrary Arguments")
# "arbitrary argument" A parameter which accepts any number of arguments
# "*" A modifier which indicates the parameter is an arbitrary argument
# Example
def make_pizza(*toppings):
    # Print the toppings
    print(toppings)

make_pizza("pepperoni")
make_pizza("spinach", "mushroom", "garlic")
print('\n')
# Example
def make_pizza2(*toppings):
    # Print the toppings
    for topping in toppings:
        print("- " + topping)

print("Pizza 1:")
make_pizza2("pepperoni")
print("\nPizza 2:")
make_pizza2("spinach", "mushroom", "garlic")
# Python matches positional arguments, then keyword arguments, then arbitrary arguments in order
# Example
def make_pizza3(crust, *toppings):
    topping_list = ""
    for topping in toppings:
        topping_list += " | " + topping

    print(crust.title() + " crust pizza with:" + topping_list + ".")

print("Pizza 3 - 1")
make_pizza3('thin', 'pepperoni')
print("\nPizza 3 - 2")
make_pizza3('thick', 'sardines', 'garlic', 'jalepeno')
print('\n')

# "arbitrary keyword" A parameter which accepts any number of key-value pairs as its arguments
# "**" A modifier which indicates a parameter is an arbitrary keyword
# Example
profiles = {}
def store_profile(name, profile):
    profiles[name] = profile

def profiler(first, last, **info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    stats = ""
    for category, detail in info.items():
        profile[category] = detail
        stats += str(category).title() + ": " + str(detail).title() + "\n"
    name = first + " " + last
    information = name.title() +'\n' + stats
    store_profile(name.title(), profile)
    return information

user_profile = profiler('alex', 'blair',
                        location = 'chicago',
                        age = 29,
                        weight = 143,
                        status = "in relationship")
print(user_profile)
print(profiles['Alex Blair'])

print("Exercise 10: Modules")
# "module" A function stored in a separate file
# "import" A statement which makes code in a module available in the current file
# Imported functons need to be called using dot notation
# "dot notation" When the module is called with the desired function attached as a method
# Example:
#import chapter8_1

#chapter8_1.pizza('thick', 'pepperoni')
#chapter8_1.pizza('thin', 'snake', 'scorpion', 'shark')

# If the entire module is not required, specific functions can be imported instead
# "from" A statement which indicates which module to search for what you want to import
# Example
#from chapter8_1 import pizza

#pizza('thick', 'pepperoni')
#pizza('thin', 'snake', 'scorpion', 'shark')

# Module functions can also be given an alias
# "as" A statement which assigns an alias to an item
# Example
#from chapter8_1 import pizza as gogogadget

#gogogadget('steel', 'gears', 'sprockets', 'springs')

# All functions can be imported at once using the "*" operator
# Functions imported this way no longer need to use dot notaton
# Example:
from chapter8_1 import *

pizza('wood', 'leaves', 'branches', 'flowers')



