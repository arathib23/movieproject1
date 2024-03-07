"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from details import views

app_name="details"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name="base"),
    path('home',views.home,name="home"),
    path('addmovies',views.addmovies,name="addmovies"),
    path('moviedetail/<int:p>',views.moviedetail,name="moviedetail"),
    path('moviedelete/<int:p>',views.moviedelete,name="moviedelete"),
    path('movieedit/<int:p>',views.movieedit,name="movieedit"),

]
