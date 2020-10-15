1#/usr/bin/env python3
print("Chapter 6: Dictionaries")
print('\n')

print("Exercise 1:  Working with Dictionaries")
# "Dictionary" A collection of key-value pairs
# Dictionaries store and connect pieces of related information
# "Key-Value Pair" A pair of values in which the "key" is used to access the "value"
# A key's value can be any object recognized by python3 (number, string, dictionary, etc.)
# The syntax for a dictionary is a variable followed by - in bracce - the key, ":", and the values (separated by commas)
# The following is a simple dictionary, with just 1 key-value pair, in which "breed" is they key and "labrador" is the value
# When the key is called, this dictionary will return the values associated with the key
dogs={'breed':'labrador'}
print(dogs['breed'])
# Any number of key-value pairs can be stored in a dictionary
# The following block is a dictionary with 2 key-value pairs
targets1={'size':'small','points':9}
print(targets1['size'])
print(targets1['points'])
print('\n')

print("Exercise 2: Accessing Values in a Dictionary")
# Individual key-value pairs can be stored in variables
points_earned=targets1['points']
print("Small target shot!")
print("you earned "+str(points_earned)+" points!")
print('\n')

print("Exercise 3: Modifying Values in a Dictionary")
# To add a new key-value pair, write the name of the dictionary followed by the new pair in square brackets
print(targets1)
targets1['x_pos']=0
targets1['y_pos']=25
print(targets1)
print('\n')
# Dictionaries can be empty
targets2={}
targets2['size']='small'
targets2['points']=25
print(targets2)
print('\n')
# Dictionary values can be modified by the same process as adding a key-value pair
targets1['size']='small'
targets1['points']=25
targets1['speed']='fast'
targets2['size']='large'
targets2['speed']='slow'
targets2['points']=10
targets2['x_pos']=25
targets2['y_pos']=50
print(targets1)
print(targets2)
# Combined with loops, dictionaries can be updated on their own
if targets1['speed']=='slow':
    x_increment=1
elif targets1['speed']=='medium':
    x_increment=2
elif targets1['speed']=='fast':
    x_increment=3

targets1['x_pos']=targets1['x_pos']+x_increment
print("New x_pos: "+str(targets1["x_pos"]))
# Key-value pairs can be removed with the "del" statement
# Remember: Changes made with the del statement are permanent
del targets1['points']
print(targets1)
print('\n')

print("Exercise 4: Dictionaries with Similar Objects")
# Results with similar information can be stored in dictionaries
# Dictionaries can be written over multiple lines
# Any informaton inside the brace will be considered part of the dictionary
# The style guide requires an indentation for key-value pairs on new lines of a dictionary and the closing brace on its own line
animal_sounds={
    'dog':'woof',
    'cat':'mew',
    'duck':'quack',
    'rabbit':'...',
}
print('The dog goes "'+str(animal_sounds['dog']+'".'))
print('\n')

print("Exercise 5: Looping with Keys")
# ".items()" A method which returns individual values in an item
# In this case, the items are the key-value pairs
user1={
    'username':'sns',
    'first_name':'alex',
    'last_name':'blair',
}
for key, value in user1.items():
    print('\nKey: '+key)
    print('Value: '+value)
# Because we defined the variables "key" and "value" in our for loop,
# the first element of the "users1" is assigned to the "key" variable,
# and the second element is assigned to the "value" variable
# The following block returns an error because there are only two elements in each item
# for which to assign to a variable
#for a, b, c in user1.items():
#    print('\na: '+a)
#    print('b: '+b)
#    print('c: '+c)
for animal, sound in animal_sounds.items():
    print('The '+animal+' goes '+sound+'.')
# "keys()" A method which returns the keys of a dictionary
for animal in animal_sounds.keys():
    print(animal)
print('\n')
# Note: The keys() method is the default behavior when calling a dictionary
# The style guide recommends adding the keys() method for readability
# The following code will behave exactly the same as the above code
for animal in animal_sounds:
    print(animal)
print('\n')
# To only work with specific keys, make sure to use the keys() method in your loop
domestic=['dog','cat']
exotic=['duck','rabbit']
animal_sounds['eagle']='caw'
for animal in animal_sounds.keys():
    print(animal.title())
    if animal in domestic:
        print("The "+animal+" is a domestic pet.")
    elif animal in exotic:
        print("The "+animal+" is an exotic pet.")
    elif animal not in domestic or exotic:
        print("The "+animal+" is not a pet.")
print('\n')
# If data is added to a dictionary in differing orders,
# dictionaries that work together may not function as expected
targets1['points']=25
print(targets1.keys())
print(targets2.keys())
print(sorted(targets1.keys()))
print(sorted(targets2.keys()))
print('\n')

print("Exercise 6: Looping with Values")
# "values()" A method which returns the values in a dictionary
print(animal_sounds.values())
for sound in animal_sounds.values():
    print("What animal makes the "+sound+" sound?")
print('\n')
# the values() method does NOT check for repeating values
# "set" A list-like object where each value must be unique
animal_sounds['wolf']='woof'
for sound in animal_sounds.values():
    print("An animal can make the "+sound+" sound.")
print('\n')
print("If we make 'animal_sounds' a set, only unique values are used")
for sound in set(animal_sounds.values()):
    print("An animal can make the "+sound+" sound.")
print('\n')

print("Exercist 7: Nesting")
# "nesting" When a list, set, or dictionary stored as a value in another list, set, or dictionary
# The following block nests dictionaries in a list
small_target=targets1
large_target=targets2
targets3={
    'size':'medium',
    'points':15,
    'speed':'average',
    'x_pos':25,
    'y_pos':100,
}
medium_target=targets3
print(small_target)
print(medium_target)
print(large_target)
print('\n')
targets=[small_target, medium_target, large_target]
for goal in targets:
    print(goal)
print('\n')
targets=[]
print(targets)
# Generate Targets
for target_number in range(30):
    new_target={
        'size':'small',
        'points':25,
        'speed':'fast',
    }
    targets.append(new_target)
print('\n')
for target in targets[:5]:
    print(target)
print("Total Targets Generated: "+str(len(targets)))
# The generated dictionaries (new_target) may be equal to each other,
# but python3 treats each one as a separate object
# Because of this, they can be modified, individually
for target in targets[5:]:
    if target['size']=='small':
        target['size']='medium'
        target['speed']='average'
        target['points']=15
for target in targets[15:30]:
    if target['size']!='large':
        target['size']='large'
        target['speed']='slow'
        target['points']=10
target_number=1
for target in targets:
    print(str(target_number)+":")
    print(target)
    target_number=target_number+1
print('\n')
# Lists can be nested in dictionaries
pizza={
    'crust':['thin','thick'],
    'topping':['onion','mushroom','sausage','spinach']
}
print("Pizza Choices:\nCrust Types: "+str(pizza['crust'])+'\n'+"Toppings: "+str(pizza['topping']))
print('\n')
print("Pizza Combinations:\n")
for category, selection in pizza.items():
    print(category.title()+" Types:")
    if category == 'crust':
        print(selection)
    elif category == 'topping':
        print(selection)
print('\n')
# Dictionaries can be nested in dictionaries
users={
    'bigboy12': {
        'first':'david',
        'last':'barnett',
        'location':'new york',
    },
    'lilgirl43': {
        'first':'amy',
        'last':'charleston',
        'location':'illinois',
    },
    'mamabear': {
        'first':'karen',
        'last':'manager',
        'location':'shopping mall',
    },
}
for username, user_info in users.items():
    print("\nUsername: "+username)
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']
    print("\tFull Name: "+full_name.title())
    print("\tLocaion: "+location.title())