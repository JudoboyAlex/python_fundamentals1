# Ask the user to enter a number. Use an if statement to print "that's a big number!" if the number is 100 or more, or "why not dream a little bigger?" otherwise.

print("Please enter a number")
num = input()
if int(num) >= 100:
    print("That's a big number!")
else:
    print("Why not dream a little bigger?")

# Ask the user to enter their age, and then display a message telling them how many years apart in age you are from them. If they enter a number larger than 105, print "I'm not sure I believe you".

print("Please enter your age")
user_age = input()
if int(user_age) < 105:
    print("You are {} apart in age from me.".format(37 - int(user_age)))
else:
    print("I'm not sure I believe you")

# Save your name as a string into a variable, then ask the user to enter their name. If the two names match, print "We have the same name!".

my_name = "Alexander The Great"
print("What is your name?")
user_name = input()
if my_name == user_name:
    print("We have the same name!")

# Pick a number and save it in a variable called secret_number. Ask the user to enter a number. If they enter the secret number, print "You win!". If they are off by 1, print "So close!". Otherwise, print "Try again".

secret_number = 9
print("Enter a number")
user_number = input()
if int(user_number) == secret_number:
    print("You win!")
elif int(user_number) - secret_number == 1 or int(user_number) - secret_number == -1:
    print("So close!")
else:
    print("Try again") 






