from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("Hello World")
    return render(request,'home.html')

def add(request):
    val1 = request.POST['Num1']
    val2 = request.POST["Num2"]
    res = int(val1)+int(val2)

    return render(request,'result.html', {'result':res})