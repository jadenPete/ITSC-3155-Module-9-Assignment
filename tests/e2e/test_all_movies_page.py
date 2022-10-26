from flask.testing import FlaskClient
import pytest
import re
from tests import clear_movie_repository
from tests.e2e import movie_row_regex

@pytest.mark.usefixtures("clear_movie_repository")
def test_home_page(test_app: FlaskClient):
	test_app.post("/movies", data={
		"movie_title": "Avatar",
		"movie_director": "James Cameron",
		"movie_rating": "5"
	})

	test_app.post("/movies", data={
		"movie_title": "James Bond",
		"movie_director": "Ian Fleming",
		"movie_rating": "2"
	})

	test_app.post("/movies", data={
		"movie_title": "Barbarian",
		"movie_director": "Zach Cregger",
		"movie_rating": "4"
	})

	response = test_app.get("/movies")

	assert response.status_code == 200

	response_data = response.data.decode()

	for regex in [
		movie_row_regex("Avatar", "James Cameron", "5"),
		movie_row_regex("James Bond", "Ian Fleming", "2"),
		movie_row_regex("Barbarian", "Zach Cregger", "4")
	]:
		assert re.search(regex, response_data, re.MULTILINE) is not None
