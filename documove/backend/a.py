import os
import requests
import json

def download_environment_documentaries():
    url = 'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': 'db62ad7757737f4cf7101493c0bccdf2',
        'language': 'ko-KR',
        'with_genres': 99,  # 다큐멘터리 장르의 genre_id
        'page': 1,
        'total_pages': 3000  # 원하는 페이지 수로 설정하세요
    }

    environment_documentaries = []

    for page in range(1, params['total_pages'] + 1):
        params['page'] = page
        response = requests.get(url, params=params)
        data = response.json()
        movies = data.get('results', [])

        for movie in movies:
            # 영화의 장르 목록을 가져옵니다
            genre_ids = movie.get('genre_ids', [])

            # "environment" 장르 ID인 10321이 포함되어 있는지 확인합니다
            if 10321 in genre_ids:
                environment_documentaries.append(movie)

    # 파일 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'movies/fixtures/environment_docu.json')

    # JSON 파일로 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(environment_documentaries, f, indent=4, ensure_ascii=False)

    return environment_documentaries

def main():
    environment_documentaries = download_environment_documentaries()
    print(f"환경 관련 다큐멘터리 영화 데이터를 JSON 파일로 다운로드하였습니다. (총 {len(environment_documentaries)}개)")

if __name__ == '__main__':
    main()