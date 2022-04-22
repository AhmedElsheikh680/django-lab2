from django.urls import path
from .views import index, show,author,create, edit,delete


urlpatterns =[
    path('', index, name="index"),
    path('<int:book_id>', show, name="show_book"),
    path('author/<int:author_id>', author, name="show_author"),
    path('create', create, name="create_book"),
    path('<int:book_id>/edit', edit, name="edit_book"),
    path('<int:book_id>/delete', delete, name="delete_book")
]