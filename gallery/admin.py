from django.contrib import admin
from .models import Poster,Category,Location,Image
# Register your models here.

admin.site.register(Poster)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)