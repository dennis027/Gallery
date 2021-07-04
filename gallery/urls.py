from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
url(r'^$', views.welcome,name='welcome'),
url(r'^image/(\d+)',views.image,name='image'),
url(r'^search/', views.search_gallery, name='search_gallery'),
url(r'^review/', views.review, name='review'),


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)