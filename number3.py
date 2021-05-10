#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game, but better

import random


def main():
    # this function plays the number guessing game, but better

    number = 10
    guess = int(input("Guess a number 1-10: "))

    if guess == number:
        print("Correct!")
    if guess != number:
        print("Incorrect, the answer was: ")
        print(number)
        

if __name__ == "__main__":
    main()
