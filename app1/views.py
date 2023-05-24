from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_strings(request):
    return HttpResponse('<h1>This String response is returned by app1</h1>')

def app1_htmlpage(request):
    return render(request,'app1_htmlpage.html')