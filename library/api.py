from ninja import NinjaAPI
from .models import Book
from .models import customer
from .models import Borrow
from .schemas import bookSchema
from .schemas import CreatebookSchema
from .schemas import customerSchema
from .schemas import BorrowSchema
from .schemas import CreatecustomerSchema
from django.shortcuts import get_object_or_404

app=NinjaAPI()

# Book Endpoints
@app.get("/book",response=list[bookSchema])
def get_all_books(request):
    return Book.objects.all()

@app.get("/book/{book_id}", response=CreatebookSchema)
def get_book(request, book_id: int):
    return Book.objects.get(id=book_id)

@app.post("/book", response=bookSchema)
def create_book(request, book:bookSchema):
    new_book = Book.objects.create(**book.dict())
    return new_book

@app.put("/book/{book_id}", response=bookSchema)
def update_book(request, book_id: int, book: bookSchema):
    book_instance = Book.objects.get(id=book_id)
    for attr, value in book.dict().items():
        setattr(book_instance, attr, value)
    book_instance.save()
    return book_instance

@app.delete("/book/{book_id}")
def delete_book(request, book_id: int):
    book_instance = Book.objects.get(id=book_id)
    book_instance.delete()
    return {"success": True}

# customer Endpoints
@app.get("/customer", response=list[customerSchema])
def get_all_user(request):
    return customer.objects.all()

@app.get("/customer/{user_id}", response=CreatecustomerSchema)
def get_user(request, customer_id: int):
    return customer.objects.get(user_id=customer_id)

@app.post("/customer", response=customerSchema)
def create_user(request, customer_data:customerSchema):
    new_user = customer.objects.create(**customer_data.dict())
    return new_user

@app.put("/customer/{user_id}", response=customerSchema)
def update_user(request, customer_id: int, customer_data:customerSchema):
    user_instance = customer.objects.get(user_id=customer_id)
    for attr, value in customer_data.dict().items():
        setattr(user_instance, attr, value)
    user_instance.save()
    return user_instance

@app.delete("/customer/{user_id}")
def delete_user(request, customer_id: int):
    user_instance = customer.objects.get(user_id=customer_id)
    user_instance.delete()
    return {"success": True}

#borrow endpoints

@app.get("/borrows", response=list[BorrowSchema])
def list_borrows(request):
    return Borrow.objects.select_related('customer', 'book').all()

@app.post("/borrow", response=BorrowSchema)
def create_borrow(request, customer_id: int, book_id: int):
    customer_instance = get_object_or_404(customer, pk=customer_id)
    book_instance = get_object_or_404(Book, pk=book_id)
    borrow = Borrow.objects.create(customer=customer_instance, book=book_instance)
    book_instance.is_borrowed = True
    book_instance.save()
    return borrow

@app.post("/return", response=BorrowSchema)
def return_borrow(request, book_id: int):
    borrow = get_object_or_404(Borrow, pk=book_id)
    book = borrow.book
    book.is_borrowed = False
    book.save()
    borrow.delete()
    return {"success": True}

@app.get("/borrow/{borrow_id}", response=BorrowSchema)
def get_borrow(request, book_id: int):
    borrow = get_object_or_404(Borrow, pk=book_id)
    return borrow