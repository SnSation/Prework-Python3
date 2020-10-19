1#usr/bin/env python3

# Coding Temple Prework
# Python 102 - Task 3: Coding Questions

# Exercise 1
# Write a function to print "hello_USERNAME!"
# 'USERNAME' is the input of the function
# First line of code:
# def hello_name(user_name):

def hello_name(user_name):
    print("hello_" + user_name +"!")

hello_name("Aeva")

print("\n")
# Exercise 2
# Print the first 100 odd numbers in Python.

count = 0
while count <= 100:
    if count % 2 == 1 and count <= 100:
        print(count)
    count += 1

print('\n')
# Exercise 3
# Write a function to return the max number of a given list
# First line of code:
# def max_num_in_list(a_list):

def max_num_in_list(a_list):
    print("The largest number in the list is " + str(sorted(a_list).pop()) + ".")

max_list = [1, 2, 5, 77, 54, 23, 13, 65, 9]
max_num_in_list(max_list)

print('\n')
# Exercise 4
# Write a function to return if the given year is a leap year.
# A leap year is:
# - Divisible by 4
# - Not divisible by 100 UNLESS it is also divisble by 400
# The return should be a boolean Type
# First line of code:
# def is_leap_year(a_year):

def is_leap_year(a_year):
    if (a_year / 400).is_integer() == True:
        return True
    elif (a_year / 4).is_integer() == True and (a_year / 100).is_integer() == False:
        return True
    else:
        return False

print(is_leap_year(2005))
print(is_leap_year(3600))

print('\n')
# Exercise 5
# Write a function to check to see if all numbers in a list are consecutive
# First line of code:
# def is_consecutive(a_list):

def is_consecutive(a_list):
    consecutive = True
    list_length = len(a_list)-1
    for number in a_list[:(list_length)]:
        number_index = a_list.index(number)
        next_index = number_index + 1
        next_number = a_list[next_index]
        if number + 1 != next_number:
            consecutive = False
    return consecutive

consecutive_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
consecutive_list2 = [55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
nonconsecutive_list = [1, 2, 3, 4, 6, 8, 10, 11]

print(is_consecutive(consecutive_list))
print(is_consecutive(consecutive_list2))
print(is_consecutive(nonconsecutive_list))