from django.shortcuts import render


def home(request):
    return render(request, 'home.html') 

def travel(request):
    return render(request, 'travel.html')

def mycareer(request):
    return render(request, 'mycareer.html')

def book(request):
    return render(request, 'book.html') 