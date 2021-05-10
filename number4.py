#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game

import random
import string


def main():

    # input
    guess_as_string = str(input("Enter a number 1-10: "))
    random_number = random.randint(1, 10)

    # process & output
    try:
        guess_as_number = int(guess_as_string)
        if guess_as_number == random_number:
            print("Correct")
        else:
            print("Wrong. The answer was {}".format(random_number))
    except Exception:
        print("{} is not an integer".format(guess_as_string))

    finally:
        print("Thanks for playing <3")


if __name__ == "__main__":
    main()
