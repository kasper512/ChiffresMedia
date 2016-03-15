from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getMessages$', views.getMessages, name='getMessages'),
    url(r'^sendMessage$', views.sendMessage, name='sendMessage'),

    url(r'^login$', views.login, name='login'), 
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),

    url(r'^sendPublicKey$', views.sendPublicKey, name='sendPublicKey'),
]