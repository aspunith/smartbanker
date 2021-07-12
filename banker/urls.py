from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('instruction.html', views.instruct, name='instruction'),
    path('',views.index, name='index'),
    path('submit',views.submit, name='submit'),
    path('index.html', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
]