import pytest
from src.repositories.movie_repository import get_movie_repository
from tests import clear_movie_repository

def create_movies():
	movie_repository = get_movie_repository()
	movie_repository.create_movie("Dune (2021)", "Denis Villeneuve", 5)
	movie_repository.create_movie("Dune (1984)", "David Lynch", 3)
	movie_repository.create_movie("Avatar", "James Cameron", 4)

@pytest.mark.usefixtures("clear_movie_repository")
def test_search_existent():
	create_movies()

	movie_repository = get_movie_repository()

	dune_movie = movie_repository.get_movie_by_title("Dune (2021)")

	assert dune_movie.title == "Dune (2021)"
	assert dune_movie.director == "Denis Villeneuve"
	assert dune_movie.rating == 5

@pytest.mark.usefixtures("clear_movie_repository")
def test_search_nonexistent():
	create_movies()

	movie_repository = get_movie_repository()

	assert movie_repository.get_movie_by_title("Dune") is None
	assert movie_repository.get_movie_by_title("") is None
