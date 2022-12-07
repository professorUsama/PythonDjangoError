# from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.


languages = {
    'python': "This page is about to python programming language",
    'php': "This page is about to PHP programming language",
    'c++': "This page is about to C++ programming language",
    'javascript': "This page is about to JavaScript programming language",
}

def news_page(request, topic):
    result = languages[topic]
    return HttpResponse(result)

def programming_page(request,page_num):
    language_key = list(languages.keys())
    return HttpResponseRedirect(language_key[page_num])
