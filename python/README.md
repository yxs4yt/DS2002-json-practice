# JSON in Python

As you may already recognize, JSON is quite similar to dictionaries in Python. 
Since JSON is the "language" for machinized exchanges of data, it is important
to be able to retrieve, parse, and generate JSON using Python.

## Example 1 - Read a JSON file and parse the tree

There is a file in the `/data` directory of this repository named `book.json` with a single book entry in it. Let's read in that file and parse it using Python:

```
import os
import json

with open('../data/book.json','r') as file:
  data = json.load(file)

print(data['author'])
print(data['genre'])

for d in data['genres']:
  print(d)

file.close()
```

Note that the file contains only ONE entry, so no loops are required to immediately start fetching out Key-Value pairs.

In the case of the array of `genres` tags, a for-loop is useful.

### Another Example

Take `data.json` in the `data/` directory. How do we parse a multi-entry object within the tree?

```
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
```


## Example 2 - Simple Pull and Parse JSON

```
import requests

url = "https://api.github.com/repos/nmagee/ds2002-course/branches"

response = requests.get(url)

# get out the name objects
for r in response.json():
  print(r['name'])
```

If you run the first three commands of this Python interactively you now have an object populated with all artifacts of the request and other methods.

```
>>> import requests
>>> url = "https://api.github.com/repos/nmagee/ds2002-course/branches"
>>> response = requests.get(url)

>>> response.
response.apparent_encoding     response.history               response.ok                   
response.close(                response.is_permanent_redirect response.raise_for_status(    
response.connection            response.is_redirect           response.raw                  
response.content               response.iter_content(         response.reason               
response.cookies               response.iter_lines(           response.request              
response.elapsed               response.json(                 response.status_code          
response.encoding              response.links                 response.text                 
response.headers               response.next                  response.url
``` 

Some important elements about the request:

- `response.encoding` - `'utf-8'`
- `response.headers.*` - HTTP response headers about the request/reply.
- `response.status_code` - `200` is OK; other status codes indicate errors.
- `response.request.*` - Request method, URL, headers, body, etc. about the original request.
- `response.text` - Text version of the actual data response. Quote-wrapped.
- `response.json()` - Native JSON of the data response. This is often `[ ]` wrapped indicating an array within the response that should be iterated apart.

```
>>> response.json()
[{'name': 'container', 'commit': {'sha': '0caa8d395b834613ef35571ceec8ef01fdbc2518', 'url': 'https://api.github.com/repos/nmagee/ds2002-course/commits/0caa8d395b834613ef35571ceec8ef01fdbc2518'}, 'protected': False}, {'name': 'main', 'commit': {'sha': '4719cdbb60d1a180d2afde1947c097e80c7c13d1', 'url': 'https://api.github.com/repos/nmagee/ds2002-course/commits/4719cdbb60d1a180d2afde1947c097e80c7c13d1'}, 'protected': False}]

>>> payload = response.json()
>>> for p in payload:
>>>   print(p['name'])
container
main
```

## Example 3 - Pull and Parse JSON with Error Handling

This includes a variety of possible errors: HTTP, ReadTimeout, Connection, and RequestException.
Ideally any errors are logged to an external log file, not printed to the screen.

```
import requests

url = "https://api.github.com/repos/nmagee/ds2002-course/branches"

try: 
  response = requests.get(url, timeout=1) 
  response.raise_for_status() 
except requests.exceptions.HTTPError as errh: 
  print("HTTP Error") 
  print(errh.args[0]) 
except requests.exceptions.ReadTimeout as errrt: 
  print("Time out: ", errrt) 
except requests.exceptions.ConnectionError as conerr: 
  print("Connection error: ", conerr) 
except requests.exceptions.RequestException as errex: 
  print("Exception request: ", errex) 
finally:
  response.close()

# get out the name objects
for r in response.json():
  print(r['name'])
```

## Example 4 - Fabricate JSON from Pythonic Data Structures

Take the Python dictionary below:

```
myvals = [{"repo_name":"json-practice", "repo_url":"https://github.com/nmagee/json-practice/"}, {"repo_name":"fastapi-demo", "repo_url":"https://github.com/nmagee/fastapi-demo/"}]
```

You can convert this to JSON using the `.dumps()` method of the `json` library:

```
import json

myvals = [{"repo_name":"json-practice", "repo_url":"https://github.com/nmagee/json-practice/"}, {"repo_name":"fastapi-demo", "repo_url":"https://github.com/nmagee/fastapi-demo/"}]
myjson = json.dumps(myvals)
```

The `myjson` variable now contains JSON encoded data.

Such an object could also be created dynamically, appending key-value tuples into a list using `.extend()` and then converting that into a dictionary with `dict()`:

```
first = ('sape', 4139)
second = ('guido', 4127)
third = ('jack', 4098)

# combine tuples into list. Can .append one by one or .extend all at once
mylist = []
mylist.extend((first, second, third))

# convert to dict
mydict = dict(mylist)
mydict

# convert to JSON
myjson = json.dumps(mydict)
myjson
```
