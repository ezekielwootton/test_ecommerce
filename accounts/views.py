from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        # validate user registration information
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save the users information
            user = form.save()
            # log the user into the site
            login(request, user)
            # redirect the user to products page
            return redirect('products:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        # validate the users login information
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # retrieve user information
            user = form.get_user()
            # log the user into the site
            login(request, user)
            # redirect the user to the products page
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('products:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('products:list')

