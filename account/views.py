from django.shortcuts import render
from django.http import HttpResponse
from account.forms import RegistrationForm
from django.contrib.auth import login as dj_logon, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return HttpResponse("You are authenticated")
    else:
        form = RegistrationForm
        if request.method == "POST" or request.method == "post":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save();
                return HttpResponse("Your account has been created successfully")
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):
    if request.user.is_authenticated:
        return HttpResponse("Your are already login")
    else:
        if request.method == "POST" or request.method == "post":
            username=request.POST.get('username');
            password=request.POST.get('password')
            customer=authenticate(request, username=username, password=password)
            if customer is not None:
                dj_logon(request, customer)
                return HttpResponse("Successfully Login")
            else:
                return HttpResponse("Credential ot match")
        else:
            return render(request,"login.html")

