from src.repositories.movie_repository import get_movie_repository
from app import app, movie_repository
import pytest

def test_movie_created():
    movie_repository.create_movie("Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan", "Larry Charles", 5)
    all_movies = movie_repository.get_all_movies()

    test_movie = Movie("Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan", "Larry Charles", 5)
    same_movie = False

    for movie in all_movies:
        if movie.__dict__ == test_movie.__dict__:
            same_movie = True

    assert same_movie

def test_movie_created():
    movie_repository.create_movie("Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan", "Larry Charles", 5)
    all_movies = movie_repository.get_all_movies()

    test_movie = Movie("Inception", "Christopher Nolan", 5)
    same_movie = False

    for movie in all_movies:
        if movie.__dict__ == test_movie.__dict__:
            same_movie = True