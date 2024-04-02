from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

@xframe_options_sameorigin
@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')
