# books are stored in memory, so changes are lost when the server restarts

books = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho", "published_year": 1988, "price": 299, "available": True},
    {"id": 2, "title": "Wings of Fire", "author": "A. P. J. Abdul Kalam", "published_year": 1999, "price": 350, "available": True},
    {"id": 3, "title": "Clean Code", "author": "Robert C. Martin", "published_year": 2008, "price": 899, "available": True},
]

next_id = 4


def get_all_books(author=None):
    if author:
        return [b for b in books if author.lower() in b["author"].lower()]
    return books


def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def add_book(data):
    global next_id

    book = {
        "id": next_id,
        "title": data["title"],
        "author": data["author"],
        "published_year": data["published_year"],
        "price": data.get("price", 0),
        "available": True,
    }
    books.append(book)
    next_id += 1
    return book


def update_book(book_id, data):
    book = get_book(book_id)
    if book is None:
        return None

    book["title"] = data["title"]
    book["author"] = data["author"]
    book["published_year"] = data["published_year"]
    book["price"] = data.get("price", book["price"])
    book["available"] = data.get("available", book["available"])
    return book


def delete_book(book_id):
    book = get_book(book_id)
    if book is None:
        return False

    books.remove(book)
    return True
