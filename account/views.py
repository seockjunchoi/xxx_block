from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
#from .models import User
from django.contrib.auth import get_user_model

# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html', {})
    return HttpResponseRedirect(reverse("login"))

def forgot_passwd(request):
    return render(request, 'account/forgot_password.html', {})

@login_required
def profile(request):

    return render(request, 'profile.html', {})

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("main"))
    if request.method == "POST":
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            User = get_user_model()
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            User.objects.filter(username=username).update(email=email, first_name=phone, is_active='1')
        return HttpResponseRedirect(reverse("main"))
    return render(request, 'account/register.html', {})