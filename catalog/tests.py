from django.test import TestCase
from django.urls import reverse
from .models import Category, Tag, Product


class ProductListViewTests(TestCase):

    def setUp(self):
        # Set up some test categories
        self.category1 = Category.objects.create(name='Electronics')
        self.category2 = Category.objects.create(name='Clothing')

        # Set up some test tags
        self.tag1 = Tag.objects.create(name='New')
        self.tag2 = Tag.objects.create(name='Sale')

        # Set up some test products
        self.product1 = Product.objects.create(
            name="Smartphone",
            description="A latest model smartphone",
            category=self.category1
        )
        self.product1.tags.add(self.tag1)

        self.product2 = Product.objects.create(
            name="Coffee Maker",
            description="An automatic coffee maker",
            category=self.category1
        )
        self.product2.tags.add(self.tag2)

        self.product3 = Product.objects.create(
            name="T-shirt",
            description="A comfortable cotton t-shirt",
            category=self.category2
        )
        self.product3.tags.add(self.tag1)

    def test_product_list_view_no_filters(self):
        # Test that all products are shown when no filters are applied
        response = self.client.get(reverse('product_list'))  # Adjust URL name if needed
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Smartphone')
        self.assertContains(response, 'Coffee Maker')
        self.assertContains(response, 'T-shirt')

    def test_product_list_view_filter_by_category(self):
        # Test that filtering by category works
        response = self.client.get(reverse('product_list'), {'category': 'Electronics'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Smartphone')
        self.assertContains(response, 'Coffee Maker')
        self.assertNotContains(response, 'T-shirt')

    def test_product_list_view_filter_by_description(self):
        # Test that searching by description works
        response = self.client.get(reverse('product_list'), {'q': 'smartphone'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Smartphone')
        self.assertNotContains(response, 'Coffee Maker')
        self.assertNotContains(response, 'T-shirt')

    def test_product_list_view_filter_by_tags(self):
        # Test that filtering by tags works
        response = self.client.get(reverse('product_list'), {'tags': ['New']})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Smartphone')
        self.assertContains(response, 'T-shirt')
        self.assertNotContains(response, 'Coffee Maker')

    def test_product_list_view_filter_by_category_and_tags(self):
        # Test that filtering by both category and tags works
        response = self.client.get(reverse('product_list'), {'category': 'Electronics', 'tags': ['New']})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Smartphone')
        self.assertNotContains(response, 'Coffee Maker')
        self.assertNotContains(response, 'T-shirt')

    def test_product_list_view_no_results(self):
        # Test that if no products match the filters, a message is shown
        response = self.client.get(reverse('product_list'), {'category': 'Clothing', 'q': 'laptop'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No products found matching your criteria.')

    def test_product_list_view_selected_category_in_dropdown(self):
        # Test that the selected category is reflected in the dropdown
        response = self.client.get(reverse('product_list'), {'category': 'Clothing'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'selected', html=True)

    def test_product_list_view_selected_tags_in_checkbox(self):
        # Test that selected tags are reflected in the checkbox
        response = self.client.get(reverse('product_list'), {'tags': ['New']})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'checked', html=True)
