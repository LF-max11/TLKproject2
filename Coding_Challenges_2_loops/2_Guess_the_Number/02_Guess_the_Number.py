#-----------------------------------------------------------------------------
# Name:        Guess the Number(02_Guess_the-Number.py)
# Purpose:     Create  a program that generates a random number between `1`
#              and `10` and keeps asking the user to guess it using a `while`
#              loop **until they guess correctly
#
# Author:      LF
# Created:     15-March-2025
# Updated:     16-March-2025
#-----------------------------------------------------------------------------
print("Start")
import random

# Generate a random number between 1 and 10
number_to_guess = random.randint(1, 10)

# Start the guessing loop
while True:
    try:
        # Ask the user to guess the number
        guess = int(input("Guess the number (between 1 and 10): "))

        # Check if the guess is correct
        if guess == number_to_guess:
            print("Correct! 🎉")
            break  # Exit the loop once the correct guess is made
        else:
            print("Wrong, try again!")

    except ValueError:
        print("Please enter a valid number!")
print("Thank you for guessing!")
print("Have a nice day!")
