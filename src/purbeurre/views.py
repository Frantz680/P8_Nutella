from django.shortcuts import render, HttpResponse


def utilisateurs_views(request):
    # return render(request, "connexion.html")
    return render(request, 'utilisateurs/mon_compte.html')

