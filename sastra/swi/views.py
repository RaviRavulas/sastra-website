from django.shortcuts import render
from .models import students
from django.http import HttpResponse
from .forms import newdetails

# Create your views here.
def home(request):
    return render(request,'sas.html')
def login(request):
    return render(request,'login.html')
def data(request):
    return render(request,'check.html')
def enter(request):
    pas=request.POST.get('password')
    if int(pas)==8435:
        s=students.objects.all()
        return render(request,'details.html',{'x':s})
    else:
        return HttpResponse('INVALID PASSWORD')
def portal(request):
    reg=request.POST.get('regno')
    s=students.objects.filter(regno=reg)
    pas=request.POST.get('password')
    for i in s: 
        if int(pas)==i.password:
            return render(request,'details.html',{'x':s})
        else:
            return HttpResponse('INVALID PASSWORD')
    return HttpResponse('INVALID REGNO')
            
def new(request):
    if request.method=='POST':
        form=newdetails(request.POST)
        if form.is_valid():
             name=form.cleaned_data['name']
             password=form.cleaned_data['password']
             regno=form.cleaned_data['regno']
             cgpa=form.cleaned_data['cgpa']
             attendance=form.cleaned_data['attendance']
             n=students()
             n.name=name
             n.password=password
             n.regno=regno
             n.cgpa=cgpa
             n.attendance=attendance
             n.save()
             return HttpResponse('ADDED')
   
    else:
        form=newdetails()
    return render(request,'enter.html',{'form':form})
    
    
