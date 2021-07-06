from django.http  import HttpResponse
from django.shortcuts import render,redirect,Http404
from .models import Poster,Category,Location,Image




def welcome(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'all-gallery/gallery.html', {'images': images[::-1], 'locations': locations})


def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'all-gallery/location.html', {'location_images': images})


def search_gallery(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'all-gallery/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'all-gallery/search.html', {"message": message})
def review(request):
    pass
def image(request):
    pass