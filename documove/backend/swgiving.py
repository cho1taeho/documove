import requests
import json

API_KEY = '5e1354cf-91c7-4d17-aa3a-1c908f511aad'  # 여기에 GlobalGiving API 키를 입력하세요.
THEME_ID = 'water'  # 여기에 원하는 테마 ID를 입력하세요.
BASE_URL = 'https://api.globalgiving.org/api/public/projectservice/themes/{}/projects'

def fetch_projects(theme_id, next_id=None):
    url = BASE_URL.format(theme_id)

    params = {
        'api_key': API_KEY,
    }

    if next_id:
        params['nextProjectId'] = next_id

    response = requests.get(url, headers={'Accept': 'application/json'}, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        return None


def fetch_all_projects(theme_id):
    next_id = None
    all_projects = []

    while True:
        response = fetch_projects(theme_id, next_id)
        
        if response is None:  # API 요청이 실패한 경우
            break

        all_projects.extend(response["projects"]["project"])

        if response["projects"]["hasNext"] == "true":
            next_id = response["projects"]["nextProjectId"]
        else:
            break

    return all_projects


def save_as_json_file(filename, data):
    with open(f'movies/fixtures/{filename}', 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    projects = fetch_all_projects(THEME_ID)
    save_as_json_file('giving.json', projects)
