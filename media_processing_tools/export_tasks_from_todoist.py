import requests

TODOIST_API_TOKEN = '75080e7a87399c767c24335610c0271ab0caf46a'
TODOIST_API_URL = 'https://api.todoist.com/rest/v2/tasks'

def fetch_todoist_tasks():
    headers = {
        'Authorization': f'Bearer {TODOIST_API_TOKEN}'
    }
    
    response = requests.get(TODOIST_API_URL, headers=headers)
    if response.status_code == 200:
        tasks = response.json()
        return tasks
    else:
        print(f"Failed to fetch tasks. Status code: {response.status_code}")
        return []

if __name__ == '__main__':
    tasks = fetch_todoist_tasks()
    for task in tasks:
        print(task)
