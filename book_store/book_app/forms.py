from book_app.models import BookStoreModel
from django import forms

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = ['id', 'book_name', 'author', 'category']

