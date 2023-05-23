import requests
import json

def get_all_projects(api_key):
    api_endpoint = "https://api.globalgiving.org/api/public/projectservice/all/projects/active"
    headers = {'Accept': 'application/json'}
    params = {
        "api_key": api_key,
    }
    all_projects = []
    next_project_id = 0

    while True:
        if next_project_id:
            params["nextProjectId"] = next_project_id
        response = requests.get(api_endpoint, headers=headers, params=params)
        if response.status_code == 200:
            response_json = response.json()
            all_projects.extend(response_json['projects']['project'])
            if response_json['projects']['nextProjectId']:
                next_project_id = response_json['projects']['nextProjectId']
            else:
                break
        else:
            print("Error: Received status code", response.status_code)
            break
    return all_projects

def main():
    api_key = '5e1354cf-91c7-4d17-aa3a-1c908f511aad'  # replace with your actual API key
    projects = get_all_projects(api_key)
    if projects:
        with open('movies/fixtures/giving.json', 'w') as f:
            json.dump(projects, f, indent=4)

if __name__ == "__main__":
    main()
