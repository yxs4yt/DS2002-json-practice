#!/usr/bin/env python3
import json
import pandas as pd

# Read in the JSON data from the file 'data/schacon.repos.json'
with open('data/schacon.repos.json', 'r') as file:
    repos = json.load(file)

# Normalize the JSON data into a pandas DataFrame
df = pd.json_normalize(repos)

# Select only the four required fields:
# name, html_url, updated_at, visibility
df_subset = df[['name', 'html_url', 'updated_at', 'visibility']]

# Export the first 5 lines to chacon.csv without headers and index
df_subset.head(5).to_csv('chacon.csv', index=False, header=False)
