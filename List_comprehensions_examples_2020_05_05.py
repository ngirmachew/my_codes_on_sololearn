# Some list comrehension examples:

# General form: [EXPRESSION/VARIABLE for VARIABLE in SEQUENCE]

# Example 0:

name = "Dangote" # The source SEQUENCE

spelling = [letter for letter in name] # letter before the for key word is the EXPRESSION, the letter after for is the VARIABLE and name is the source SEQUENCE

print(f"Is this how you spell your name, Mr. {name}?: {spelling}")

# Example 1:

evens = [2, 4, 6, 8, 10, 12] # The source SEQUENCE

evens_squared = [x * x for x in evens] # x*x is the EXPRESSION, the x after for is the VARIABLE and evens is the source SEQUENCE

print(f"Evens: {evens}\nEvens Squared: {evens_squared}")

# Example 2:
pets = ["cat", "dog", "hamster", "rabbit", "parakeet"] # The source SEQUENCE

the_pets = ["The crazy " + pet for pet in pets] # "The crazy " + pet is the EXPRESSION, the pet after for is the VARIABLE and pets is the source SEQUENCE

print(f"Pets: {pets}\nThe crazy pets: {the_pets}")

# with condition: [EXPRESSION/VARIABLE for VARIABLE in SEQUENCE if CONDITION]

# Example 3: 
ages = [25, 20, 34, 65, 43, 12, 87, 14] # The source SEQUENCE

can_purchase_alcohol = [age for age in ages if age >= 21] # age (before the key word for) is the EXPRESSION, which just happens to be the variable itself, the age after for is the VARIABLE, ages is the source SEQUENCE, and if age >= 21 is the CONDITION

print(f"Here is the list of ages allowed to purchase alcohol at our store: {can_purchase_alcohol}")