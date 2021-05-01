from django.shortcuts import render
from .forms import FormName

# Create your views here.

def index(request):
    return render(request,'index.html')

def form(request):
    form = FormName()
 
    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")

    return render(request,'form.html',{'form':form})