from django.shortcuts import render
from .models import Book


def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    
    if not pub_date:
        books = Book.objects.all().order_by('pub_date')
        context = {
            'books': books
        }
        return render(request, template, context)
    
    books = Book.objects.all().filter(pub_date=pub_date)
    # ошибка формата
    
    prev_book = Book.objects.all().filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    prev_date = prev_book.pub_date if prev_book else None
    
    next_book = Book.objects.all().filter(pub_date__gt=pub_date).order_by('pub_date').first()
    next_date = next_book.pub_date if next_book else None 
    
    context = {
        'books': books,
        'prev_date': prev_date,
        'next_date': next_date
    }

    return render(request, template, context)