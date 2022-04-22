from django import forms
from .models import Book

class BookModel(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "publish_date", "author", "price", "appropriate"]