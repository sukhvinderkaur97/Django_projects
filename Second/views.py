from django.shortcuts import render

def xyz(request):
    return render(request, 'a.html')

def abc(request):
    return render(request, 'b.html')
def bcd(request):
    return render(request, 'index.htm')