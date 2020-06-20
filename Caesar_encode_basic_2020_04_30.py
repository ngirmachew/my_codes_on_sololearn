given_position = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ' ': 26}
position_2 = {v : k for k, v in given_position.items()}

def encode_message(msg):
    encoded_message = "".join([position_2[given_position[c.lower()]+1] if given_position[c.lower()] + 1 <= 26 else position_2[0] for c in list(msg)])
    print(f"'{msg}' becomes: '{encoded_message}'")
#Test:
message= "hi I am Caesar"
message2 = "hI"
message3 = "za Az"
message4 = "abracadabra"
encode_message(message)
encode_message(message2)
encode_message(message3)