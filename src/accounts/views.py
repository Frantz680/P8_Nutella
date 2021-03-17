from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm


@login_required
def utilisateurs_views(request):
    # return render(request, "connexion.html")
    return render(request, 'utilisateurs/mon_compte.html')


"""def registrer_views(request):
    form = User()
    return render(request, 'accounts/registrer.html', {'form': form})"""

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, 'Votre compte a été crée avec succès.')
            return redirect('src:home')
    else:
        form = UserForm()


    return render(request, 'accounts/register.html', {'form': form})