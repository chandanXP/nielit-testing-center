from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from pyexpat.errors import messages
from .forms import SignupForm


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('success')
        else:
            # Display an error message
            messages.error(request, 'Invalid login credentials')

    return render(request, 'authentication/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('auth/registration')
    else:
        form = SignupForm()
    return render(request, 'authentication/signup.html', {'form': form})


def registration_success(request):
    return render(request, 'authentication/registration_success.html')


