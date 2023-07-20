from django.contrib import admin
from django.urls import path
from . import views
from schoolproject import settings
from django.conf.urls.static import static

urlpatterns = [

    path('register',views.register,name='register')
]