from django.contrib import admin
from .models import Poster,Category,Location,Image
# Register your models here.

# class GalleryAdmin(admin.ModelAdmin):
#     filter_horizontal=('Category','Location')

admin.site.register(Poster)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)