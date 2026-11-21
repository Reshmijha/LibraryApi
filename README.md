# Library API

A simple REST API built with Python and Flask to manage a list of books. You can add, view, update, delete and search books by author.

I made this project to practice the basics of building APIs: routing, handling JSON requests, validating input and returning proper status codes. Data is kept in memory, so there is no database to set up. Everything resets when the server restarts.

## Tech used

- Python 3
- Flask

## Project structure

```
LibraryApi/
├── app.py              # app setup and error handlers
├── data.py             # in-memory data and CRUD functions
├── validators.py       # request body validation
├── routes/
│   ├── __init__.py
│   └── books.py        # book endpoints
├── requests.http       # sample requests for testing
└── requirements.txt
```

## Getting started

Clone the repo

```
git clone https://github.com/<your-username>/LibraryApi.git
cd LibraryApi
```

Create a virtual environment and install Flask

```
python -m venv venv
```

Windows:
```
venv\Scripts\activate
```

Linux / Mac:
```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

Start the server

```
python app.py
```

The API will be running at `http://localhost:5000`

## Endpoints

| Method | Endpoint                 | Description            |
|--------|--------------------------|------------------------|
| GET    | `/api/books`             | Get all books          |
| GET    | `/api/books?author=name` | Search books by author |
| GET    | `/api/books/<id>`        | Get a single book      |
| POST   | `/api/books`             | Add a new book         |
| PUT    | `/api/books/<id>`        | Update a book          |
| DELETE | `/api/books/<id>`        | Delete a book          |

## Examples

### Get all books

```
GET /api/books
```

Response `200 OK`

```json
[
  {
    "id": 1,
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "published_year": 1988,
    "price": 299,
    "available": true
  }
]
```

### Add a book

```
POST /api/books
Content-Type: application/json
```

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "published_year": 2018,
  "price": 499
}
```

Response `201 Created`

```json
{
  "id": 4,
  "title": "Atomic Habits",
  "author": "James Clear",
  "published_year": 2018,
  "price": 499,
  "available": true
}
```

### Update a book

```
PUT /api/books/1
Content-Type: application/json
```

```json
{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "published_year": 1988,
  "price": 249,
  "available": false
}
```

Response `200 OK` with the updated book.

### Delete a book

```
DELETE /api/books/2
```

Response `204 No Content`

### Using curl

```
curl http://localhost:5000/api/books

curl -X POST http://localhost:5000/api/books -H "Content-Type: application/json" -d "{\"title\": \"Atomic Habits\", \"author\": \"James Clear\", \"published_year\": 2018, \"price\": 499}"

curl -X DELETE http://localhost:5000/api/books/2
```

You can also use Postman, or open `requests.http` in VS Code with the REST Client extension.

## Validation

POST and PUT requests are checked before saving:

- `title` is required (max 100 characters)
- `author` is required
- `published_year` must be between 1450 and 2100
- `price` can't be negative
- `available` must be true or false

If something is wrong the API returns `400 Bad Request` with a list of errors:

```json
{
  "errors": [
    "title is required",
    "published_year must be a number between 1450 and 2100"
  ]
}
```

If a book id doesn't exist you get `404 Not Found`:

```json
{
  "error": "Book with id 99 not found"
}
```

## Things I might add later

- SQLite database instead of in-memory list
- Pagination for the books list
- Unit tests with pytest
- Authentication
