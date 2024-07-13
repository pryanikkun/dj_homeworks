from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime
from .models import Book


def books_view(request, pub_date=None):
    template = 'books/books_list.html'

    next_date = None
    prev_date = None

    if pub_date:
        books_dates = list(Book.objects.order_by(
            'pub_date'
        ).distinct().values_list(
            'pub_date', flat=True
        ))
        if pub_date in books_dates:
            books = Book.objects.filter(
                pub_date=pub_date
            )
            next_date = books_dates[books_dates.index(pub_date) + 1] \
                if pub_date != books_dates[len(books_dates)-1] else None
            prev_date = books_dates[books_dates.index(pub_date) - 1] \
                if pub_date != books_dates[0] else None
        else:
            books = []
    else:
        books = Book.objects.all()

    context = {
        'books': books,
        'next_date': next_date,
        'prev_date': prev_date,
    }

    return render(request, template, context)
