#1/usr/bin/env python3
print('Chapter 2: Variables and Simple Data')

# Exercise 1: Print Something
# A variable is an object stored as another object
# A string is any series of characters
# Python recognized anything within quotes as a string
# str() is the variable type for a String
message = "Hello Python World!"
print(message)

# Exercise 2: Print Something Else
message="Hello Phthon Crash Course World!"
print(message)

# Exercise 3: Generate and Correct an Error
# print(mesage)
mesage="Hello Python Crash Course Reader!"
print(mesage)

# Exercise 4: Change Case of a String
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Exercise 5: Concatenate a String
first_name="ada"
last_name="lovelace"
full_name=first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# Exercise 6: Changing Stored Variable
# Variables will store the most recent value attached to them
message = "Hello, " + full_name.title() + "!"
print(message)

# Exercise 7: Using Whitespace
print("Python")
# \t Adds an indentation
print("\tPython")
# \n Adds a new line
print("Languages:\nPython")
# Whitespace notations can be combined
print("Languages:\n\tPython\n\tHTML\n\tCSS")

# Exercies 8: Stripping Whitespace
# strip() Temporarily removes whitespace on the left and right sides of a string
fav_lang="python "
fav_lang
fav_lang.strip()
# Returns:
# 'python '
# 'python'
# lstrip() and r(strip) remove whitespace from the left and right side of a string, respectively
# To keep a changed variable, it must be stored again
fav_lang1="python"
print(fav_lang1)
print(fav_lang1.upper())
fav_lang1=fav_lang1.upper()
print(fav_lang1)

# Exercise 9: Quotes and Apostrophes
# Python usually uses " and ' interchangably, but if they are used in a string, it cannot tell where a quote begins and ends
# The following will return a syntax error because Python ends the quote at the first apostrophe, but the following text is not enclosed
#message='One of Python's strengths is its community.'
# The following is correct
message="One of Python's strengths is its community."
print(message)

# Exercise 10: Comments
# A comment is a series of characters ignored by the interpreter
# Comments are used to communicate or note information within the code of a file
# "#" is the symbol indicating a comment
# The following will be ignored
#print("Hello")
# The following will be used
print("Hello")
# "#" makes everything to the right of it a comment
# The following will return a syntax error because the comment also excludes the closing parenthesis
#print("Hello" #Everyone)

# Exercise 11: Math in Python
# Symbols can be used to for calculations
# + Add
# - Subtract
# * Multiply
# / Divide (This will return a float instead of an integer)
# ** Exponentiate
# Standard Order of Operations is observed in Python
# An integer is any number without a decimal point
# int() is the variable type for an Integer
# A float is any number with a decimal point
# float() is the variable type for a Float
print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2**3)
print(2+3*2)

# Exercise 12: Converting numbers to strings
# Python can print numbers
print(2+3*2**3)
# Python cannot concatenate strings and numbers together
# The following will return a syntax error because there are both a string and a number in the same statement
#print("2 + 3 * 2 ** 3 ="+(2+3*2**3))
# .str() Converts a number into a string
# The following is correct
print("2 + 3 * 2 ^ 3 = "+str(2+3*2**3))

# Closing Comments
# Beautiful is better than ugly
# Simple is better than complex
# Complex is better then complicated
# Readability matters
# There should be one, and only one, obvious way to do it
# Now is better than never

# Supplemental
# import is used to download data from directories in sys.path
# The following would search for and download "The Zen of Python.advice" if it is located in sys.path
#import The_Zen_of_Python.advice