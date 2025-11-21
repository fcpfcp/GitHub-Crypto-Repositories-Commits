```python
import requests
import json
import os


REPOS = [
"bitcoin/bitcoin",
"ethereum/go-ethereum",
"solana-labs/solana"
]


API_URL = "https://api.github.com/repos/{}/commits"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def fetch_commit_count(repo):
headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
url = API_URL.format(repo)
response = requests.get(url, headers=headers)


if response.status_code == 200:
commits = response.json()
return len(commits)
else:
return None


def main():
results = {}


for repo in REPOS:
count = fetch_commit_count(repo)
results[repo] = count


print(json.dumps(results, indent=2))


if __name__ == "__main__":
main()
