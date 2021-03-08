from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required


@login_required
def utilisateurs_views(request):
    # return render(request, "connexion.html")
    return render(request, 'utilisateurs/mon_compte.html')

