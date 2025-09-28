from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def home_page(request):
    return HttpResponse("you made it!")