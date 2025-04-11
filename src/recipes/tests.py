from django.test import TestCase
from recipes.models import Recipe
from categories.models import Category
from ingredients.models import Ingredient
from .forms import RecipeSearchForm
from django.urls import reverse
from django.test import Client


class RecipeModelTest(TestCase):
    """Tests for the Recipe model"""
    
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods"""
        # Create a category
        test_category = Category.objects.create(
            name='Test Category',
            description='A category for testing'
        )
        
        # Create an ingredient
        test_ingredient = Ingredient.objects.create(
            name='Test Ingredient',
            notes='An ingredient for testing'
        )
        
        # Create a recipe
        test_recipe = Recipe.objects.create(
            name='Test Recipe',
            cooking_time=15,
            ingredients='Test Ingredient, Another Ingredient, Third Ingredient',
            category=test_category
        )
        
        # Add ingredient to recipe
        test_recipe.ingredient_list.add(test_ingredient)
    
    def test_recipe_name(self):
        """Test the recipe name field"""
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(field_label, 'name')
        self.assertEqual(max_length, 100)
        self.assertEqual(recipe.name, 'Test Recipe')
        
    def test_cooking_time(self):
        """Test the cooking_time field"""
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('cooking_time').verbose_name
        self.assertEqual(field_label, 'cooking time')
        self.assertEqual(recipe.cooking_time, 15)
        
    def test_ingredients_field(self):
        """Test the ingredients text field"""
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.ingredients, 'Test Ingredient, Another Ingredient, Third Ingredient')
        
    def test_get_ingredients_list(self):
        """Test the get_ingredients_list method"""
        recipe = Recipe.objects.get(id=1)
        ingredients_list = recipe.get_ingredients_list()
        self.assertEqual(len(ingredients_list), 3)
        self.assertIn('Test Ingredient', ingredients_list)
        # i am using the actual strings with spaces:
        self.assertIn(' Another Ingredient', ingredients_list)
        self.assertIn(' Third Ingredient', ingredients_list)        
    def test_calculate_difficulty_easy(self):
        """Test the calculate_difficulty method - Easy case"""
        recipe = Recipe.objects.create(
            name='Easy Recipe',
            cooking_time=5,
            ingredients='Salt, Pepper'
        )
        self.assertEqual(recipe.calculate_difficulty(), 'Easy')
        
    def test_calculate_difficulty_medium(self):
        """Test the calculate_difficulty method - Medium difficulty"""
        recipe = Recipe.objects.create(
            name='Medium Recipe',
            cooking_time=5,
            ingredients='Salt, Pepper, Sugar, Flour, Eggs'
        )
        self.assertEqual(recipe.calculate_difficulty(), 'Medium')
        
    def test_calculate_difficulty_intermediate(self):
        """Test the calculate_difficulty method - Intermediate difficulty"""
        recipe = Recipe.objects.create(
            name='Intermediate Recipe',
            cooking_time=15,
            ingredients='Salt, Pepper'
        )
        self.assertEqual(recipe.calculate_difficulty(), 'Intermediate')
        
    def test_calculate_difficulty_hard(self):
        """Test the calculate_difficulty method - Hard difficulty"""
        recipe = Recipe.objects.create(
            name='Hard Recipe',
            cooking_time=15,
            ingredients='Salt, Pepper, Sugar, Flour, Eggs'
        )
        self.assertEqual(recipe.calculate_difficulty(), 'Hard')
        
    def test_category_relationship(self):
        """Test the category foreign key relationship"""
        recipe = Recipe.objects.get(id=1)
        category = Category.objects.get(id=1)
        self.assertEqual(recipe.category, category)
        
    def test_ingredient_list_relationship(self):
        """Test the ingredient_list many-to-many relationship"""
        recipe = Recipe.objects.get(id=1)
        ingredient = Ingredient.objects.get(id=1)
        self.assertIn(ingredient, recipe.ingredient_list.all())
        
    def test_string_representation(self):
        """Test the string representation of the Recipe model"""
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), recipe.name)

#the tests for the advanced search form are below.

class RecipeSearchFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
    
    def test_form_fields(self):
        form = RecipeSearchForm()
        self.assertTrue('search_query' in form.fields)
        self.assertTrue('category' in form.fields)
        self.assertTrue('max_cooking_time' in form.fields)
        self.assertTrue('difficulty' in form.fields)
    
    def test_search_form_valid(self):
        form_data = {
            'search_query': 'test recipe',
            'category': self.category.id,
            'max_cooking_time': 30,
            'difficulty': 'easy'
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_search_form_empty(self):
        form_data = {}
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())  # Empty form should be valid       


class RecipeAnalyticsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create categories
        cls.category = Category.objects.create(name='Test Category')
        
        # Create recipes
        Recipe.objects.create(
            name='Easy Recipe',
            cooking_time=10,
            ingredients='ingredient1',
            category=cls.category
        )
        Recipe.objects.create(
            name='Hard Recipe',
            cooking_time=60,
            ingredients='ingredient1, ingredient2, ingredient3, ingredient4',
            category=cls.category
        )
    
    def setUp(self):
        self.client = Client()
    
    def test_view_url_exists(self):
        response = self.client.get('/analytics/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('recipe-analytics'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('recipe-analytics'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/analytics.html')
    
    def test_context_contains_charts(self):
        response = self.client.get(reverse('recipe-analytics'))
        self.assertTrue('category_chart' in response.context)
        self.assertTrue('difficulty_chart' in response.context)
        self.assertTrue('time_chart' in response.context)
    
    def test_context_contains_stats(self):
        response = self.client.get(reverse('recipe-analytics'))
        self.assertEqual(response.context['recipe_count'], 2)
        self.assertEqual(response.context['category_count'], 1)         

class RecipeSearchViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data
        cls.category1 = Category.objects.create(name='Breakfast')
        cls.category2 = Category.objects.create(name='Dinner')
        
        # Create recipes
        Recipe.objects.create(
            name='Test Recipe 1',
            cooking_time=15,
            ingredients='ingredient1, ingredient2',
            category=cls.category1
        )
        Recipe.objects.create(
            name='Test Recipe 2',
            cooking_time=45,
            ingredients='ingredient3, ingredient4',
            category=cls.category2
        )
        Recipe.objects.create(
            name='Special Pasta',
            cooking_time=30,
            ingredients='pasta, sauce',
            category=cls.category2
        )
    
    def setUp(self):
        self.client = Client()
    
    def test_search_view_exists(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
    
    def test_search_by_name(self):
        response = self.client.get('/search/?search_query=Test Recipe 1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('results' in response.context)
        self.assertEqual(len(response.context['results']), 1)
    
    def test_search_partial_name(self):
        """Test that partial search works (wildcard functionality)"""
        response = self.client.get('/search/?search_query=Special')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('results' in response.context)
        self.assertEqual(len(response.context['results']), 1)
        self.assertEqual(response.context['results'][0].name, 'Special Pasta')
    
    def test_search_by_ingredient(self):
        """Test search by ingredient"""
        response = self.client.get('/search/?search_query=pasta')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('results' in response.context)
        self.assertEqual(len(response.context['results']), 1)
        self.assertEqual(response.context['results'][0].name, 'Special Pasta')
    
    def test_search_by_category(self):
        """Test filtering by category"""
        response = self.client.get(f'/search/?category={self.category1.id}')
        self.assertEqual(response.status_code, 200)
