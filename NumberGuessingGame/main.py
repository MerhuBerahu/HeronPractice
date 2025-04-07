"""
The program randomly picks a number, and the user tries to guess it.
"""
import random

computer_guess =  random.randint(1, 100)


while True:
    # Prompt the user to guess a number between 1 and 100
    user_guess = int(input("Guess a number between 1 and 100: "))

    # Check if the guess is correct
    if user_guess == computer_guess:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_guess < computer_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    