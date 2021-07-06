# from django.http  import HttpResponse
# from django.shortcuts import render,redirect,Http404
# from .models import Poster,Category,Location,Image


# # Create your views here.
# def welcome(request):
#     images= Image.objects.all()
#     return render(request,'all-gallery/gallery.html',{'images':images})

# # def gallery(request):
# #     return render(request,'all-gallery/gallery.html')    

# def review(request):
#     images=Image.objects.all()
#     description=Image.objects.all()
#     category=Image.objects.all()
#     location=Image.objects.all()
#     return render(request,'all-gallery/gallery-review.html',{"images":images,"description":description,"category":category,"location":location})


# def image(request,image_id):
#     try:
#         image = Image.objects.get(id = image_id)
#     except Image.DoesNotExist:
#         raise Http404()
    
#     return render(request,"all-gallery/image.html", {"image":image})


# def search_gallery(request):

#     if 'gallery' in request.GET and request.GET["gallery"]:
#         search_term = request.GET.get("gallery")
#         searched_gallery = Image.search_by_category(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-gallery/search.html',{"message":message,"articles": searched_gallery})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-gallery/search.html',{"message":message})    


# def get_image_by_location(request):
#     pass

# def copy_to_clipboard(request):
#     pass

# def image_location(request, location):
#     images = Image.filter_by_location(location)
#     print(images)
#     return render(request, 'pictures/location.html', {'location_images': images})
from django.shortcuts import render
from .models import Image, Location


def welcome(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'all-gallery/gallery.html', {'images': images[::-1], 'locations': locations})


def image(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'all-gallery/location.html', {'location_images': images})


def search_gallery(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'all-gallery/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'all-gallery/search_results.html', {"message": message})
def review(request):
    pass
def image(request):
    pass

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'all-gallery/location.html', {'location_images': images})