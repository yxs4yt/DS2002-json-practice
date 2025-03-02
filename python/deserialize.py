import json

# Opening JSON file
f = open('../data/data.json')

# returns JSON object as a dict
data = json.load(f)

# Iterate through the array and fetch name
for i in data['employees']:
    print(i['name'])

# Closing file
f.close()