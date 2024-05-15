"""django_loginDev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, delete, update, add, vaild, view

app_name = 'dataDictionaryApp'

urlpatterns = [
    path('index/', index, name='index'),
    path('delete<int:pk>/', delete, name='delete'),
    path('update<int:pk>/', update, name='update'),
    path('view<int:pk>/', view, name='view'),
    path('add/', add, name='add'),
    path('vaild/', vaild, name='vaild'),
]
