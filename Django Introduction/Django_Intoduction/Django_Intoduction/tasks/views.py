from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# Fuctune Base View:
# 1. A function that has one or more params
# 2. Returns a response

def index(request):
    content = "It works!"
    return HttpResponse(content)
