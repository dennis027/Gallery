from django.http  import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def welcome(request):
    return render(request,'all-gallery/gallery.html')

# def gallery(request):
#     return render(request,'all-gallery/gallery.html')    