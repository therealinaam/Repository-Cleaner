# github repository cleaner
# Github REST APIs documentation: https://docs.github.com/en/rest/reference/repos#delete-a-repository
{
  "current_user_url": "https://api.github.com/user",
  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",
  "authorizations_url": "https://api.github.com/authorizations",
  "code_search_url": "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}",
  "commit_search_url": "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}",
  "emails_url": "https://api.github.com/user/emails",
  "emojis_url": "https://api.github.com/emojis",
  "events_url": "https://api.github.com/events",
  "feeds_url": "https://api.github.com/feeds",
  "followers_url": "https://api.github.com/user/followers",
  "following_url": "https://api.github.com/user/following{/target}",
  "gists_url": "https://api.github.com/gists{/gist_id}",
  "hub_url": "https://api.github.com/hub",
  "issue_search_url": "https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}",
  "issues_url": "https://api.github.com/issues",
  "keys_url": "https://api.github.com/user/keys",
  "label_search_url": "https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}",
  "notifications_url": "https://api.github.com/notifications",
  "organization_url": "https://api.github.com/orgs/{org}",
  "organization_repositories_url": "https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}",
  "organization_teams_url": "https://api.github.com/orgs/{org}/teams",
  "public_gists_url": "https://api.github.com/gists/public",
  "rate_limit_url": "https://api.github.com/rate_limit",
  "repository_url": "https://api.github.com/repos/{owner}/{repo}",
  "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}",
  "current_user_repositories_url": "https://api.github.com/user/repos{?type,page,per_page,sort}",
  "starred_url": "https://api.github.com/user/starred{/owner}{/repo}",
  "starred_gists_url": "https://api.github.com/gists/starred",
  "user_url": "https://api.github.com/users/{user}",
  "user_organizations_url": "https://api.github.com/user/orgs",
  "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page,per_page,sort}",
  "user_search_url": "https://api.github.com/search/users?q={query}{&page,per_page,sort,order}"
}

# %%
# import required modules
import requests
from prettytable import PrettyTable

# %%
# ------ This part asks the user to input their username ans displays all the repositories in the account ------

table = PrettyTable()
table.field_names = ["Name", "Size", "Last Modified"]

# asking the user to enter the github username
username = input("Enter the github username: ")
password = input("Enter the github password: ")
github_url = "https://api.github.com/users/" + username + "/repos"


# getting the response from the github api
response = requests.get(github_url)
# getting the json data from the response
json_data = response.json()
# looping through the json data
for data in json_data:
    # getting the name of the repository
    name = data["name"]
    # getting the size of the repository
    size = data["size"]
    # getting the last modified date of the repository
    last_modified = data["updated_at"]

    # adding the data to the table
    table.add_row([name, size, last_modified])

# printing the table
print(table)


# %%
# ------ This part asks the user to input the repository name and deletes the repository ------

# asking the user to enter the repository name
repo_name = input("Enter the repository name: ")

# getting the response from the github api
response = requests.delete("https://api.github.com/repos/" + username + "/" + repo_name, auth=(username, password))

# getting the status code from the response
status_code = response.status_code

# checking if the status code is 204
if status_code == 204:
    print("The repository was successfully deleted")
else:
    print("The repository was not deleted")
    
# %%
# ------ This part asks the user to input the repository name, then asks the specific foder or file that they want to delete ------

# asking the user to enter the repository name
repo_name = input("Enter the repository name: ")

# getting the response from the github api
response = requests.get("https://api.github.com/repos/" + username + "/" + repo_name + "/contents", auth=(username, password))

# getting the json data from the response
json_data = response.json()

# looping through the json data
for data in json_data:
    # getting the name of the file or folder
    name = data["name"]
    # getting the type of the file or folder
    type = data["type"]

    # checking if the type is file
    if type == "file":
        # printing the file name
        print("File: " + name)
    # checking if the type is dir
    elif type == "dir":
        # printing the folder name
        print("Folder: " + name)

# asking the user to enter the file or folder name
file_folder_name = input("Enter the file or folder name: ")

# getting the response from the github api
response = requests.delete("https://api.github.com/repos/" + username + "/" + repo_name + "/contents/" + file_folder_name, auth=(username, password))

# getting the status code from the response
status_code = response.status_code

# checking if the status code is 204
if status_code == 204:
    print("The file or folder was successfully deleted")
else:
    print("The file or folder was not deleted")


# %%
