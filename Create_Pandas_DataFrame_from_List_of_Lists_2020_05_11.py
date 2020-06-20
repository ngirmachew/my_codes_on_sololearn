import pandas as pd
# Given: 
"""
['Lagos', '1,845', '1,343', '469', '33'] 
['Kano', '602', '528', '48', '26'] 
['FCT', '356', '297', '53', '6']
['Borno', '185', '157', '12', '16']
"""
# Create a list of lists and/or a Pandas DataFrame:
# 1. List of Lists: -> Just zip them all and turn each into a list within a list comprehension:
list_of_lists = [list(lst) for lst in zip(['Lagos', '1,845', '1,343', '469', '33'], ['Kano', '602', '528', '48', '26'], ['FCT', '356', '297', '53', '6'], ['Borno', '185', '157', '12', '16'])]
print("*" * 30)
print(f"Here is the list of lists:\n\t{list_of_lists}")

# 2. Use that list of lists to create a dataframe with the cities as columns:
df = pd.DataFrame.from_records(list_of_lists[1:], columns = list_of_lists[0])
print("*" * 30)
print(f"Here is the dataFrame:\n{df}")
print("*" * 30)