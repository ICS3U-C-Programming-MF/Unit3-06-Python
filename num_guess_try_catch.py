#!/usr/bin/env python3
# Made by Maximiliano Fairman
# Created on oct 23rd 2025
# Use a random number generator
# to create a correct guess between 0 and 9 every time the program is started over.
import random  # used to generate a random number

def main():
    # Ask the user to guess
    try:
        guess = int(input("Guess a number between 0 and 9: "))
        secret_number = random.randint(0, 9)  # generates a random number between 0 and 9

        # If the guess is correct
        if guess == secret_number:
            print("You guessed correctly!")
        # If the guess is incorrect
        else:
            print("You guessed wrong")
    # if the user inputs a non-integer
    except ValueError:
        print("Invalid input. Please enter an integer between 0 and 9.")

if __name__ == "__main__":
    main()
