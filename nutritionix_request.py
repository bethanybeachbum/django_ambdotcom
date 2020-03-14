"""
user name:  bethanybeachbum
API_ID:
a960790f

API_KEY:
399046c67a2d31b9d2b1b67f7492e7de
"""

import requests

url = "https://trackapi.nutritionix.com/v2/natural/nutrients?query=popcorn"
response = requests.get(url,
  headers = {
    "Content-Type":"application/json",
    "appId":"a960790f",
    "appKey":"399046c67a2d31b9d2b1b67f7492e7de",
    "x-remote-user-id":"bethanybeachbum",
    "query":"Cookies `n Cream"
    }
)

print(type(response))

# we print the status code
print(f"Status code: {response.status_code}")

response_dict = response.json()
print(response_dict.keys())

# Use requests to make the call to the API
# We call get() and pass it the URL and the header that we definded
# And we assign the response object to the variable r
# the response object has an attribute called status_code which
# tells us whether the request was successful
# r = requests.get(url, headers=headers)

# The API returns the info in JSON format so we use json() metho to convert
# the info to a Python dictdionary
# Store API response in a variable call response_dict.

	# response_dict = r.json()

	# # Process results.
	# print(response_dict.keys())
	# # Print the value associated with total_count
	# print(f"Total repositories: {response_dict['total_count']}")

	# # Explore infomration aboaut the repositories.
	# # The vaue associated with 'items' is a list containg a number of dicutionaries,
	# # each of which contains data about an iddividual Python repos.
	# # We store this list of dictionaries in rep_dicts.
	# repo_dicts = response_dict['items']
	# # Print the length of rep_dicts to see how many repos we have info for.
	# print(f"Repositories returned: {len(repo_dicts)}")
	# # Pull out the first item in the dictionary and stor it to repo_dict
	# # Examine the first repository.
	# repo_dict = repo_dicts[1]
	# # print number of keys
	# print(f"\nKeys: {len(repo_dict)}")
	# # print the ditctionary's keys
	# for key in sorted(repo_dict.keys()):
	# 	print(key)

	# print("---------------")
	# print("\nSelected information about first repo:")
	# print(f"Name: {repo_dict['name']}")
	# print(f"Owner: {repo_dict['owner']['login']}")
	# print(f"Stars: {repo_dict['stargazers_count']}")
	# print(f"Repository: {repo_dict['html_url']}")
	# print(f"Created: {repo_dict['created_at']}")
	# print(f"Updated: {repo_dict['updated_at']}")
	# print(f"Description: {repo_dict['description']}")


# Make an API call and store the response.
# Store the URL of the API call in the 'url' variable.
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'


