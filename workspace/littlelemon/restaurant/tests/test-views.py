from django.test import TestCase
from ..models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=60, inventory=200)
        pass