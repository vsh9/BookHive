from ninja import Schema
from datetime import date

class bookSchema(Schema):
    id: int=None
    title: str
    author: str
    is_borrowed:bool=False

class CreatebookSchema(Schema):
    title: str
    author: str
    is_borrowed:bool=False

class customerSchema(Schema):
    user_id: int=None
    name: str
    no_books: int
    mobile_no: str

class CreatecustomerSchema(Schema):
    name: str
    no_books: int
    mobile_no: str

class BorrowSchema(Schema):
    customer: customerSchema
    book: bookSchema
    borrow_date: date