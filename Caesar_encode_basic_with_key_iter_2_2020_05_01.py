# Write a function to encode supplied messages
# The function optionally takes a key (digit) by which to shift the characters  

# Alphabetic positions dict for reference:
given_position = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 26}

# grab the keys in given_position dict, and join them into a string (which will be automatically zero indexed):
master_string = "".join(given_position.keys())
print(f"\nMaster String: '{master_string}'\n")
# Now, let's encode:
def encode_message(msg, shift_key=0):
  encoded_message = "" # Create a 0 len variable to hold the final message
  # Check if shift_key supplied:
  if not shift_key: # shifet_key is set to 0 by default, if it changes, this condition returns false
    print(f"Nothing encoded -> '{msg}'") # As no shift_key was provided
  else: # Means there is a non-zero shift_key
      # Save the length of the master_string for use later
    length = len(master_string) # length = 27, not hardcoded
    for character in list(msg.lower()): # since only lowercased letters and whitespaces are allowed 
      # save its current position (index) in the master_string
      character_index = master_string.find(character) # Since the master_string is made up of unique characters and a white space, each character's index is unique
      # check if shifting by the steps in the shift_key would not overflow:
      if (character_index + shift_key) < int(length / 2):
        # If no overflow, add the character at a position equal to its old position plus shift_key in the encoded_message:
              encoded_message += master_string[character_index + shift_key]
      else:
        # Otherwise, adjust for steps wrapping around the master_string, use a % (modulo) to locate target character having first combined the old character_index with the shift_key
        encoded_message += master_string[(character_index + shift_key) % length]
    # Report      
    print(f"'{msg}' shifted by '{shift_key}' becomes: '{encoded_message}'")

# Let's test:
message1= "hi I am Caesar"
message2 = "hI"
message3 = "za Az"
message4 = "abra ca dabr a"
message5 = "a b cz "
message6 = "Will this ever change?"
print("*" * 40)
encode_message(message1, 1)
print("*" * 40)
encode_message(message2, 2)
print("*" * 40)
encode_message(message3, 8)
print("*" * 40)
encode_message(message4, 13)
print("*" * 40)
encode_message(message5, 26)
print("*" * 40)
encode_message(message6, 0)