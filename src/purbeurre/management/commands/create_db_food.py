import requests
import json

from django.core.management.base import BaseCommand
from django.db.utils import DataError, IntegrityError
from purbeurre.models import Category_product, Name


class Command(BaseCommand):
    """
    This
    class is used for information retrieval in the API.
    """

    url = \
        'https://fr.openfoodfacts.org/langue/francais/categories.json'

    category_json = json.loads(requests.get(url).text)
    CATEGORIES = ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner', 'Biscuits', 'Vins',
                  'Boissons-gazeuses', 'Yaourts', 'Pains', 'Glace', 'Fromages-de-france', 'Pizzas', 'Snacks sucrés']
    product_name = ""
    product_url = ""
    product_shop = ""
    product_nutrition = ""

    def request_category(self):
        """
        Get category names from Open Food Facts.
        """

        for counter in range(50):
            name_category = self.category_json["tags"][counter]["name"]
            Category_product.objects.create(name_category=name_category)
        
        self.request_food()

    def request_food(self):

        for category in range(50 + 1):
            category_choice_json = self.category_json["tags"][category - 1]

            answer_category_json = json.loads(
                requests.get(category_choice_json["url"] + ".json").text)

            for product in answer_category_json["products"]:

                try:
                    name_product = product["product_name"]
                    nutrition_grade = product["nutrition_grades"]
                    picture_product = product['image_front_url']
                    picture_nutrition = product["image_nutrition_small_url"]
                    url_product = product["url"]

                    Name.objects.create(name_product=name_product, nutrition_grade=nutrition_grade,
                                       url_product=url_product, picture_product= picture_product, picture_nutrition=picture_nutrition)

                except KeyError:
                    pass

                except DataError:
                    pass

                except IntegrityError:
                    pass
                

            

        """for name_category in self.CATEGORIES:"""

        """category = Category_product.objects.create(name=name_category)

        params = {
            'action': 'process',
            'json': 1,
            'page_size': 500,
            'page': 1,
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': name_category,
        }"""

        """response = requests.get('https://fr.openfoodfacts.org/cgi/search.pl',
                                params=params)

        data = response.json()
        products = data['products']

        for product in products:
            try:
                name_product = product["product_name"]
                nutrition_grade = product["nutrition_grades"]
                picture_product = product['image_front_url']
                picture_nutrition = product["image_nutrition_small_url"]
                url_product = product["url"]

                Name.objects.create(name_product=name_product, nutrition_grade=nutrition_grade, category=name_category,
                                       url_product=url_product, picture_product= picture_product, picture_nutrition=picture_nutrition)

            except KeyError:
                pass

            except DataError:
                pass

            except IntegrityError:
                pass"""

    def handle(self, *args, **options):
        self.request_category()