from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

import requests, json

from purbeurre.models import Category_product, Name


def home(request):

    return render(request, "index.html")


def search(request):

    search_user = request.GET.get('search_user')
    print("ok", search_user)

    try:
        product = Name.objects.filter(name_product=search_user).first()
        substitutes = Name.objects.filter(category=product.category, nutrition_grade__lt=product.nutrition_grade).order_by("nutrition_grade")

        paginator = Paginator(substitutes, 6)
        page = request.GET.get('page')
        alt_products = paginator.get_page(page)

        context = {
        	'alt_products': alt_products,
        	'paginate': True,
            'title': search_user,
            'image': product.picture_product,
            'nutri': product.nutrition_grade,
        }

    except AttributeError:
        messages.warning(request, "Ce produit n'existe pas. Vérifiez l'orthographe de la recherche")
        return redirect('home')

    return render(request, 'search.html', context)



