from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def final(request):
    return render(request, 'final.html')

def lk(request):
    return render(request, 'lk.html')

def test(request):
    return render(request, 'test.html')
    
def login(request):
    return render(request, 'login.html')