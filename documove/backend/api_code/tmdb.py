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
            "theme_id": "env",
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

        converted_movies = [convert_movie_data(movie) for movie in movies]
        all_movies.extend(converted_movies)

        # 다음 페이지로 이동
        page = data.get('page', 1)
        total_pages = data.get('total_pages', 1)
        if page >= total_pages:
            break
        params['page'] = page + 1

    # 파일 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'movies/fixtures/1.json')

    # JSON 파일로 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_movies, f, indent=4, ensure_ascii=False)

    return all_movies

def main():
    keyword = 'environment'  # 검색할 키워드
    movies = download_movies_by_keyword(keyword)
    print(f"키워드 '{keyword}'를 포함하는 모든 영화 데이터를 JSON 파일로 다운로드하였습니다. (총 {len(movies)}개)")

if __name__ == '__main__':
    main()
