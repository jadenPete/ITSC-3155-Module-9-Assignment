# TODO: Feature 1
from urllib import response
from flask.testing import FlaskClient


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
    response_data = response.data()
    
    
    assert b'<tr>Table</tr>' in response_data
    
   

    