# chat_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('', views.chat_view, name='chat'),  # Use an empty string '' for the chat view
]
