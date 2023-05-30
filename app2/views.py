from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('<H1>dhoni IS A GOOD PALYER</H1>')

