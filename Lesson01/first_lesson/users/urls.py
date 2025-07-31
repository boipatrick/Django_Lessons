from django.urls import path
from . import views

app_name = 'users'  # This is the namespace for the users app

urlpatterns = [
   
    path('register/', views.register_view, name='register'), # This is the URL for registering new users
   
]

