import pytest
from project import select_movie, is_movie_guessed, display_progress
from moviesname import movietitle

def test_select_movie():
    movie, hint, description = select_movie()
    assert isinstance(movie, str)
    assert isinstance(hint, str)
    assert isinstance(description, str)
    assert (movie, hint, description) in movietitle

def test_is_movie_guessed():
    assert is_movie_guessed("JURRASIC PARK", set("JURRASICPARK")) == True
    assert is_movie_guessed("INCEPTION", set("INCEPT")) == False
    assert is_movie_guessed("the godfather", set("THE GODFATHER")) == True
    assert is_movie_guessed("barbie", set("BARBIE")) == True
    assert is_movie_guessed("STAR wars", set("STAR")) == False


def test_display_progress():
    assert display_progress("TITANIC", set()) == "_______"
    assert display_progress("TITANIC", set("TIC")) == "TIT__IC"
    assert display_progress("FROZEN", set("FRINOXZEN")) == "FROZEN"
    assert display_progress("Interstellar", set("INTZXER")) == "INTER_TE___R"
    assert display_progress("The Matrix", set("AEIOU")) == "__E _A__I_"
    assert display_progress("Pulp Fiction", set("PIC")) == "P__P _IC_I__"

def test_movie_length():
    assert len("The Matrix".replace(" ","")) == 9
    assert len("Oppenheimer".replace(" ","")) == 11
    assert len("The Lion King".replace(" ", "")) == 11
    assert len("FORREST GUMP".replace(" ", "")) == 11
    assert len("FORREST GUMP".replace(" ", "")) == 11
    assert len("Back To The Future".replace(" ", "")) == 15





