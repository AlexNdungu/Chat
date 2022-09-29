from django.urls import path
from . import views

#Here we will write the paths

urlpatterns = [
    path('base/',views.base, name='base' ),
    path('front/',views.front, name='frontPage'),
    path('sign/',views.sign, name='signIn'),
    path('logout/',views.user_logout,name='logout'),

]
