from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Books, Auther


# Create your views here.

def home(request):
    return render(request, 'home.html')

# def books(request):
#     temp = Books.objects.all()
#     return render(request, 'books.html', {'datas': temp})

def author(request):
    authers = Auther.objects.all()
    return render(request, 'auther.html', {'authers': authers})

class BooksViews(TemplateView):
    def get(self, request):
        context = {}
        temp = Books.objects.all()
        context['data'] = temp
        return render(request, 'books.html', context)