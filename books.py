from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


# class Book:
#     id: int
#     title: str
#     author: str
#     description: str
#     rating: int
#     published_date: int

#     def __init__(self, id, title, author, description, rating, published_date):
#         self.id = id
#         self.title = title
#         self.author = author
#         self.description = description
#         self.rating = rating
#         self.published_date = published_date


# BOOKS = [
#     Book(1, "Computer Science Pro", "codingwithroby", "A very nice book!", 5, 2030),
#     Book(2, "Be Fast with FastAPI", "codingwithroby", "A great book!", 5, 2030),
#     Book(3, "Master Endpoints", "codingwithroby", "A awesome book!", 5, 2029),
#     Book(4, "HP1", "Author 1", "Book Description", 2, 2028),
#     Book(5, "HP2", "Author 2", "Book Description", 3, 2027),
#     Book(6, "HP3", "Author 3", "Book Description", 1, 2026),
# ]


BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return


@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
