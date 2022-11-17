from django.db import models

# Create your models here.
# Create models Category, Partner, Author, Book , BookLoan
class Category(models.Model):
    name = models.CharField(max_length=30)#,default='Comedia' se podria poner
    recommended_age = models.CharField(max_length=6)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Partner(models.Model):    #todo many to many
    first_name = models.CharField(max_length=30, blank= False, null= False)
    last_name = models.CharField(max_length=30, blank= False, null= False)
    dni = models.CharField(max_length=8)
    book = models.ManyToManyField(Book, through='BookLoan')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
#status prestado/devuelto
class BookLoan(models.Model):
    status = models.CharField(max_length=20, blank=False, null=False, default="Prestado")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)



