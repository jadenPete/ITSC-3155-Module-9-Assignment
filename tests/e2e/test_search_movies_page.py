from flask.testing import FlaskClient
import pytest
import re
from tests.e2e import movie_row_regex
from tests import clear_movie_repository

@pytest.mark.usefixtures("clear_movie_repository")
def test_search_page(test_app: FlaskClient):
	test_app.post("/movies", data={
		"movie_title": "Dune (2021)",
		"movie_director": "Denis Villeneuve",
		"movie_rating": "5"
	})

	test_app.post("/movies", data={
		"movie_title": "Dune (1984)",
		"movie_director": "David Lynch",
		"movie_rating": "3"
	})

	test_app.post("/movies", data={
		"movie_title": "Avatar",
		"movie_director": "James Cameron",
		"movie_rating": "4"
	})

	response = test_app.get("/movies?q=Dune (2021)")
	response_data = response.data.decode()

	dune_2021_regex = movie_row_regex("Dune (2021)", "Denis Villeneuve", "5")

	for regex in [dune_2021_regex]:
		assert re.search(regex, response_data, re.MULTILINE) is not None

	response = test_app.get("/movies?q=")
	response_data = response.data.decode()

	for regex in [
		dune_2021_regex,
		movie_row_regex("Dune (1984)", "David Lynch", "3"),
		movie_row_regex("Avatar", "James Cameron", "4")
	]:
		assert re.search(regex, response_data, re.MULTILINE) is not None
