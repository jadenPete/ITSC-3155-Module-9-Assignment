import pytest
from tests import clear_movie_repository

@pytest.mark.usefixtures("clear_movie_repository")
def test_create_page(test_app):
	response = test_app.post("/movies", data={
		"movie_title": "Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan",
		"movie_director": "Larry Charles",
		"movie_rating": "5"
	}, follow_redirects=True)

	assert response.status_code == 200
	assert b"Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan" in response.data
	assert b"Larry Charles" in response.data
	assert b"5" in response.data

	response = test_app.post("/movies", data={
		"movie_title": "Foo",
		"movie_director": "Bar"
	})

	assert response.status_code == 200
	print(response.data)
	assert b'<div class="alert alert-danger" role="invalid">Please enter a number between 1 and 5.' in response.data

	response = test_app.post("/movies", data={
		"movie_title": "Foo",
		"movie_rating": "5"
	})

	assert response.status_code == 200
	assert b'<div class="alert alert-danger" role="invalid">Please enter a number between 1 and 5.' in response.data

	response = test_app.post("/movies", data={
		"movie_director": "Bar",
		"movie_rating": "5"
	})

	assert response.status_code == 200
	assert b'<div class="alert alert-danger" role="invalid">Please enter a number between 1 and 5.' in response.data

	response = test_app.post("/movies", data={
		"movie_title": "Foo",
		"movie_director": "Bar",
		"movie_rating": "-1"
	})

	assert response.status_code == 200
	assert b'<div class="alert alert-danger" role="invalid">Please enter a number between 1 and 5.' in response.data

	response = test_app.post("/movies", data={
		"movie_title": "Foo",
		"movie_director": "Bar",
		"movie_rating": "7"
	})

	assert response.status_code == 200
	assert b'<div class="alert alert-danger" role="invalid">Please enter a number between 1 and 5.' in response.data
