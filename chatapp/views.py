from django.shortcuts import render

# Create your views here.

def home(request,uid):
    return render(request,'index.html')