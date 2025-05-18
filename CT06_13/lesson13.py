# print("Hello from lesson 13")

Groceries = [
    "Apples",
    "Bread",
    "Carrots",
    "Dates",
    "Eggs",
    "Flour",
    "Grapes",
    "Honey"
]

Groceries[7] = "Herb"

Groceries.append("Ice")
Groceries.insert(1, "Banana")
Groceries.pop(2)

print(Groceries)    
# Task 2: List of groceries (part 2)
# 1. Use a 'for' loop and print out all the groceries on your list
# 2. If grocery == "Apples", print "<grocery name>: I need 5 of these"
# 3. If grocery == "Carrots", print "<grocery name>: I need 3 of
#    these"
# 4. If name == "Grapes", print "<grocery name>: Get the FarmFresh
#    brand"

for grocery in Groceries:
    if grocery == "Apples":
        print( grocery + " I need 5 of these")
    elif grocery == "Carrots":
        print(grocery + " I need 3 of these")
    elif grocery == "Grapes":
        print(grocery + " Get the FramFresh brand")
    else:
        print(grocery)


# Task 4: Online Catalogue
# **Task 4a**:
# Write a program to create an online catalogue for a grocery store.

# 1. Using a 'while' loop, ask the user (grocery store manager) to
#    input the items their online catalogue should have.
# 3. Add each item into the catalogue list
# 4. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the grocery store manager, do the
# following:

# 1. Imagine a customer browsing the website of the grocery store.
#    Ask the customer: "What are you looking for?"
# 2. If the item is in the list, say "Yes we sell that."
# 3. Else, say "Sorry, we don't have that."


item = []
while True:
    user = input("What would you like to add to the store? ")
    if user == "end":
        break
    else:
        item.append(user)
    print(item)


ask = input("Hello, what are you looking for? ")

if ask in item:
    print("We have that")
else:
    print("Sorry we do not have")










































































