from django.test import TestCase
from .models import Category,Location,Image
import datetime as dt
# Create your tests here.
class CategoryTestClass(TestCase):
    '''
    Test class that defines test cases for the category class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        """
        set up method to run before each test case
        """
        Category.objects.create(name="Test Category")

    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")
        
class LocationTestClass(TestCase):
    '''
    Test class that defines test cases for the location class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        """
        set up method to run before each test case
        """
        Location.objects.create(name="Test Location")

    def test_category_name(self):
        """
        Test that the location name is correct
        """
        location =Location.objects.get(name="Test Location")
        self.assertEqual(location.name, "Test Location")
        
class ImageTestClass(TestCase):
    '''
    Test class that defines test cases for the limage class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        """
        set up method to run before each test case
        """

