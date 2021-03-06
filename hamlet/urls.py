from django.urls import path
from . import views

app_name = 'aler'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('blog', views.blog, name = 'blog'),
    path('agents', views.agents, name = 'agents'),
    path('properties', views.properties, name = 'properties'),
]