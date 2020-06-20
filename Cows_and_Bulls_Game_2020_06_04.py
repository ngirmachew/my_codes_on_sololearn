# This could be improved upon, do feel free to shout back if so inclined... 
# Cows and Bulls Game
# For info on the game go here --> https://en.wikipedia.org/wiki/Bulls_and_Cows
import random # All we need is randrange()!
# Let's boogy!
# Set your counters:
cows = 0
bulls = 0
attempt = 0
# Generate the four digit number to guess
generated_num = random.randrange(1000, 10000) # Here, the range is b/n 1000 (inclusive) and 10000 (exclusive). This returns a random four digit number between 1000 and 10000 (excluding 10000).. 
# Change the generated num into a list of individual digits and save it back to itself:
generated_num = [int(i) for i in str(generated_num)]
#print(f"TESTING 'generated_num': {generated_num}") # Uncomment this line if you want to beat the game ;)
# Roll out the red carpet:
print("\nWelcome to Cows and Bulls.\n")
# Initiate the loop
while True:
  user_input = input("Please input four numbers: ")
  # increment attempt by 1:
  attempt += 1
  # massage the user_input to turn it into a list of ints. 
  user_input = [int(x) for x in user_input.strip()]
  # print(f"TESTING 'user_input': {user_input}") # -> Uncomment this if you wish to see the converted input
  # Check for the cows and bulls:
  for i in range(4): # checking only for 4 digits
    if user_input[i] == generated_num[i]: # The cows score! There is index to index match
      cows += 1
    elif user_input[i] in generated_num: # The bulls kick in if index to index match fails for current iteration
      bulls += 1
  print(f"Cows: {cows}\nBulls: {bulls}\n") # Feedback
  # Check if the genius solved it, if so, break out:
  if cows == 4:
    print(f"Congratulations! The Answer was {generated_num} \nYou took {attempt} try to find out the answer")
    break
  # If we hit this line, means genius needs another try
  # Reset the cows and bulls
  cows = bulls = 0