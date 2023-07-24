import requests
import json


  
# requestUrl = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=R9RSHuxrGmLLXRwgPCV11WGa1huyK6iA"
  
# requestHeaders = {
#     "Accept": "application/json"
#   }

# response = requests.get(requestUrl, headers=requestHeaders)

def jprint(obj):
    text = json.dumps(obj, indent=4)
    print(text)

response2 = requests.get("https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=R9RSHuxrGmLLXRwgPCV11WGa1huyK6iA&author=Dana%Simpson")

# response = requests.get("https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=R9RSHuxrGmLLXRwgPCV11WGa1huyK6iA")

titles = response2.json()['results']
# jprint(titles)

one_author_results =[]

for one_author in titles:
    book_data = {
        'title': one_author['title'],
        'author': one_author['author'],
        'description': one_author['description'],
        'publisher': one_author['publisher'],
        'isbn': one_author['isbns'][0]['isbn10'] if len(one_author['isbns']) > 0 else None
    }
    one_author_results.append(book_data)

print("Number of results:")
print(len(one_author_results))
jprint(one_author_results)


# all_titles = []

# for all_books in titles: 
#     results = all_books['title']
#     all_titles.append(results)

# print("Titles in database")
# print(all_titles)


# print(response2.status_code)

# jprint(response2.json())
