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

def add_book(request):
    errors = []
    add_check = False
    author_add = False
    if request.POST:
        post = request.POST
        if Book.objects.filter(ISBN = post['ISBN']):
            errors.append('This ISBN has been in BookDB !')
        elif Book.objects.filter(Title = post['Title']):
            errors.append('This Book has been in BookDB !')
        else:
            try:
                author = Author.objects.filter(AuthorID = post['AuthorID'])
                Book.objects.create(
                    ISBN = post['ISBN'],
                    Title = post['Title'],
                    AuthorID = author[0],
                    Publisher = post['Publisher'],
                    PublishDate = post['PublishDate'],
                    Price = post['Price']
                )
                add_check = True
            except IndexError:
                errors.append('Do not find the author!' )
                author_add = True
            except :
                errors.append('Please input by the correct way ! ')
                errors.append('Make sure input all things')
    return render_to_response('add_book.html',locals())
