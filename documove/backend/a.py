import os
import requests
import json

def download_all_movies_by_keyword(keyword):
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

        all_movies.extend(movies)

        # 다음 페이지로 이동
        page = data.get('page', 1)
        total_pages = data.get('total_pages', 1)
        if page >= total_pages:
            break
        params['page'] = page + 1

    # 파일 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'movies/fixtures/Environment.json')

    # JSON 파일로 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(all_movies, f, indent=4, ensure_ascii=False)

    return all_movies

def main():
    keyword = 'Environment'  # 검색할 키워드
    movies = download_all_movies_by_keyword(keyword)
    print(f"키워드 '{keyword}'를 포함하는 모든 영화 데이터를 JSON 파일로 다운로드하였습니다. (총 {len(movies)}개)")

if __name__ == '__main__':
    main()