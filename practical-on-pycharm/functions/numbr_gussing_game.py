import random

def number_gussing_game():
    secret_number=random.randint(1,100)
    guess=None
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")
    print("Can you guess what it is?")
    while guess != secret_number:
        guess = int(input("Enter your guess"))
        if guess<secret_number:
            print("Too low! try again")
        elif guess>secret_number:
            print("T00 low try")