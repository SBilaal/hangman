

from operator import contains
import random
import words



def hangman():
    lives = 6
    full_word = random.choice(words.words).upper()
    current_word = "-" * len(full_word)
    used_letters = ""


    while lives > 0 and current_word.upper() != full_word.upper():
        guessed = input('Guess a letter: ').upper()
        used_letters += (guessed + " ")

        if contains(full_word, guessed):
            index = full_word.index(guessed)
            split_current = list(current_word)
            split_current[index] = guessed
            current_word = "".join(split_current)
            print(f"You have {lives} lives left and you have used these letters: {used_letters}")
            print(f"Current word: {current_word}")
        else:
            lives = lives - 1
            print(f"Your letter, {guessed} is not in the word")
            print(f"You have {lives} lives left and you have used these letters: {used_letters}")
            print(f"Current word: {current_word}")
        print("")
        print("")
    if current_word.upper() == full_word.upper():
        print("Yay, you got it right!")
    else:
        print('Oops, try again later. The correct word is: {}'.format(full_word))

hangman()