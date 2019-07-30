from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from .forms import RegistrationForm


def registration_view(request):

    if request.method == 'POST':

        form = RegistrationForm(data=request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = True
            user.save()

            if user:
                login(request, user)

            return redirect(reverse('products:list'))

    else:
        form = RegistrationForm()

    return render(request, 'accounts/registration.html', {'form': form})

