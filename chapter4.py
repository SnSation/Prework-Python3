1#/usr/bin/env python3
print('Chapter 4: Working with Lists')
print('\n')

print('Exercise 1: Looping Through a List')
# Loops perform a task repeatedly until indicated to stop
# Loops are useful for working with dynamic elements
# for A statement which defines the following commands to executed in a loop
# Syntax for a "for" statement is "for", then the item to be worked with, then the location of the item, then (on a new line), the action to be performed
# A for statement used on a list will repeat the action until every element in the list has been used once
names=['blair', 'sophia', 'aeva']
for name in names:
    print(name)
print("'for' loop Syntax")
print("names=['blair', 'sophia', 'aeva']")
# The first section of a "for" loop defines what the target items are and where to store them
# The following line retrieves the first value from the list, "names", and store it in the variable "name"
print("for name in names:")
# The second section of a "for" loop provides instructions for the loop to execute
# The following line prints the stored value of the variable "name"
print("    print(name)")
# This process is repeated until all elements in the list, "names", have been printed
print('\n')

print('Exercise 2: Doing More Within a Loop')
for name in names:
    print(name.title()+", you're amazing!")
# Each line in the instructions represent a single action
# The loop will perform all indented instructions prior to restarting with the next variable
for name in names:
    print(name.title()+" you're amazing!")
    print("I love you so much!")
# New lines beyond the indented instuctions are NOT part of the loop and will only be performed once (like normal)
for name in names:
    print(name.title()+" you're amazing!")
    print("I love you so much!")
print("Goodbye, Everyone!")
print('\n')

print("Exercise 3: Indentation Errors")
print("Indentation Error Exercise: Line 42")
# Python uses indentation to determine which lines are connected to the line above it
# indentation error An error displayed an indented line is expected, but nonexistent
# The following block will retun an indentation error because python is expecting an indented block after the start of the "for" loop
#for name in names:
#print(name.title()+" you're amazing!")
#print("I love you so much!")
#print("Goodbye, Everyone!")
# logic error An error that is NOT displayed the code is valid, but does not perform as expected
# The following block will NOT return an error, but does NOT print "I love you so much!" after every name
for name in names:
    print(name.title()+" you're amazing!")
print("I love you so much!")
print("Goodbye, Everyone!")
print("Unnecessary Indentation Within the Loop: Line 56")
# unnecessary indentation an error displayed when a line is indented more than expected
# The following block will retun an unnecessary indentation error because the indentation in the instruction block doesn not match the loop's expected indentation
#for name in names:
#        print(name.title()+" you're amazing!")
#    print("I love you so much!")
#print("Goodbye, Everyone!")
# Unnecessary indentation after a loop will cause the line to be considered part of the loop
for name in names:
    print(name.title()+" you're amazing!")
    print("I love you so much!")
    print("Goodbye, Everyone!")
print('\n')

print("Exercise 4: Colon Errors")
print("Missing Colon Exercise: Line 71")
# the ":" indicates to interpret the following block as the loop instructions
# The following block returns a syntax error because a "for" loop requires a : to determine what the loop instructions are in
#for name in names
#    print(name.title()+" you're amazing!")
#    print("I love you so much!")
#    print("Goodbye, Everyone!"
print('\n')

print("Exercise 5: Making Numerical Lists")
# range() A function which generates a series of numbers
# The following block will print the values in the range of 1 through 4
for value in range(1,5):
    print(value)
# Returned values are often off by one because counting begins at the first value, but ends at the last value
# This means that the last value is never counted in a loop
# If output values are off by one, add 1 to the expected range
print('\n')

print("Exercise 6: Using range() to make a List")
# The return from "range()" can be converted into a list
numbers=list(range(1,6))
print(numbers)
# range() can bue modified to skip elements in a range
# The syntax for range() is the start of the range, then the end of the range, then how to count the range
evens=list(range(2,11,2))
print(evens)
# Example: range() used in a loop
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
print('\n')

print("Exercise 7: Simple Functions")
# min() A function which returns the smallest value in an item
# max() A function which returns the largest value in an item
# sum() A function which returns the sum of all values in an item
digits=[1,3,6,4,55,21,8]
print(min(digits))
print(max(digits))
print(sum(digits))

print("Exercise 8: List Comprehensions")
# list comprehension A combination of a "for" loop, the creation of new elements, and the appendation of those elements
# No ":" is used in a "for" loop used in a list comprehension
# List comprehension syntax: what you want to do with the results of the following statement(s) then a loop
exponents=[value**2 for value in range(1,11)]
print(exponents)
print('\n')

print("Exercise 9: Working with a List")
# slice A specific group of items within a list
# Note: Remember counting stops at the end of a range!
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters[3:6])
print(letters[:4])
print(letters[5:])
print("Here are the 3rd, 4th, and 5th letters of the alphabet:")
for letter in letters[2:5]:
    print(letter)
print("Here are those letters in a list:")
letter_list=[]
for letter in letters[2:5]:
    letter_list.append(letter)
print(letter_list)
# To copy a list, make a slice that includes the entire list by omitting the indices around the ":"
fruits=['apple', 'banana', 'orange', 'mango', 'pear']
print(fruits)
thefruits=fruits[:]
print(thefruits)
thefruits.append('guava')
print(fruits)
print(thefruits)
print('\n')

print("Exercise 10: Tuples")
# tuple A list that is immutable (can NOT be changed)
# A tuple is defined like a list except "()" are used instead of "[]"
rectangle=(50,200)
print(rectangle[0])
print(rectangle[1])
# The following block returns an error because values in a tuple can NOT be modified
#rectangle[0]=100
#print(rectangle[0])
# Tuple values can be overwritten if it is redefined
print("Rectangle 1")
for dimension in rectangle:
    print(dimension)
rectangle=(100,400)
print("Rectangle 2")
for dimension in rectangle:
    print(dimension)
print('\n')

print("Exercise 11: Style")
# style A set of conventions for the structure of code
# Following the same style guidelines allows one to understand another's code
print("Style Guice: Python Enhancement Protocol (PEP 8) is the most commonly used style guide")
print("Indentation: 1 Indentation = 4 Spaces")
print("Line Length: Python lines should be limited to 79 characters")
print("Comment Length: Python comments should be limited to 72 characters")
print("Blank Lines: A single blank line should be used to separate blocks of code with different functions")