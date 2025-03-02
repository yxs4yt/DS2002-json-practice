# Using `jq`

To install `jq` see [this page](https://jqlang.github.io/jq/).

There is a great resource for learning how to use `jq` effectively called [jqplay](https://jqplay.org/#)

The basics for the CLI or a `bash` script are:

- `jq` expects either text stream data or some other output as its data source. 
- `jq` allows you to filter segments of JSON structurally by object or array.
- `jq` returns a text stream as its output. This can easily be captured into memory, fed into another CLI, or a file.


Assume the following JSON:

```
{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": [
                            "GML",
                            "XML"
                        ]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
```

To fetch the "title" field in the second line, you would first parse the `glossary` object, and then the `title` object within that: 

```
cat ../data/simple.single.json | jq -r '.glossary.title'
```

## Remote JSON

You can also use `curl` to fetch JSON and feed that into JSON as `stdout`:

```
curl https://api.github.com/repos/nmagee/ds2002-course/branches | jq -r .[].name
```

## JSON Arrays

The developer should observe the structure of the data payload returned and parse accordingly.
In the case below, the open square brackets `[]` tell `jq` to iterate over all elements of the array.

```
cat ../data/schacon.repos.json | jq -r .[].name
```

In the case below, you could grab the first item of the array:

```
cat ../data/schacon.repos.json | jq -r .[0].name
```
