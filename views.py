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

