import json

library = {
    "name": "City Library",
    "books": [
        {"title": "Book A", "author": "Author X", "year": 2005},
        {"title": "Book B", "author": "Author Y", "year": 2010},
        {"title": "Book C", "author": "Author Z", "year": 2015}
    ]
}

with open("library.json","w") as f:
    json.dump(library,f)

with open("library.json","r") as f:
    data=json.load(f)
    books = data["books"]
    for book in books:
       if book["year"]>2008:
            print(book["title"])
