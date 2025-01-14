import requests
import json

api_url = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=R9RSHuxrGmLLXRwgPCV11WGa1huyK6iA/"

def jprint(obj): 
    text = json.dumps(obj, indent=4)
    print(text)

class Book: 

    #GET ALL/DEFAULT 
    @classmethod
    def get_all(cls):
        response = requests.get(api_url)

        page_results = response.json()['results']

        home_books = []

        for books in page_results:
            book_data = {
                'isbn': books['isbns'][0]['isbn10'] if len(books['isbns']) > 0 else None,
                'title': books['title'],
                'author': books['author'],
                'description': books['description'],
                'publisher': books['publisher']
            }
            home_books.append(book_data)
        print(home_books)
        return home_books
    
    #SEARCH BY TITLE
    
    #SEARCH BY AUTHOR