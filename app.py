from flask import Flask, redirect, render_template, request, url_for

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/movies")
def list_all_movies():
    if request.args.get("q", "") == "":
        movies = movie_repository.get_all_movies()
    else:
        movies = [movie_repository.get_movie_by_title(request.args["q"])]

    return render_template("list_all_movies.html", list_movies_active=True, movies=movies)


@app.get("/movies/new")
def create_movies_form():
    return render_template("create_movies_form.html", create_rating_active=True, message="")

@app.post("/movies")
def create_movie():
    movie_title = request.form.get("movie_title")
    movie_director = request.form.get("movie_director")
    movie_rating = request.form.get("movie_rating", type=int)

    if movie_title is None or movie_director is None or movie_rating is None or movie_rating < 0 or movie_rating >5:
        message = '<div class="alert alert-danger" role="invalid">Please enter a number between 1 and 5.'

        return render_template("create_movies_form.html", create_rating_active=False, message=message)
    else:
        movie_repository.create_movie(movie_title, movie_director, movie_rating)

    return redirect(url_for("list_all_movies"))

@app.get("/movies/search")
def search_movies():
    return render_template("search_movies.html", search_active=True)
