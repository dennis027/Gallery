from django.http  import HttpResponse
from django.shortcuts import render,redirect
from .models import Poster,Category,Location,Image

# Create your views here.
def welcome(request):
    images= Image.objects.all()
    return render(request,'all-gallery/gallery.html',{'images':images})

# def gallery(request):
#     return render(request,'all-gallery/gallery.html')    