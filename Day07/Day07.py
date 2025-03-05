import random
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
lives = 6


import hangman_art
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:


    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()



    display = ""

    for letter in chosen_word:
        if letter == guess:
            print("You've already guessed",letter)
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)



    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True


            print(f"IT WAS {chosen_word}! YOU LOSE")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    
    print(hangman_art.stages[lives])
