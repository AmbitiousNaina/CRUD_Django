from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm

def list(request):
    books = Book.objects.all()
    return render(request, 'book_entry/list.html', {'books': books})

def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BookForm()
    return render(request, 'book_entry/add.html', {'form': form})

def update(request, pk=0):
    if request.method == "GET":
        if pk == 0:
            return redirect('list')  # Redirect to list if no pk provided
        else:
            book = Book.objects.get(pk=pk)
            form = BookForm(instance=book)
            return render(request, "book_entry/update.html", {'form': form})
    else:
        if pk == 0:
            return redirect('list')  # Redirect to list if no pk provided
        else:
            book = Book.objects.get(pk=pk)
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                messages.success(request, 'Book updated successfully!')
            else:
                messages.error(request, 'Failed to update book. Please check the form.')
            return redirect('list')


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('list')
    return render(request, 'book_entry/delete.html', {'book': book})
