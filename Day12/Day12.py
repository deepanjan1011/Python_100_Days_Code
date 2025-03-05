import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
thought_number = random.randint(1, 100)
lvl_choice = str(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
attempts = 10 if lvl_choice == 'easy' else 5
def game():
    global attempts
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == thought_number:
            print(f"You got it! The answer was {guess}.")
            return
        elif guess < thought_number:
            print("Too low.\nGuess again.")
        else:
            print("Too high.\nGuess again.")
        attempts -= 1
    if attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")

game()