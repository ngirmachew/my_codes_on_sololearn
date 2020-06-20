
# Given the following pattern dict:
given_pattern_dict = {2 : 6, 3 : 12, 4 : 20, 5 : 30, 6 : 42}
# Solve  for 9 as a new key to be added to the given_pattern_dict

# Looking at the given_pattern_dict, printed as:
for k, v in given_pattern_dict.items():
    print(f"{k} -> {v}")

"""
    2 -> 6
    3 -> 12
    4 -> 20
    5 -> 30
    6 -> 42
"""
# One can easily see that each value of the (key, value) pair of the given_pattern_dict is arrived at by multiplying the key by key + 1, i.e. value = key * (key + 1)
"""
    2 -> 6  -> 2 * (2 + 1)
    3 -> 12 -> 3 * (3 + 1)
    4 -> 20 -> 4 * (4 + 1)
    5 -> 30 -> 5 * (5 + 1)
    6 -> 42 -> 6 * (6 + 1)
    Hence:
    7 -> 56 -> 7 * (7 + 1)
    8 -> 72 -> 8 * (8 + 1)
    9 -> 90 -> 9 * (9 + 1)
"""

# Thus, turning this into a python funciton could look like:
def next_pair(new_key):
    new_value = new_key * (new_key + 1)
    given_pattern_dict[new_key] = new_value
    print(f"{new_key} would be paired with {new_value}.")
    print(f"The Dict:\n\t{given_pattern_dict}")

# Let's check
print("=" * 20)
next_pair(9)
print("=" * 20)
next_pair(8)
print("=" * 20)
next_pair(7)
print("=" * 20)
next_pair(6)
print("=" * 20)
next_pair(0)