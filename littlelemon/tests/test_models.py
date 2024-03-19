from django.test import TestCase
from .models import Menu

# Test case class for MenuItem
class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a new MenuItem instance
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        
        # Use the __str__ method of the item to get the string representation
        expected_item_str = f"{item.title} : {str(item.price)}"
        
        # Assert that the string representation matches what we expect
        self.assertEqual(item.__str__(), expected_item_str)
