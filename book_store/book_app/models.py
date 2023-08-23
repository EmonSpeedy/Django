from django.db import models

# Create your models here.

class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror'),
    )
    
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return f"{self.book_name}...ID => {self.id}"
    

