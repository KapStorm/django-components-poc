from django.urls import path

from users import views

urlpatterns = [
    path('', views.users, name='users'),
    path('tailwind/', views.users_tailwind, name='users-tailwind'),
]
