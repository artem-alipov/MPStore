"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from homepage  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('directories/', include('directories.urls'), name='directories'),
    path('hp/', include('homepage.urls'), name='hp'),
    path('cart/', include('cart.urls'), name='cart'),
    path('book/', include('book.urls'), name='book'),
    path('profile/', include('user_profile.urls'), name='profile'),
    path('staff/', include('staff.urls'), name='staff'),
    path('success', views.success_page, name='success.html'),
    
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
