from django.urls import path
from .views import home, BooksViews, author

urlpatterns = [
    path('', home, name='home'),
    path('books/', BooksViews.as_view(), name='books'),
    path('auther/', author, name='auther')
]

