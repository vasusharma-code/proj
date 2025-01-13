# chat_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Sign Up view
def sign_up(request):
    # Implement sign-up logic
    return render(request, 'chat_app/sign_up.html')  # Update the template path

# Login view
def login_view(request):
    # Implement login logic
    return render(request, 'chat_app/login.html')  # Update the template path

# Chat view
def chat_view(request):
    # Implement chat page logic
    return render(request, 'chat_app/chat.html')  # Update the template path

# Chat view
def chat_view(request):
    # Hardcode two random users for simplicity
    users = [
        {'id': 1, 'username': 'User1'},
        {'id': 2, 'username': 'User2'},
    ]
    
    # Pass the users to the template
    return render(request, 'chat_app/chat.html', {'users': users})