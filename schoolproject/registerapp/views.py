from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            user=User.objects.create_user(username=username,password=password)

            user.save()
            return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')


    return render(request,"register.html")