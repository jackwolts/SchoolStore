from django.contrib import admin
from django.urls import path
from . import views

from schoolproject import settings
from django.conf.urls.static import static

urlpatterns = [

    path('form',views.form,name='form'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),


]