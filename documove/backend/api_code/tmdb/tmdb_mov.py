import os
import requests
import json
from datetime import datetime

def convert_movie_data(movie):
    release_date = movie["release_date"]
    if not release_date:
        release_date = None
    else:
        release_date = datetime.strptime(release_date, "%Y-%m-%d").strftime("%Y-%m-%d")

    converted_movie = {
        "model": "movies.movie",
        "pk": movie["id"],
        "fields": {
            "adult": movie["adult"],
            "genre_ids": movie["genre_ids"],
            "original_language": movie["original_language"],
            "original_title": movie["original_title"],
            "overview": movie["overview"],
            "popularity": movie["popularity"],
            "poster_path": movie["poster_path"],
            "release_date": release_date,
            "title": movie["title"],
            "vote_average": movie["vote_average"],
            "vote_count": movie["vote_count"],
            "like_users": [],
            "theme_id": "justice",
        }
    }

    return converted_movie

def download_movies_by_keyword(keyword):
    url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': 'db62ad7757737f4cf7101493c0bccdf2',
        'language': 'ko-KR',
        'query': keyword,
        'page': 1
    }

    all_movies = []

    while True:
        response = requests.get(url, params=params)
        data = response.json()
        movies = data.get('results', [])

        converted_movies = [convert_movie_data(movie) for movie in movies if movie.get('poster_path')]
        all_movies.extend(converted_movies)

        # Move to the next page
        page = data.get('page', 1)
        total_pages = data.get('total_pages', 1)
        if page >= total_pages:
            break
        params['page'] = page + 1

    # Set the file path
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'movies/fixtures/tmdb/human_rights.json')

    # Save as JSON file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_movies, f, indent=4, ensure_ascii=False)

    return all_movies

def main():
    keyword = 'human rights'  # Keyword to search
    movies = download_movies_by_keyword(keyword)
    print(f"Downloaded all movie data containing the keyword '{keyword}' as a JSON file. (Total: {len(movies)} movies)")

if __name__ == '__main__':
    main()

