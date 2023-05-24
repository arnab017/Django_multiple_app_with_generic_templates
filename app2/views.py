from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_strings(request):
    return HttpResponse('<h1>This app2_string respone is returned by app2</h1>')

def app2_htmlpage(request):
    return render(request,'app2_htmlpage.html')