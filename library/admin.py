from django.contrib import admin
from .models import Book , customer, Borrow

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_borrowed')
    search_fields = ('title', 'author')

@admin.register(customer)
class userAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'no_books', 'mobile_no')
    search_fields = ('name', 'mobile_no')

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'borrow_date')
    search_fields = ('customer__name', 'book__title')
