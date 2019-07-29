from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # is_valid returns a boolean but in the background creates a .cleaned_data DICTIONARY so have to use GET()
            username = form.cleaned_data.get('username')
            # Creates a flash message for success. then redirects to home page
            messages.success(
                request, f'Account created for {username}! \n You can Log In now')
            return redirect('login')
            # dont want to stay on the page if information submitted is valid so redirects the flash message and user to home page

    return render(request, 'user/register.html', {'form': form})
    # when called with 'get request' goes to register page which contains a blank register form

# def login(request)
# No need for login function in views.py because login and logout are class based views and were created wtih .asview() fxn


@login_required
def profile(request):
    if request.method == 'POST':
        u_uform = UserUpdateForm(request.POST, instance=request.user)
        p_uform = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_uform.is_valid() and p_uform.is_valid():
            u_uform.save()
            p_uform.save()
            username = u_uform.cleaned_data.get('username')
            messages.success(
                request, f'Account updated for {username}!')
            return redirect('profile')
            # would go to profile page anyways because of the return at the end of the class but should add a redirect to profile
            # so that it doesn't send a post request when reloading after submitting. tldr: good practice

    u_uform = UserUpdateForm(instance=request.user)
    p_uform = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_uform': u_uform,
        'p_uform': p_uform}

    return render(request, 'user/profile.html', context)

def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=form.user)
            return redirect('login')
        else:
            return render(request, 'user/change_password.html', {'form': form})
    else:
        context = {'form': PasswordChangeForm(user=request.user)}
        return render(request, 'user/change_password.html', context)