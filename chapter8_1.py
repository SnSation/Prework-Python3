1#/urs/bin/env python3
def pizza(crust, *toppings):
    additions = ""
    for topping in toppings:
        additions += '\n' + topping
    print(crust.title() + " crust pizza with:" + additions)
