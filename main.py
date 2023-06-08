import time
import random

words = input("Enter the secret words, separated by spaces: ").split()

name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
time.sleep(1)
print("Start guessing...\n")
time.sleep(0.5)

turns = 5

word = random.choice(words)
guesses = ''

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1
    if failed == 0:
        print("\nYou won")
        break
    guess = input("\nguess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("You have", turns, 'more guesses')
        if turns == 0:
            print("\nYou Lose")
