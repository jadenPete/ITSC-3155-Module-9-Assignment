import pytest
from src.repositories import movie_repository

@pytest.fixture
def clear_movie_repository():
	movie_repository.clear_movie_repository()
