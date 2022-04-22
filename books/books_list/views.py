from django.shortcuts import render,redirect,get_object_or_404

from .forms import BookModel
from .models import Book,Author



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



def create(request):
    if request.method == "POST":
        form = BookModel(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("show_book", book_id=book.id)
    else:
        form = BookModel()
        return render(request, "books_list/create.html", context={"form": form})

def edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookModel(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect("show_book", book_id=book.id)
    else:
        form = BookModel(instance=book)
        return render(request, "books_list/create.html", context={"form": form})


def delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("index")















