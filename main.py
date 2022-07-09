

from operator import contains
import random
import string
import words



def hangman():
    lives = 6
    full_word = random.choice(words.words).upper()
    current_word = "-" * len(full_word)
    used_letters = ""


    while lives > 0 and current_word.upper() != full_word.upper():
        guessed = input('Guess a letter: ').upper()
        used_letters += (guessed + " ")

        if guessed in full_word:
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

# Using what I have learned from a video

def clean_word():
    word = random.choice(words.words)
    while " " in word or "-" in word:
        # if " " in word or "-" in word:
        word = random.choice(words.words)
    return word.upper()

def hangman_v2():
    chosen_word = clean_word()
    guesses_left = set(chosen_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while lives > 0 and len(guesses_left) > 0:
        guessed = input("Guess a letter: ").upper()
        print("")
        if guessed in alphabet - used_letters:
            used_letters.add(guessed)
            if guessed in chosen_word:
                guesses_left.remove(guessed)
            else:
                print(guessed, " isn't in the word")
                lives = lives - 1
        else: 
            print("You've chosen this letter before")
        print("You have ", lives, " lives left and you have used these letters: ", " ".join(used_letters))
        guessed_status = [i if i not in guesses_left else "-" for i in chosen_word]
        print("Current word: ", "".join(guessed_status))
        print("")

    if len(guesses_left) == 0:
        print('Yay! You got it right')
    else:
        print('Oops, another time. The correct word is: ', chosen_word)

hangman_v2()