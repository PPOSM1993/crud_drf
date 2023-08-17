from django.db import models

from isbn_field import ISBNField
from django.forms import model_to_dict

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200, null=False, blank=False, verbose_name='Category')
    
    def __str__(self):
        return self.category
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

class Language(models.Model):
    language = models.CharField(max_length=200, null=False, blank=False, verbose_name='Language')
    
    def __str__(self):
        return self.language
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['id']

class Binding(models.Model):
    binding = models.CharField(max_length=200, blank=False, null=False, verbose_name='Binding')
    
    def __str__(self):
        return self.binding
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Binding'
        verbose_name_plural = 'Bindings'
        ordering = ['id']

class FormatBook(models.Model):
    format = models.CharField(max_length=200, null=False, blank=False, verbose_name='Format Book')

    def __str__(self):
        return self.format
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Format'
        verbose_name_plural = 'Formats'
        ordering = ['id']

class Author(models.Model):
    name_author = models.CharField(max_length=255, blank=False, null=False, verbose_name='Name Author')
    about_author = models.TextField(max_length=5000, blank=False, null=False, verbose_name='About Author')
    
    def __str__(self):
        return self.name_author

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['id']

class Editorial(models.Model):
    #La editorial y proveedor es lo mismo.
    name_editorial = models.CharField(max_length=200, blank=False, null=False, verbose_name='Editorial')
    rut_editorial = models.CharField(max_length=200, blank=False, null=False, verbose_name='RUT Editorial')
    address_editorial = models.CharField(max_length=200, blank=False, null=False, verbose_name='Address Editorial')
    mail_editorial = models.CharField(max_length=200, blank=False, null=False, verbose_name='Email Editorial')

    def __str__(self):
        return self.name_editorial
        
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editorials'
        ordering = ['id']

class GenderLiterary(models.Model):
    name_gender = models.CharField(max_length=200, blank=False, null=False, verbose_name='Gender Literary')

    def __str__(self):
        return self.name_gender

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Name Gender Literary'
        verbose_name_plural = 'Name Genders Literary'
        ordering = ['id']

class Book(models.Model):
    isbn = isbn = ISBNField(verbose_name='ISBN')
    name_Book = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name Book')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category')
    name_author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Author')
    price = models.IntegerField(blank=False, null=False, verbose_name='Size Book')
    review = models.TextField(max_length=15000, blank=False, null=True, verbose_name='Review')
    size = models.CharField(max_length=9, blank=False, null=False, verbose_name='Size Book')
    language = models.ForeignKey(Language, on_delete=models.PROTECT, blank=False, null=True, verbose_name='Language')
    imgBook = models.ImageField(null=True, blank=True)
    name_gender = models.ForeignKey(GenderLiterary, on_delete=models.PROTECT, blank=False, null=False, verbose_name='Gender Literary')

    
    def __str__(self):  
        return f'Name Book: {self.name_Book}'#, f'ISBN Book: {self.isbn}'
        
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['id']


"""
class Book(models.Model):
    isbn = isbn = ISBNField(verbose_name='ISBN')
    name_Book = models.CharField(max_length=255, blank=False, null=True, verbose_name='Name Book')
    name_author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Author')
    name_gender = models.ForeignKey(GenderLiterary, on_delete=models.PROTECT, blank=False, null=False, verbose_name='Gender Literary')
    review = models.TextField(max_length=15000, blank=False, null=True, verbose_name='Review')
    language = models.ForeignKey(Language, on_delete=models.PROTECT, blank=False, null=True, verbose_name='Language')
    size = models.CharField(max_length=7, blank=False, null=False, verbose_name='Size Book')
    price = models.IntegerField(blank=False, null=False, verbose_name='Size Book')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=False, null=True, verbose_name='Language')
    imgBook = models.ImageField() 
    
    def __str__(self):  
        return f'Name Book: {self.name_Book}', f'ISBN Book: {self.isbn}', f'Author(s): {self.name_author}'
        
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['id']"""