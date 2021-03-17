from django.shortcuts import render
from purbeurre.models import Category_product
import requests, json

# Create your views here.
def home(request):

    return render(request, "index.html")

def api(request):
    if 'str_user' in request.GET:
        name = request.GET['name']
        print(name)
        url = \
        'https://fr.openfoodfacts.org/langue/francais/categories.json'

        category_json = json.loads(requests.get(url).text)

        for counter in range(50):
            Category_product.objects.create(category_json["tags"][counter]["name"])