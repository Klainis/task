"""djangotask URL Configuration

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
from . import views


urlpatterns = [
    path('register/', views.add_user),
    path('user/delete/', views.delete_user),
    path('authorise/', views.authorise),
    path('vacancy/add/', views.add_vacancy),
    path('vacancy/', views.get_vacancy),
    path('vacancy/delete/', views.delete_vacancy),
    path('skill/add/', views.add_skill),
    path('skill/', views.get_skill),
    path('skill/delete/', views.delete_skill),
    path('vacancy/set/skill/', views.add_skill_to_vacancy),
    path('vacancy/unset/skill/', views.remove_skill_from_vacancy),
    path('user/set/skill/', views.add_skill_to_user),
    path('user/unset/skill/', views.remove_skill_from_user),
    path('vacancy/response/', views.add_response),
    path('response/', views.get_response),
    path('response/delete/', views.delete_response),
]
