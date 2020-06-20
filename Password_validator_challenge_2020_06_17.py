# Challenge by ~Bwhiz:
"""
write a program that takes a string as input and evaluates it as a valid password. The password is valid if it has, at a minimum: 
    - 2 numbers,
    - 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*')
    - a length of at least 7 characters
If the password passes the check, output 'strong', else output 'weak'
"""
import random # Just in case we need to generate random stuff, like random passwords to test
import re # So we can validate as per the requirements
import string # So we can grab all the alphabet characters (a-z, A-Z, and numbers from 0-9)

# save the alpahabets and special characters in a string::
alphabets_plus_sp_chars = string.ascii_letters.join('!@#$%&*'*300 + string.digits * 300)
# Let's shuffle 
alphabets_plus_sp_chars = ''.join(random.sample(alphabets_plus_sp_chars,len(alphabets_plus_sp_chars)))
# NOTE that string.ascii_letters returns a string of all the alphabet letters, caps and small, and to that, we join the allowed special characters, a bunch of them, and the numbers via string.diguts.
# The shuffle above may be confusing, but here is another approach:
# Turn the string into a list
# alphabets_plus_sp_chars_list = list(alphabets_plus_sp_chars)
# Shuffle the result list:
# random.shuffle(alphabets_plus_sp_chars_list)
# Convert it back to a string:
# alphabets_plus_sp_chars = ''.join(alphabets_plus_sp_chars_list) # --> Same as above (line 16)
pattern = re.compile(r"(^(?=(.*\d){2,})(?=(.*[!@#$%&*]){2,})(?=.*\w)).{7,}$")
# The breakdown of the pattern:
#(^(?=(.*\d){2,})(?=(.*[!@#$%&*]){2,})(?=.*\w)).{7,}$
#Everything is put within brackets so that the .{7,} applies to all,  thus,
# ^ --> Means match start of the line
# (?=(.*\d){2,}) --> Means to look ahead and match at least two digits
# (?=(.*[!@#$%&*]){2,}) --> Means to look ahead and match at least two of these special characters inside the []
# (?=.*\w)) --> Means look ahead and match any letters, including, if any digits, a-z, A-Z or 0-9
# .{7,} --> In the end, everything to the left must be at least 7 characters long in total
# $ --> Means match the {7,} at the end of line
# NOw enter da func:
def validate_password(password):
  return f"'{password}' is STRONG." if pattern.match(password) else f"'{password}' is WEAK."
tes_case = validate_password("ab*17%TY") 
print(tes_case)
tes_case = validate_password('PT@KO@xq')
print(tes_case)
# Or, just generate random passwords and feed the results to the above validate_password function
# For example, let's say we want 90 passwords generated, each of length 8 chars, and test each:
for i in range(90):
    gen_password = ''.join(random.choice(alphabets_plus_sp_chars) for i in range(8)) # join some random chars!
    lab_res = validate_password(gen_password)
    print(lab_res)
# Another way to sample for the test is by using random.sample function with the desired length:
#for i in range(90):
#    gen_password = ''.join(random.sample(alphabets_plus_sp_chars,8))
#    lab_res = validate_password(gen_password)
#    print(lab_res)
    
    