from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def about_me(request):
    return render(request, 'home/aboutme.html')


def education(request):
    return render(request, 'home/education.html')

def hoby(request):
    return render(request, 'home/hoby.html')

def work_exp(request):
    return render(request, 'home/work_exp.html')