import requests


def printGithubStats(username):

    query_url = "https://api.github.com/users/" + username + "/repos"

    try:
        r = requests.get(query_url)
        jsonProfile = r.json()
    except:
        print("Cannot gather list of repos")
        return []
    

    ansList = []
    for repo in jsonProfile:
        try:
            repoName = repo['name']

            query_url = "https://api.github.com/repos/" + username +"/" + repoName + "/commits"

            r = requests.get(query_url)
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