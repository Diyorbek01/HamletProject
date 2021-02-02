from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import loginForm, registerForm


def registration(request):
    if request.method == 'POST':
        register_form = registerForm(request.POST)
        first_name = register_form.cleaned_data['first_name']
        last_name = register_form.cleaned_data['last_name']
        email = register_form.cleaned_data['email']
        username = register_form.cleaned_data['username']
        password1 = register_form.cleaned_data['password1']
        password2 = register_form.cleaned_data['password2']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
        else:
            messages.info(request,"Passwords are not valid!")
            return redirect('registration')
        return redirect('../' + username)
    else:
        register_form = registerForm()
    return render(request, "accounts/sign_up.html", {'register_form': register_form})

def login(request):
    if request.method == 'POST':
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('../' + username)
        else:
            messages.info(request, "Username or password is not valid!")
            return redirect('sign_in')
    else:
        login_form = loginForm()
    return render(request, 'accounts/sign_in.html', {'login_form': login_form})


def logout(request):
    auth.logout(request)
    return redirect('/')

