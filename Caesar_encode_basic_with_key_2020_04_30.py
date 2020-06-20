# Write a function to encode supplied messages
# The function optionally takes a key (digit) by which to shift the characters  

# Alphabetic positions dict for reference:
given_position = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 26}

# Swap the key:value pair in the dict for easy reference:
position_2 = {v : k for k, v in given_position.items()}  #-> Basically saying, loop over each 'key:value' pair in the given_position dict, swap the pair around into 'value:key' and shovel them into the new dict position_2. Hence, position_2 # => {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: ' '}

def encode_message(msg, shift_key=0):
    encoded_message = "" # Create a 0 len variable to hold the final encoded message
    # Check for shift_key
    if not shift_key: # shifet_key is set to 0 by default, if it changes, this condition returns false
        print(f"Nothing encoded -> '{msg}'") # Means there was no shift_key provided
    else: # Means there is a non-zero shift key
        # turn the message into a list containing each character as a member,  then loop through each character:
        # Save the length of the keys of the position_2 dict
        length = len(position_2.keys()) # length = 27, not hardcoded, for use next
        for c in list(msg.lower()): # for each character in lowercased msg
            # check if shifting by the steps in the shift_key would not overflow:
            if (given_position[c] + shift_key) < int(length / 2): 
                # If no overflow, add the character at a position equal to its old position plus shift_key in the encoded_message:
                encoded_message += position_2[given_position[c] + shift_key]
                # print(f"{c} is now: {position_2[shift_key + given_position[c]]}")
            else: # Otherwise, adjust for steps circling back to the beginning of the underlying dict, use a % to locate target character having first combined the old position with the shift_key
                encoded_message += position_2[(given_position[c] + shift_key) % length]
                print(f"{c} -> {position_2[(given_position[c] + shift_key) % length]}")
    print(f"'{msg}' shifted by '{shift_key}' becomes: '{encoded_message}'")

#Test:
message= "hi I am Caesar"
message2 = "hI"
message3 = "za Az"
message4 = "abracadabra"
message5 = "abcz"
print("*" * 40)
encode_message(message, 1)
print("*" * 40)
encode_message(message2, 2)
print("*" * 40)
encode_message(message3, 8)
print("*" * 40)
encode_message(message4, 13)
print("*" * 40)
encode_message(message5, 26)
print("*" * 40)