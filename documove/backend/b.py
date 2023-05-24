import os
import django
import requests
import json

# Django 설정 모듈을 설정합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from movies.models import Giving

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

    while True:
        projects = get_projects_for_theme(theme_id, api_key, next_project_id)

        if projects is None:  # API 요청이 실패한 경우
            break

        for project in projects["projects"]["project"]:
            # Extract only the required keys from each project
            extracted_project = {key: project[key] for key in ['id', 'organization', 'active', 'title', 'summary', 'themeName', 'country', 'region', 'funding', 'remaining', 'numberOfDonations', 'status', 'activities', 'imageLink', 'imageGallerySize', 'videos', 'approvedDate', 'themes', 'image', 'type'] if key in project}
            
            # Create a new Giving instance and save it
            giving = Giving(**extracted_project)
            giving.save()

        if projects["projects"]["hasNext"] == "true":
            next_project_id = projects["projects"]["nextProjectId"]
        else:
            break


if __name__ == "__main__":
    theme_id = 'climate'  # 여기에 원하는 테마 ID를 입력하세요.
    api_key = '5e1354cf-91c7-4d17-aa3a-1c908f511aad'  # 여기에 발급받은 API 키를 입력하세요.
    save_all_projects_for_theme(theme_id, api_key)
