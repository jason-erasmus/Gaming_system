from games.hangman_game.hangman import hangman_game
from games.number_game.guess_the_number import number_game

if __name__ == "__main__":
    game_choice = int(input("Choose a game 1 or 2"))
    if game_choice == 1:
        number_game()
    elif game_choice == 2:
        hangman_game()
    else:
        print("Choose a game")
