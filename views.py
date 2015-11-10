from django.http import HttpResponse
from django.shortcuts import render_to_response
from BookDB.models import Author,Book

def bookdb_hello(request):
    return render_to_response('bookdb_hello.html')

def bookdb_begin(request):
    return render_to_response('bookdb_begin.html')

def author_test(request):
    list_all = Author.objects.all()
    return render_to_response('author_list.html', locals())

def search_author(request):
    error = False
    Author_all_list = Author.objects.all()
    if 'author' in request.GET:
        q_author = request.GET['author']
        query = q_author
        if not q_author:
            error = True
        else:            
            Author_find = Author.objects.filter(Name = q_author)
            Book_all = Book.objects.filter(AuthorID = Author_find)
            return render_to_response('author_list.html', locals())
    elif 'delete' in request.GET:
        book_delete = request.GET['delete']
        Author_find = Book.objects.filter(Title = book_delete)[0].AuthorID#!!!
        Book_all = Book.objects.filter(AuthorID = Author_find)
        query = Book_all[0].AuthorID.Name
        Book.objects.filter(Title = book_delete).delete()
        return render_to_response('author_list.html', locals())
    return render_to_response('search_author.html', locals())
