from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image_input/', views.search_image, name='image_input'),
]