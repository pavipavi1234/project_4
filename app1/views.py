from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mahi(request):
    return HttpResponse('<H1><marquee>MAHI IS A GOOD PALYER</marquee></H1>')
def app1(request):
    return render(request,'mahi.html')
    