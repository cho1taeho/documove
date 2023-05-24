
import os
import requests
import json
from datetime import datetime

def convert_tv_data(tv):
    first_air_date = tv["first_air_date"]
    if not first_air_date:
        first_air_date = None
    else:
        first_air_date = datetime.strptime(first_air_date, "%Y-%m-%d").strftime("%Y-%m-%d")

    converted_tv = {
        "model": "movies.movie",
        "pk": tv["id"],
        "fields": {
            "name": tv["name"],
            "original_name": tv["original_name"],
            "overview": tv["overview"],
            "poster_path": tv["poster_path"],
            "first_air_date": first_air_date,
            "popularity": tv["popularity"],
            "vote_average": tv["vote_average"],
            "vote_count": tv["vote_count"],
            "like_users": [],
            "theme_id": "water"
        }
    }

    return converted_tv

def download_tv_shows_by_keyword(keyword):
    url = 'https://api.themoviedb.org/3/search/tv'
    params = {
        'api_key': 'db62ad7757737f4cf7101493c0bccdf2',
        'language': 'ko-KR',
        'query': keyword,
        'page': 1
    }

    all_tv_shows = []

    while True:
        response = requests.get(url, params=params)
        data = response.json()
        tv_shows = data.get('results', [])

        converted_tv_shows = [convert_tv_data(tv) for tv in tv_shows if tv.get('poster_path')]
        all_tv_shows.extend(converted_tv_shows)

        # 다음 페이지로 이동
        page = data.get('page', 1)
        total_pages = data.get('total_pages', 1)
        if page >= total_pages:
            break
        params['page'] = page + 1

    # 파일 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'movies/fixtures/tmdb/fishing.json')

    # JSON 파일로 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_tv_shows, f, indent=4, ensure_ascii=False)

    return all_tv_shows

def main():
    keyword = 'fishing'  # 검색할 키워드
    tv_shows = download_tv_shows_by_keyword(keyword)
    print(f"키워드 '{keyword}'를 포함하는 모든 TV 쇼 데이터를 JSON 파일로 다운로드하였습니다. (총 {len(tv_shows)}개)")

if __name__ == '__main__':
    main()
