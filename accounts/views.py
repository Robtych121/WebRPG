from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ModificationForm

# Create your views here.
@login_required()
def userControlPanel(request):

    user = User.objects.get(email=request.user.email)

    return render(request, "ucp.html", {"profile": user})


@login_required
def profile(request):
    if request.method == "POST":
        form = ModificationForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(userControlPanel)
    else:
        form = ModificationForm(instance=request.user)

    return render(request, "update-profile.html", {'form':form})