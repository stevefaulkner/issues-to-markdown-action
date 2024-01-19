import os
import requests

def get_issues(repo, token, label):
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {'Authorization': f'token {token}'}
    params = {'state': 'all', 'labels': label}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")
    return response.json()

def save_issue(issue):
    try:
        title = issue.get('title', 'Untitled').replace(' ', '_')
        filename = f"{issue.get('number', 'Unknown')}_{title}.md"
        with open(filename, 'w') as file:
            file.write(f"# {issue.get('title', 'Untitled')}\n\n")
            file.write(issue.get('body', ''))
    except Exception as e:
        print(f"Error processing issue: {e}")

def main():
    repo = 'stevefaulkner/test2b'  # Replace with your username/repo
    token = os.getenv('GITHUB_TOKEN')
    try:
        issues = get_issues(repo, token, 'done')
        for issue in issues:
            save_issue(issue)
    except Exception as e:
        print(f"Error fetching issues: {e}")

if __name__ == "__main__":
    main()

