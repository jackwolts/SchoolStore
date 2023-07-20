from . import views
from django.urls import path

from schoolproject import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.demo,name='index'),

]