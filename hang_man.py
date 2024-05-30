import random

words = ["apple", "orange", "banana", "lemon"]
choose_word = random.choice(words)
word_display = ['_' for _ in choose_word]
attempts = 8

while attempts > 0 and '_' in word_display:
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in choose_word:
        for index, letter in enumerate(choose_word):
            if letter == guess:
                word_display[index] = letter

    else:
        print("Guess again.")
        attempts -= 1

if '_' not in word_display:
    print("\n")
    print("you guessed it correctly.")
    print(" ".join(word_display))
    print("you win !!")
else:
    print("\n")
    print("run out of guesses")
    print("your loss")
