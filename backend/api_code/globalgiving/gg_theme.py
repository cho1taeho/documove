import requests
import json

def get_all_themes(api_key):
    api_endpoint = "https://api.globalgiving.org/api/public/services/themes"
    headers = {'Accept': 'application/json'}
    params = {
        "api_key": api_key,
    }
    response = requests.get(api_endpoint, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Received status code", response.status_code)
        return None

def main():
    api_key = '5e1354cf-91c7-4d17-aa3a-1c908f511aad'  # replace with your actual API key
    themes = get_all_themes(api_key)
    if themes:
        with open('movies/fixtures/themes.json', 'w') as f:
            json.dump(themes, f, indent=4)

if __name__ == "__main__":
    main()