import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMGU4ODRmNzM3MWMzNDIwM2Y3MzZmZWNjODIzNmE1ZCIsInN1YiI6IjYyOTA4YzY1N2Q1ZGI1MTBhNTFlNzFlNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bCSFcue4zW-DLWIZMa5HULuJV-b5BwW2C5t2jAFrvOg"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movie_info(original_title):
    title = "original_title"
    return f"{title}/{original_title}"


