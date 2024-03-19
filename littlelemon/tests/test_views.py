from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        Menu.objects.create(title="Ice Cream", price=5.00, inventory=20)
        Menu.objects.create(title="Coffee", price=3.00, inventory=15)

    def test_get_all_menus(self):
        # Initialize the APIClient app
        client = APIClient()

        # Get the response from the 'menu-list' route
        response = client.get(reverse('menu-list'))

        # Get the data from the db
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Compare the response data with the serialized menu items
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Remember to replace 'menu-list' with the actual name you have given to the URL
# that corresponds to the Menu list view in your urls.py.
