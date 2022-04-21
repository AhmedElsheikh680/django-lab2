from django.urls import path
from .views import index, show,author


urlpatterns =[
    path('', index, name="index"),
    path('<int:book_id>', show, name="show_book"),
    path('author/<int:author_id>', author, name="show_author")
]