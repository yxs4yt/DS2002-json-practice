# json-practice

Get practice working with JSON:

- [`jq`](jq)
- [Python3](python)
- [data/](data)
- [jsonlint](https://jsonlint.com/)
- [jqplay](https://jqplay.org/#)

## Reading and Fetching JSON

### Reading JSON from a file

In `bash` you can read a file using `cat` and simply pass the output to `jq` with a `|` pipe like this:

```
cat data/simple.list.json | jq -r
```

In Python you can read a file into a variable, which can then be treated like a data object:

```
import json

# Open the JSON file
with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)
```

### Fetching JSON from a remote source

Some `curl` examples for fetching JSON from a remote data source then passed to `jq`:

```
curl https://api.github.com/users/schacon/repos | jq -r
curl https://api.github.com/repos/nmagee/ds2002-course/branches | jq -r
```

In Python, either `requests` or `urllib3` can GET remote data to populate a variable:

```
import requests

url = "https://api.github.com/users/schacon/repos"
response = requests.get(url)

data = response.json()
```

## 1. Compare with XML

```
{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}
```

The same text expressed as XML:

```
<menu id="file" value="File">
  <popup>
    <menuitem value="New" onclick="CreateNewDoc()" />
    <menuitem value="Open" onclick="OpenDoc()" />
    <menuitem value="Close" onclick="CloseDoc()" />
  </popup>
</menu>
```

Drawn from https://json.org/example.html

## 2. Work with `jq`

Review the contents of [jq/README.md](jq/README.md) and practice using the CLI to parse JSON.

## 3. Work with Python

Review the contents of [python/README.md](python/README.md) and practice using Python to parse JSON.

