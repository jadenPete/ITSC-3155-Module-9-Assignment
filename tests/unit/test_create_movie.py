import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from tests import clear_movie_repository

@pytest.mark.usefixtures("clear_movie_repository")
def test_movie_created():
    movie_repository = get_movie_repository()
    movie_repository.create_movie("Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan", "Larry Charles", 5)

    all_movies = movie_repository.get_all_movies()

    test_movie = Movie("Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan", "Larry Charles", 5)

    same_movie = False

    for movie in all_movies:
        if movie.__dict__ == test_movie.__dict__:
            same_movie = True

    assert same_movie

@pytest.mark.usefixtures("clear_movie_repository")
def test_movie_not_created():
    movie_repository = get_movie_repository()
    movie_repository.create_movie("Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan", "Larry Charles", 5)

    all_movies = movie_repository.get_all_movies()

    test_movie = Movie("Inception", "Christopher Nolan", 5)

    same_movie = False

    for movie in all_movies:
        if movie.__dict__ == test_movie.__dict__:
            same_movie = True

    assert not same_movie
