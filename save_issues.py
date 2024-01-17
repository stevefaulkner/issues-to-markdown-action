import os
import requests

def get_issues(repo, token, label):
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {'Authorization': f'token {token}'}
    params = {'state': 'all', 'labels': label}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def save_issue(issue):
    title = issue['title'].replace(' ', '_')
    filename = f"{issue['number']}_{title}.md"
    with open(filename, 'w') as file:
        file.write(f"# {issue['title']}\n\n")
        file.write(issue['body'])

def main():
    repo = 'your_username/your_repo'  # Replace with your username/repo
    token = os.getenv('GITHUB_TOKEN')
    issues = get_issues(repo, token, 'done')

    for issue in issues:
        save_issue(issue)

if __name__ == "__main__":
    main()
