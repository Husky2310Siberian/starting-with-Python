# Make a game where the computer generates a random number, and the player has to guess it.

import random

secret_number = random.randint(1, 100)

def guess_number():
    """
    Recursive function to guess the secret number.
    """
    guess = int(input("Guess the secret number: "))

    if guess > secret_number:
        print("Too high")
        guess_number()

    elif guess < secret_number:
        print("Too low")
        guess_number()

    else:
        print("Correct")


guess_number()