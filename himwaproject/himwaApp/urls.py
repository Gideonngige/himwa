from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('payment/', views.payment, name='payment'),
    path('members/', views.members, name='members'),
]