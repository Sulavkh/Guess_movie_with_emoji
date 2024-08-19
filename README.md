Author: Sulav Khatiwada
Project Title:

# GUESS MOVIE WITH EMOJI

### Video Demo: https://www.youtube.com/watch?v=qkgYKTcBDUw

### Description:
    The movie guessing game is an interactive command-line game inspired by the classic word-guessing game Hangman. In this game player try to guess the title of the movie. one letter at a time, with the help of emoji hints and description. The game randomly selects a movie from a predefined list and provides the player with a clue in the form of emojis representing key elements of the movie. The player must then guess the movie title before running out of allowed incorrect guess.

    The inspiration for this game comes from the classic game Hangman, a popular word-guessing game. The Movie Guessing game takes the core concept of Hangman, but instead of simple word list, it uses movie names and emojis as hint. By using pop culture themes, this method not only brings the game up to date, but also makes more interesting and challenging.
### Project Files:
    1. Project.py: This is the main Python script that contains the game logic. It includes several functions.

    2. moviesname.py: This file contains the list of movies titles, their emoji hints and corresponding descriptions.

    3. test_project.py: A test file with unit tests to validate the game's functionnality.
### Chanllenges and learning
    One of the main challenges in developing this game was dealing with movie titles that contains spaces. The solution involved stripping spaces for guessing purposes while retaining them in the displayed progress, ensuring that the game stays fair and intuitive.
    This project provided a chance to deepen my understanding of Python's capabilities, including string manipulation, set operations, and the use of tuples and lists.
### Future Improvements:
    A Graphical User Interface(GUI) might be added to the game in the future using libraries like Pygame or Tkinter. Players would be presented with a more personalized challenge if varying difficulty levels were implemented according to the movies level of popularity. Furthermore, adding more titles to the movies database through integration with an internet API would make it more up-todate selection og titles. Introducing a scoring system with persistent top scores would boost replayability and add a competitve element. Finally, introducing multiplayer capability would allow playesr to compete against each other.
