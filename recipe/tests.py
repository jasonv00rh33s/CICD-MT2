from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Cake", 
            category=self.category
        )

    def test_main_view_status_code(self):
            response = self.client.get(reverse('main'))
            self.assertEqual(response.status_code, 200)

    def test_category_detail_view_status_code(self):
            response = self.client.get(reverse('category_detail', args=[self.category.id]))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Cake")