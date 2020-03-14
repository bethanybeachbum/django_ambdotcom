"""
user name:  bethanybeachbum
API_ID:
a960790f

API_KEY:
399046c67a2d31b9d2b1b67f7492e7de
"""

import requests
import json
import pprint

url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
headers = {
    "accept": "application/json",
    "x-app-id":"a960790f",
    "x-app-key":"399046c67a2d31b9d2b1b67f7492e7de",
    "x-remote-user-id":"bethanybeachbum",
    "query":"hamburger"
    }
payload={"query":"banana"}
body={"json"}
r = requests.post(url, headers=headers, data=payload, json=body)

# print the status code
print(f"Second Status code: {r.status_code}")
print(f"r.text is this type:{type(r.text)}")
print(f" * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
print(f" * * * * * * * * * r.text type: * * * * ** * * *")
print(r.text)
print(f"\n")
print(f" * * * * * * * * * END OF r.text  * * * * ** * * *")
print(f"  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
#json.load method converts JSON string to Python Object
# parsed = json.loads(r)
print(f"\n")
# Json to dictionary conversion:
response_dict = r.json()
print(f"The below object called 'response_dict' has a TYPE of: {type(response_dict)} ")
print(f"\n")

print(f"  ~ ~ ~ ~ PRINTING 'response_dict' which now has a type of dictionary ~ ~ ~ ~")
print(f"\n")
print(response_dict)
print(f"\n")

print(f" ~ ~ ~ ~ ~ Printing KEYS of the dicitionary: response_dict ~ ~ ~ ~ ~ ~")
print(response_dict.keys())
print(f"Number of keys: ")
print(len(response_dict.keys()))
print(f"\n")

print(f"the first value of response_dict is a list --> response_dict['foods']\n")

print(response_dict['foods'])
print(f"\n")

print( f" $ $ $ $ Food Dictionary Count $ $ $ $ $")
print (f" assinging the first value of the dictionary to a variable called food_list\n")
food_list = response_dict['foods']
print(f"here is the type of the new variable called food_dicts: {type(food_list)}\n")

print(f"Food list returned this many : {len(food_list)}")

print("...")
print("\n")
print(food_list)

print(f" # # # # # # # END OF PRINTING FOOD LIST # # # # # # ")

print("\n")
print(f" # # # # # # # NOW PRINTING --> food_list[0] # # # # # # \n")
print(food_list[0])

print(f"  % % % % % % % % % % ASSIGNING food_list[0] to a variable called 'firstfood' % % % % % % % % % % % % \n")
firstfood = food_list[0]
print(f"Pringting firstfood\n")
print(firstfood)
print("\n")
print(f"Type of variable called firstfood: {type(firstfood)}\n")
print(f"first dictionary item of variable firstfood:")
print(firstfood['food_name'])
print(" Next line is this command:  print(firstfood['full_nutrients'][0]) ")
print(firstfood['full_nutrients'][0])

# Save data to file
banana_data = "banana_data.txt"
