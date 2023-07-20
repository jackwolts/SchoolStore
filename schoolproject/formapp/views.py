from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def form(request):
  if request.method == 'POST':
      username=request.POST['username']
      age=request.POST['age']
      email = request.POST['email']
      user=auth.authenticate(username=username,age=age,email=email)

      if user is not None:
          auth.login(request,user)
      return redirect('home')


  return render(request,"form.html")

def home(request):

    return render(request,"home.html")
def logout(request):
        return HttpResponseRedirect('/')
        return render(request, ".html")




