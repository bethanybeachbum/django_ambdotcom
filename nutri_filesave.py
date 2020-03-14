
import requests
import json
import pprint

url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
headers = {
    "accept": "application/json",
    "x-app-id":"a960790f",
    "x-app-key":"399046c67a2d31b9d2b1b67f7492e7de",
    "x-remote-user-id":"bethanybeachbum",
    }
payload={"query":"banana"}
body={"json"}
r = requests.post(url, headers=headers, data=payload, json=body)

# print the status code
print(f"Second Status code: {r.status_code}")

filename = "banana.txt"

with open(filename, 'w') as file_object:
    file_object.write(r.text)

with open(filename, 'r') as file_object:
    contents = file_object.read()

# print(contents)

# with open('banana.txt', 'wt') as out:
#    res = json.dump(obj, out, sort_keys=True, indent=4, separators=(',', ': '))  


formatted_obj = json.dumps(r, indent=4, separators=(',', ': '))
print(formatted_obj)      
