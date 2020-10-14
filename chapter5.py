1#/usr/bin/env python3
print("Chapter 5: If Statements")
print('\n')

print("Exercise 1: Simple Statements")
# conditional test An expression which can be evaluated as True or False
family=['me','sophia','mom','dad']
print(family)
for member in family:
    print(member)
# An "if else" statment can be used to modify the actions of a loop by defining the conditions in which they will be performed
# if A statement which defines a conditional test and what to do if the condition is TRUE
# else A statement which defines what to do if the condition is FALSE
# The following "if" statement checks if the value of the element in the list "family" is "sophia"
# If the value is "sophia", the value is printed with the first letter capitalized
# If the value is NOT "sophia", the value is printed as is
for member in family:
    if member == ('sophia'):
        print(member.title())
    else:
        print(member)
print('\n')

print("Exercise 2: Checking for Equality")
print("Difference Between '=' and '==': Line 26")
# "=" A symbol which equates two items to eachother: both items are stored with the same value
# "==" A symbol which checks for equality and returns "True" or "False"
# "==" is case sensitive
# The following block checks if the values of "name" and the string "alex" are equal
#name = 'alex'
#name == 'alex'
#True
#name == 'blair'
#False
#name == 'Alex'
#False
print("Ignoring Case for Equality: Line 38")
# Because "==" is case sensitive, forcing the case of two values will allow "==" to check for equality
#name = 'Alex'
#name.lower() = 'alex'
#True
print('\n')

print("Exercise 3: Checking for Inequality")
# "=!" A symbol which checks if two items are NOT equal and returns "True" or "False"
name='Alexander'
print("Hey, "+name)
if name != 'Blair':
    print("You can just call me Blair")
print('\n')

print("Exercise 4: Numerical Comparisons")
# Numerical equality comparisons follow the same rules as string comparisons
print("What is 12+14?")
responses=[22, 24, 26]
for answer in responses:
    print(answer)
    if answer != 12+14:
        print("Sorry, that is incorrect...")
    else:
        print("Yes, that is correct!")
print('\n')

print("Exercise 5: Checking Multiple Conditions")
# Keywords can be used to combine conditional tests
# "and" A keyword requiring both conditional tests to return "True" for the whole conditional to return "True"
ages=[18, 22, 15]
for years in ages:
    print("How old are you?")
    print(years)
    if years >= 21 and years >= 18:
        print("Come on in!")
    elif years <= 21 and years >=18:
        print("You can come in, but you can't drink.")
    else:
        print("Come back when you're older...")
print('\n')
# "or" A keyword requiring one conditional test to return "True" for the whole conditional to return "True"
for years in ages:
    print("How old are you?")
    print(years)
    if years >=21 or years >= 18:
        print("Come on in!")
    else:
        print("Come back when you're older...")
print('\n')

print("Exercise 6: Checking for a Value in a List")
print('Using the "in" Keyword: Line 86')
# "in" A keyword requiring the first value to be exist within a list
guesses1=['john', 'james', 'jesse']
print("What's my name? You have 3 guesses")
print(guesses1)
if 'james' in guesses1:
    print("You guessed it!")
#  "not in" A keyword requiring a value to NOT exist within a list
guesses2=['adam', 'alex', 'amory']
print(guesses2)
if 'james' not in guesses2:
    print("Sorry, no dice!")
print('\n')

print("Exercise 7: if Statements")
# "if" A statement instructing an action following a conditional test
# "if-else" A series of statements instructing actions depending on a boolean test
# "Boolean Expression" A conditional tests returning True or False
on=True
print("Is the TV on?")
if on:
    print("Yes")
else:
    print("No")
on=False
print("\nIs the TV on?")
if on:
    print("Yes")
else:
    print("No")
# "if-elif-else" A series of statements instructing actions dependent on the results of multiple conditional tests
for years in ages:
    print("How old are you?")
    print(years)
    if years >= 21 and years >= 18:
        print("Come on in!")
    elif years <= 21 and years >=18:
        print("You can come in, but you can't drink.")
    else:
        print("Come back when you're older...")
# "elif" blocks can be used in series to allow more responses to more conditions
# Python does NOT require an "else" block at the end of an "elif" chain
# "elif" statement chains only require ONE "True" to finish its chain
# This means if multiple conditions require responses, they must be tested individually
# The following "elif" block will not add all the toppings because the "elif" chain is satisfied by the first test
toppings=['mushrooms', 'sausage', 'spinach']
print(toppings)
print("Additions to the order:")
if 'mushrooms' in toppings:
    print("Adding mushrooms")
elif 'sausage' in toppings:
    print("Adding sausage")
elif 'spinach' in toppings:
    print("Adding spinach")
print('\n')
# The following block will add all the toppings because each statement is evaluated individually
print(toppings)
if 'mushrooms' in toppings:
    print("Adding mushrooms")
if 'sausage' in toppings:
    print("Adding sausage")
if 'spinach' in toppings:
    print("Adding spinach")
print('\n')

print('Exercise 8: Using Lists with "if-else" statements')
# Lists can be more efficiently used by "if" statements if they are in a "for" statement
# Multiple lists can be used in one statement
in_stock=['mushrooms', 'sausage']
print("Please add "+toppings[0]+", "+toppings[1]+", and "+toppings[2])
for request in toppings:
    if request in in_stock:
        print("Adding "+request+".")
    elif request not in in_stock:
        print("Sorry, out of "+request+".")
print('\n')
# To check if a list is empty, do not provide conditionals for the "elif" statement
requests=[]
if requests:
    for topping in requests:
        print("Adding "+topping)
else:
    print("Plain? Really?")








