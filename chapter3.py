#1/usr/bin/env python3
print('Chapter 3: Introducing Lists')

print('Exercise 1: Simple Lists')
# A list is a collection of elements in a particular order
# [] indicate a list
# , separates individual elements in a list
numbers=['one', 'two', 'three', 'four', 'five']
print(numbers)
# Lists can be empty
empty_list=[]
print(empty_list)

print('\n')
print('Exercise 2: Access Items in a List')
# Elements in a list are accessed by their index
# The index is an item's position in a list
# Index numbers start with 0 corresponding to the first item in the list
print(numbers[0])
print(numbers[1:3])
# List elements can be modified
print(numbers[2].title())
# Index numbers can also go backwards with negative numbers, starting with -1
print(numbers[-1])
print('\n')

print('Exercise 3: Use List Elements')
# List elements are variables
message="My favorite number is "+numbers[4].title()+"."
print(message)
print('\n')

print('Exercise 4: Replacing List Elements')
print('\n')
# List modification syntax requires the listname, then the index, then the element, then the new value
names=['alex', 'sophia', 'aeva', 'mom', 'dad']
print(names)
names[3]='kristina'
print(names)
print('\n')

print('Exercise 5: Adding List Elements')
# .append Appends item(s) to the list
names.append('brother')
print(names)
# New list elements can be inserted into specific positons by specifying the desired index number for the inserted item
# .insert Inserts items into a list at the specified index
names.insert(5, 'sister')
print(names)
print('\n')

print('Exercise 6: Removing List Elements')
# List elements can be deleted from a list with the "del" statement
# del A statement used to delete or remove an item
# Changes using del are permanent and global
del names[5]
print(names)
del names[3:]
print(names)
# List elements can be removed from the list to be used elsewhere
# pop() A method that removes elements from a list by its index
# Without an index value, "pop()" will use the last item in the list
# Removed list elements can be stored as a new variable
weekdays=['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']
print(weekdays)
pop_weekdays=weekdays.pop()
print(pop_weekdays)
pop_thursday=weekdays.pop(3)
print(pop_thursday)
# Removed elements are NOT returned to the original list
print(weekdays)
# List elements can be removed by their value
# remove() A method that removes an element from a list by its value
directions=['up', 'down', 'left', 'right', 'inward', 'outward']
print(directions)
duck='down'
directions.remove(duck)
print(directions)
print('Always duck '+ duck +'.')
# While a single list element may be a string, a list is not actually a string
# The following will return an error becuase python is attempting to print an item that is not a string
#print('\ntNever duck '+ directions +'.')
print('\n')

print('Exercise 7: Organize a List')
# sort() A method which rearranges a list
# sort() Rearranges alphabetically with no modifiers
# Changes using sort() are permanent and global
colors=['red', 'blue', 'yellow', 'green', 'cyan', 'magenta']
print(colors)
colors.sort()
print(colors)
# sort() can be modified
colors.sort(reverse=True)
print(colors)
# sorted() A method which rearranges a list for use elsewhere
# sorted() does preserves the original list order
print('Original List')
cars=['bmw', 'audi', 'volkswagon', 'toyota', 'ford']
print(cars)
print('print(sorted(cars))')
print(sorted(cars))
print('print(cars)')
print(cars)
# reverse() A method which reverses the order of a list
# reverse() uses elements' index
# Changes using reverse() are permanent and global
cars.reverse()
print(cars)
# Changes using reverse() can be reverted by using reverse() again
cars.reverse()
print(cars)
print('\n')

print('Exercise 8: Finding List Length')
# len() A function which returns the number of elements in a list
print(len(cars))
print('\n')

print('Exercise 9: Index Errors')
# Python will return an error if it cannot find an element with the specified index or value
# The following will return an index error because there is no item with an index value of 4 or above
#book_title=['to', 'kill', 'a', 'mockingbird']
#print(book_title[4])

