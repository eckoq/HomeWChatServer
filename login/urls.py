from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'auth', views.login, name='auth'),
    url(r'register', views.register, name='register'),
]
