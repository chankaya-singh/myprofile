from django.shortcuts import render
#from django.shortcuts import HttpResponse

# Create your views here.
from .forms import UploadFileForm
#from somewhere import handle_uploaded_file
from django.http.response import HttpResponseRedirect

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

def upload_file(request):
    if request.method =='POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url')
    else:
        form = UploadFileForm()
    return render(request,'upload.html', {'form':form})
        