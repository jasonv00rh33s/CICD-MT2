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