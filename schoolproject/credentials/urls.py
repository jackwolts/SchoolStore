from . import views
from django.urls import path

from schoolproject import settings
from django.conf.urls.static import static

urlpatterns = [

    path('login',views.login,name='login'),

]