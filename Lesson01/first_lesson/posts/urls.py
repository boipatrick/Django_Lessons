from django.urls import path
from . import views

app_name = 'posts'  # This is the namespace for the posts app

urlpatterns = [
   
    path('', views.posts_list, name='list'), # This is the URL for the posts list view
    path('<slug:slug>', views.posts_page, name='page'),
]

#Django Pattern Converters
# Slug - matches any slug string consisting of ASCII letters or numbers