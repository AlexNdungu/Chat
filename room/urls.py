from django.urls import path
from . import views

#Here we will write the paths

urlpatterns = [
    path('rooms/', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='roomInd'),
]