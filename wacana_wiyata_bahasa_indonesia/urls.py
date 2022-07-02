import django
from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.welcome),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('detail/', include('detail.urls')),
    path('list_blogs/', include('list_blogs.urls')),
] 

urlpatterns += staticfiles_urlpatterns()
