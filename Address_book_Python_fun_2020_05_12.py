# The code assumes the addressbook.txt file being in the order below with each record on a new line like so:
"""
last name
first ame
street
city state zip
home phone
mobile phone
"""
# Initial address book contents:
"""
    Lie
    Sophus
    2234 Valdres Rd
    Decorah, IA 52101
    777-555-1234
    777-554-4765
    Lee
    Kent D.
    700 College Drive
    Decorah, IA 52101
    777-555-1212
    777-554-0789
"""

# Here we go
# Grab the file name:
filename = "addressbook.txt" # This file is in the same folder/directory as this python script
# Create a file handle:
address_file = open(filename, "r+")
# Rampage:
while True: # Best for a repeated task that bails when condition fails -> False
  lookup_name = "" # so that the string can be reset for repeated searches within the same while loop session
  # Menu below:
  print("\nWould you like to ...")
  print("1) Look up a person by last name?")
  print("2) Add a person to the address book?")
  print("3) Quit?")
  # Grabe the user choice:
  user_choice = int(input("Please enter your choice: "))
  # Bail if user wants to Quit
  if user_choice == 3:
    break
  # Else, check if user wants to look up a name
  if user_choice == 1:
    # prompt user to enter the name:
    lookup_name = input("Please enter the last name to look up: ")
    # Grab the list of lines from the file handle saved earlier (No need to do this before line 42 ;)
    address_lines = address_file.readlines() # remember: a call to readlines() returns a List if lines
    # initialize a counter for possible records found: 
    record_count = 0
    # Do the loop dance:
    for index, line in enumerate(address_lines): # Enumerate because we need the index of the lines in the list
      # Then check if the current line matches the name entered and the line index modulo 6 returns 0 (because each last name in the address file is located at index 0, 6, 12, etc) -> pattern:
      if (lookup_name.rstrip().lower() == line.rstrip().lower() and (index % 6 == 0)):
        # Means Jackpot, use the current running index to pluck out the berries:
        print(f"Record for {lookup_name} found:")
        print(f"\t{address_lines[index + 1].rstrip()} {line.rstrip()}")
        print(f"\t{address_lines[index + 2].rstrip()}")
        print(f"\t{address_lines[index + 3].rstrip()}")
        print(f"\thome: {address_lines[index + 4].rstrip()}")
        print(f"\tmobile: {address_lines[index + 5].rstrip()}")
        # update the record count
        record_count += 1
      else:
        # since the file is being traversed in memory, reset it for the next search:
        address_file.seek(0)
    # End of for loop through the lines in the list, report on record find and/or count:
    if not record_count:
      print(f"Unfortunately, the name '{lookup_name}' is not on file.")
    else:
      print(f"A total of {record_count} record(s) were found for '{lookup_name}'.")
  # On the other hand, user might just want to add a record:
  if user_choice == 2:
    # Grab the dits:
    last_name = input("What is the last name? ")
    first_name = input("What is the first name? ")
    street = input("What is the street? ")
    city_state_zipcode = input("What is the city, state and zipcode? ")
    mobile = input("What is the mobile #? ")
    home_phone = input("What is the home phone #? ")
    # Anything could go wrong in trying to write to a file, hence, wrap it all up in a try/except block:
    try:
      address_file.write("\n" + last_name + "\n")
      address_file.write(first_name + "\n")
      address_file.write(street + "\n")
      address_file.write(city_state_zipcode + "\n")
      address_file.write(mobile + "\n")
      address_file.write(home_phone)
      # If no pbm: the next line prints
      print(f"Record for '{last_name}' has been successfully added to the address book!")
    except: # Means something went wrong, lots of ways to handle, this is just basic:
      print("Oh oh, something went wrong! Unable to write to or update the address book.")
# Done with the while True loop
print("Done")
# Remember to close the file:
address_file.close()