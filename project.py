import random
import string
from moviesname import movietitle

def main():
    movie, hint, description = select_movie()
    play_movie_guesser(movie, hint, description)

def select_movie():
    return random.choice(movietitle)

def play_movie_guesser(movie, hint, description):
    hidden_letters = set(movie.replace(" ", "").upper())  # letters in moviename
    guessed_letters = set()  # user guessed letter
    allowed_guesses = 10  # number of guess allowed

    print("\n Welcome to Movie Guessing Game!")
    print("\nMovie Hint")
    print(f"Emojis: {hint}")
    print(f"Description: {description}")
    print(f"The movie title has {len(movie.replace(' ', ''))} letters.")

    while hidden_letters and allowed_guesses > 0:
        progress = display_progress(movie, guessed_letters)
        print(f"\nCurrent Progress: {progress}")
        print(f"Guessed left: {allowed_guesses}")

        guess = get_player_guess(guessed_letters)

        if guess in hidden_letters:
            ()
            hidden_letters.remove(guess)
            print("Correct guess")
        else:
            allowed_guesses -= 1
            print("Incorrect guess")

        guessed_letters.add(guess)

    end_game(hidden_letters, movie)


def display_progress(movie, guessed_letters):
    progress = "".join(
        (
            letter.upper()
            if letter.upper() in guessed_letters or not letter.isalpha()
            else "_"
        )
        for letter in movie
    )
    #print(f"Current Progress: {progress}")
    return progress


def get_player_guess(guessed_letters):  # validate the correct guess and loop
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1:
            print("Please enter a single letter")
        elif guess not in string.ascii_uppercase:
            print("Please enter a valid letter")
        elif guess in guessed_letters:
            print("You have already guessed that letter")
        else:
            return guess


def end_game(hidden_letters, movie):
    if not hidden_letters:
        print(f"Congratulations!! You've guessed the movie: {movie}")
    else:
        print(f"Game Over. The movie name is {movie}")


def is_movie_guessed(movie, guessed_letters):
    return set(movie.upper().replace(" ", "")).issubset(guessed_letters)


if __name__ == "__main__":
    main()
