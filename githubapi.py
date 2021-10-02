import requests
import os


def printGithubStats(username):

    token = os.environ.get('GITHUB_TOKEN')

    query_url = f"https://api.github.com/users/{username}/repos"
    params = {
        "state": "open",
    }
    headers = {'Authorization': f'token {token}'}
    try:
        r = requests.get(query_url, headers=headers, params=params)
        jsonProfile = r.json()
    except:
        print("Cannot gather list of repos")
        return []
    

    ansList = []
    for repo in jsonProfile:
        try:
            repoName = repo['name']

            query_url = f"https://api.github.com/repos/{username}/{repoName}/commits"


            r = requests.get(query_url, headers=headers, params=params)
        except:
            print("Cannot access commit history for repo!")
            return []
        jsonRepos = r.json()
        numOfCommits = 0
        for repo in jsonRepos:
            numOfCommits += 1

        ansList.append("Repo: " + repoName + " Number of commits: " + str(numOfCommits))

    return ansList






if __name__ == '__main__':

    print(printGithubStats('ckubelle'))