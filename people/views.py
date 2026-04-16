from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, PeopleUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':

        u_form = UserRegistrationForm(request.POST)
        p_form = PeopleUpdateForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()

            people = user.people
            p_form = PeopleUpdateForm(request.POST, request.FILES, instance=people)
            p_form.save()

            
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        u_form = UserRegistrationForm()
        p_form = PeopleUpdateForm()

    return render(request, 'people/register.html', {'u_form': u_form, 'p_form': p_form})


@login_required
def profile(request):
    user = request.user 
    return render(request, 'people/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        p_form = PeopleUpdateForm(request.POST, request.FILES, instance=request.user.people)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        p_form = PeopleUpdateForm(instance=request.user.people)

    return render(request, 'people/update_profile.html', {'p_form': p_form})


