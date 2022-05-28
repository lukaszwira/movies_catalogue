from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = []
    for movie in range(1,9):
        movies.append([])
    return render_template("homepage.html", movies=movies)