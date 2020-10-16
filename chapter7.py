1#/usr/bin/env python3
print("Chapter 7: User Input and While Loops")
print("\tNote:\n\tMany blocks from this chapter will be commented out\n\tView code for exercises")
print('\n')

print("Exercise 1: The input() Function")
# "input" Data sent TO something
# "output" Data sent FROM something
# "input()" A function which pauses the program and waits for user input and stores it as a varaible
# input() interprets ALL user input as a string
# "prompt" Instructions for input()

# Example:
#message=input("Say Something:\n")
#print(message)


# Prompts can be stored in a variable for later use
# "Multi-Line String" A single string made up of multiple strings from different lines
# "+=" An operator which appends its input to the variable

# Example:
#prompt = "If you tell us your name, we can send you a personalized message."
#print(prompt)
#prompt += "\nWhat is your name?\n"
#print(prompt)
#name = input(prompt)
#print("\nHello, "+ name + "!")

print('\n')

print("Exercise 2: The int() Function")
# Because python interprets input as a string, numbers would be stored as a string, rather than in integer or float
# The following block returns an error because the input has been stored as a string,
# therefore, math operators cannot be used on it

# Example:
#size = input("How big is it?")
#print(size)
#halfsize = size / 2
#print(halfsize)

# "int()" A function which treats input as a number
# Example:
#size = input("How big is it?\n")
#size = int(size)
#halfsize = size / 2
#print(halfsize)

# Remember: numbers and strings cannot concatente
# Numbers must be converted into strings to be used with other strings
# Example
#if size >= 20:
#    print("\n"+str(size)+"? "+ "That's too big!")
#elif size <= 5:
#    print("\n"+str(size)+"? "+ "\nThat's too small!")
#else:
#    print("\n"+str(size)+"? "+ "\nThat's just right!")

# "%" (Modulo) An operator which divides and returns the remainder
# Example
#print("4 / 3")
#division = 4 / 3
#print(division)
#print("4 % 3")
#modulo = 4 % 3
#print(modulo)
# % is a convenient way to check if numbers are even
# Example
#even_or_odd = input("Which number would you like to check?\n")
#even_or_odd=int(even_or_odd)
#if even_or_odd % 2 == 0:
#    print("\n" + str(even_or_odd) + " is even.")
#else:
#    print("\n" + str(even_or_odd) + " is odd.")
print('\n')

print("Exercise 3: while Loops")
# "while" a loop function which continuously executes a block of code while the condition is True
#current_number = 1
#while current_number <= 5:
#    print(current_number)
#    current_number += 1
# while loops can be adjusted while the program is running
# Example
#prompt = "\nI can't stop..."
#prompt += "\nunless you say the magic word\n"
#stop_it = ""
#while stop_it != 'stop':
#    stop_it = input(prompt).lower()
#    if stop_it != 'stop':
#        print("That's not the right word!")
# Without a way to stop the while loop, it will loop infinitely and will crash the program
# "flag" A condition which sets its on condition based on the condition of other conditions
# A flag can require multiple conditions to return true before it sets its own condition to False
#active = True
#while active:
#    word=input(prompt).lower()
#    
#    if word == 'please':
#        print("\nThat's it!")
#        active = False
#    else:
#        print("\nThe magic word isn't " + word + ".\nWho raised you?")
print('\n')

print("Exercise 4: Exiting a Loop")
# "break" A statement which ends a loop
# Example:
#prompt = "\nWhat cities have you visited?"
#prompt += "\nEnter 'DONE' when you're finished\n"
#unfinished = True
#visited=[]
#while unfinished:
#    city = input(prompt).title()
#
#    if city.lower() == 'quit':
#        break
#    elif city.lower() == 'done':
#        print("So you've been to " + str(visited) + "?")
#        unfinished = False
#    else:
#        visited.append(city)
#        print("Have you been anywhere else?")

# "continue" A statement which restarts a loop
# Example:
# The following block counts from 0 to 9
# After each count, 1 is added to the counter
# The count is then divided by 2, and if the remainder is 0,
# the loop hits a "continue" statement, which starts the loop again
# If the remainder is 1, the number is printed
#current_count = 0
#while current_count < 10:
#    current_count += 1
#    if current_count % 2 == 0:
#        continue

#    print(current_count)
#
# "infinite loop" A loop in which there is no way to set the condition to False
# Example:
# The following code, if run, would continue forever
# This is because there is no way to change the condition to False
#x = 1
#while x <= 5:
#    print(x)
print('\n')

print("Exercise 5: Using Loops with Lists")
# Loops can be used to manipulate lists
# Example
#unconfirmed_users = ['alex', 'blair', 'sophia', 'klussi']
#confirmed_users = []
#
#while unconfirmed_users:
#    current_user = unconfirmed_users.pop(0)
#    verification = "\nCan you verify " + current_user.title() + "?\n"
#    confirmation = input(verification).lower()
#    
#    if confirmation == 'yes':
#        confirmed_users.append(current_user)
#        print(str(len(confirmed_users)) + " users confirmed.")
#    else:
#        unconfirmed_users.append(current_user)
#        print(str(unconfirmed_users) + " remains unconfirmed.")
#
# Example
#numbers = [1, 1, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8]
#while 1 in numbers:
#    numbers.remove(1)
#print(numbers)
print('\n')

print("Exercise 6: Filling a Dictionary with User Input")
# A prompt can keep requesting user input as long as a while loop is running
# Example
responses = {}

questioning = True

while questioning:
    name = input("\nWhat is your name?\n")
    origin = input("\nWhere are you from?\n")

    responses[name] = origin
    repeating = True
    while repeating:
        repeat = input("Is there anyone else to ask?\n")
        if repeat.lower() == 'no':
            print("\nResults:\n")
            for name, origin in responses.items():
                print(name + " is from " + origin + ".")
                repeating = False
            questioning = False
        elif repeat.lower() == 'yes':
            repeating = False
        elif repeat.lower() != 'yes':
            print("I'm sorry, I didn't understand that answer")







