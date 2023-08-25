from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('theblog.urls')),
    path('members/',include('django.contrib.auth.urls')), #django authentication urls
    path('members/',include('members.urls')), #other urls in members
]
