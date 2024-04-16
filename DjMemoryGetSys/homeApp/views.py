from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse

from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

@xframe_options_sameorigin
@login_required()
def home(request):
    return render(request, 'home.html')

@xframe_options_sameorigin
@login_required()
def index(request):
    return render(request, 'index.html')


@xframe_options_sameorigin
@login_required()
def catch_all(request, route):
    return redirect(reverse('loginApp:login'))