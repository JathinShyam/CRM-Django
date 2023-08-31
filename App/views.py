from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record


def home(request):

    records = Record.objects.all()
    # Checking whether user is authenticated or not
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login user if not login previously
            login(request, user)
            messages.success(request, " Successfully Logged in!")
            return redirect('home')
        else:
            messages.success(request,"Error!")
            return redirect('home')
    else:
        # user is already logged in
        return render(request, 'home.html', {'records' : records})



def logout_user(request):
    logout(request)
    messages.success(request, "Logout Success!")
    return redirect('home')
