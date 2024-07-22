from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    is_borrowed=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class customer(models.Model):
    user_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    no_books=models.IntegerField(default=0)
    mobile_no=models.CharField(max_length=15,null=True)
    borrows= models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    
class Borrow(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} borrowed {self.book.title}"