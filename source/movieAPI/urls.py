"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from .views import searchForMovieView, findMovieView, compareMoviesView, compareMovieListView, createContent

urlpatterns = [
    url('search/', searchForMovieView, name='search'),
    url('find/', findMovieView, name='find'),
    url('compare/list/', compareMovieListView, name='compare list'),
    url('compare/', compareMoviesView, name='compare'),
    url("create/", createContent, name="create content")

]