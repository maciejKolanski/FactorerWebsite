"""Factorer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from FactorerMain import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^userview/?$', views.UserView.as_view(), name='userview'),
    url(r'^about/?$', views.AboutView.as_view(), name='about'),
    url(r'^creators/?$', views.CreatorsView.as_view(), name='creators'),
    url(r'^bruteforce/?$', views.BruteforceView.as_view(), name='bruteforce'),
    url(r'^login/?$', 'django.contrib.auth.views.login'),
    url(r'^logout/?$', 'django.contrib.auth.views.logout'),
    url(r'^register/?$', views.register, name='register'),
    url(r'^success_register/?$', views.SuccessRegisterView.as_view(), name='success_register'),
    url(r'^admin/?', include(admin.site.urls)),
]
