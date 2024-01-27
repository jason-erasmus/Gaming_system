import random

from games.hangman_game.hangman_art import logo, stages
from games.hangman_game import hangman_words


def hangman_game():
    # import random

    # import hangman_words
    # from hangman_art import logo, stages
    end_of_game = False

    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)

    lives = 6

    print(logo)

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You have guessed {guess}. That is not in the word, you lose a life")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You Lose! The word was {chosen_word}")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])
