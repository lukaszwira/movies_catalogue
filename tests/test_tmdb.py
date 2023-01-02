import tmdb_client
from unittest.mock import Mock
from app import app
import pytest


@pytest.mark.parametrize('list_type',(
  ('now_playing', 'upcoming'),
  ('top_rated', 'popular')
  ))

def test_list_types(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.requests.get", api_mock)

   with app.test_client() as client:
      response = client.get('/')
      assert response.status_code == 200
      api_mock.assert_called_once_with('list_types')

def test_get_movies_list(monkeypatch):
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_poster_url_uses_default_size():
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   assert expected_default_size in poster_url

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def test_get_single_movie(monkeypatch):
   mock_movie = '{"movie_id":1}'

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movie = tmdb_client.get_single_movie("1")
   assert movie == mock_movie

def test_get_single_movie_cast(monkeypatch):
   expected_cast = []
   mock_movie = {"movie_id":1, "cast": expected_cast}

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   cast = tmdb_client.get_single_movie_cast("1")
   assert cast == expected_cast
