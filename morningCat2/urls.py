"""morningCat2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='my-home'),
    path('about/', views.about, name='my-about'),
    path('gallery/', views.gallery, name='my-gallery'),
    path('gallery_single/', views.gallery_single, name='my-gallery-single'),
    path('services/', views.services, name='my-services'),
    path('sample_inner_page/', views.sample_inner_page, name='my-sample-inner-page'),
    path('contact/', views.contact, name='my-contact'),
    path('register/', views.register, name='my-register'),

]
