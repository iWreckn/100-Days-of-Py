import random

import hangman_words
import hangman_art


from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print("\n\nWelcome to hangman.\n")

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = set()
while not game_over:

    print(f"\n****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}. Try a different letter!")
        continue

    guessed_letters.add(guess)

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_ "

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {letter} that is not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

