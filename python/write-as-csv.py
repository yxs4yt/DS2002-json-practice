#!/usr/bin/env python3

import json

# Open the JSON file
with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

f = open('data/chacon.repos.csv', 'a')
for d in data:
    line = (d['name'], ",", d['html_url'], ",", d['updated_at'], ",", d['visibility'], "\n")
    f.writelines(line)
f.close()

# f = open("demofile3.txt", "a")
# f.writelines(["See you soon!", "Over and out."])
# f.close()
