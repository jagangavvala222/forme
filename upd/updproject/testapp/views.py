from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from testapp.models import PythonDocument
from testapp.models import DjangoDocument
from testapp.models import MachinelearningDocument
from testapp.models import ResumeDocument
from testapp.forms import DocumentForm


def home(request):#python
    documents = PythonDocument.objects.all()
    return render(request, 'testapp/home.html', { 'documents': documents })
def home1(request):#django
    documents = DjangoDocument.objects.all()
    return render(request, 'testapp/home1.html', { 'documents': documents })
def home2(request):#Machine Learning
    documents = MachinelearningDocument.objects.all()
    return render(request, 'testapp/home2.html', { 'documents': documents })
def home3(request):#Machine Learning
    documents = ResumeDocument.objects.all()
    return render(request, 'testapp/home3.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'testapp/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'testapp/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'testapp/model_form_upload.html', {
        'form': form
    })
