from django.shortcuts import render
from .models import Book,Author
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'books_list/index.html', context=context)


def show(request, book_id):
    # book = Book.objects.get(id= book_id)
    book = get_object_or_404(Book, id=book_id)
    context = {
        "book": book
    }
    return render(request, 'books_list/show.html', context=context)


def author(request, author_id):

    author = Author.objects.get(id=author_id)
    books =author.book_set.all()

    context =  {
        "author": author,
        "books": books
    }

    return render(request, 'books_list/author.html', context=context)