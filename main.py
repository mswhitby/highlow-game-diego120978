import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 7

    print("Guess the number between 1 and 100. You have 7 attempts.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess == number:
                print("Correct! You win!")
                return
            elif guess < number:
                print("Too low. Guess higher.")
            else:
                print("Too high. Guess lower.")
            attempts -= 1
        except ValueError:
            print("Invalid input. Enter a number.")

    print(f"Out of attempts! The number was {number}.")

guess_the_number()
