import requests
import json
import os

def get_projects_for_theme(theme_id, api_key, next_project_id=None):
    base_url = "https://api.globalgiving.org/api/public/projectservice/themes/{}/projects".format(theme_id)
    headers = {'Accept': 'application/json'}
    params = {
        "api_key": api_key,
    }

    if next_project_id:
        params["nextProjectId"] = next_project_id

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def save_all_projects_for_theme(theme_id, api_key):
    next_project_id = None
    all_projects = []

    if os.path.isfile('movies/fixtures/giving.json'):
        with open('movies/fixtures/giving.json', 'r') as f:
            all_projects = json.load(f)

    while True:
        projects = get_projects_for_theme(theme_id, api_key, next_project_id)

        if projects is None:  # API 요청이 실패한 경우
            break

        all_projects.extend(projects["projects"]["project"])

        if projects["projects"]["hasNext"] == "true":
            next_project_id = projects["projects"]["nextProjectId"]
        else:
            break

    with open('movies/fixtures/giving.json', 'w') as f:
        json.dump(all_projects, f, indent=4)

if __name__ == "__main__":
    theme_id = 'children'  # 여기에 원하는 테마 ID를 입력하세요.
    api_key = '5e1354cf-91c7-4d17-aa3a-1c908f511aad'  # 여기에 발급받은 API 키를 입력하세요.
    save_all_projects_for_theme(theme_id, api_key)