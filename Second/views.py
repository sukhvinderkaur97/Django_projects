from django.shortcuts import render
from .models import Student

def xyz(request):
    return render(request, 'a.html')

def abc(request):
    P = Student.objects.all().values()
    return render(request, 'b.html', {'std':P})

def pqr(request):
    return render(request, 'c.html')

def lmn(request):
    return render(request, 'd.html')