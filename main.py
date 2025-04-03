# Welcome
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number ")

# The computer needs to select a number between 1-100
import random
the_num = random.randint(1,100)

# testing: print(the_num)

# User Difficulty level: easy medium and hard

print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")
user_level = input("Enter Choice: ")
attempts = 0
#max_attempts = 0

if user_level == "1":
    max_attempts = 10
elif user_level == "2":
    max_attempts = 5
elif user_level == "3":
    max_attempts = 3
else:
    print("Invalid choice. Defaulting to Easy mode.")
    attempts = 10

# Based on the level they select they will get x amount of choices
if user_level == 1:
    print("Nice! You have selected the easy difficulty level.\nLet's start the game!")
elif user_level == 2:
    print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
else:
    print("WOW! You have selected the Hard difficulty level.\nLet's start the game!")


# Take user input for Guess

while attempts < max_attempts:
    user_guess = int(input("Enter your guess: "))
    attempts += 1
#user_guess != the_num:
    if user_guess == the_num:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.") 
        break
    elif user_guess > the_num:
        print(f"Your Guess is too High it should be less than {user_guess}")
    elif user_guess < the_num:
        print(f"Your Guess is too Low it should be greater than {user_guess}")
    else:
        print("Maybe Next time")
#Error Handling
if user_guess != the_num:
    print(f"Sorry, you're out of tries. The number was {the_num}.")

"""
Future features would include, a timer error handling and multiple rounds!
"""

