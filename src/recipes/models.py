from django.db import models
#from categories.models import Category
#from ingredients.models import Ingredient

# Create your models here.
 
# This is the model for the Recipe app. It defines the structure of the Recipe object.
# It contains fields for the recipe name, cooking time, and ingredients.
class Recipe(models.Model):
    name = models.CharField(max_length=100) 
    cooking_time = models.IntegerField()
    ingredients = models.TextField()  # basic compatibility
    #Added support for images << 2.5
    #image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)

    
    # Use string references instead of direct model references
    category = models.ForeignKey('categories.Category', 
                               on_delete=models.SET_NULL, 
                               null=True, blank=True, 
                               related_name='recipes')
    
    ingredient_list = models.ManyToManyField('ingredients.Ingredient', 
                                           blank=True, 
                                           related_name='used_in')
        #the ingredient_list field is a many-to-many relationship with the ingredient model.
    #this means that a recipe can have multiple ingredients and an ingredient can be used in multiple recipes.

    def __str__(self):
        return self.name

    def get_ingredients_list(self):
        return self.ingredients.split(',') if self.ingredients else [] #we use this to get the list of ingredients via split because the ingredients are stored as a string in the database
    
    def calculate_difficulty(self):
        """Calculate recipe difficulty based on cooking time and number of ingredients"""
        cooking_time = self.cooking_time
        num_ingredients = len(self.get_ingredients_list())

        # define thresholds
        TIME_THRESHOLD = 10
        INGREDIENT_THRESHOLD = 3

        # 2 condition if else based on thresholds
        if cooking_time < TIME_THRESHOLD:
            if num_ingredients < INGREDIENT_THRESHOLD:
                return "Easy"
            else:
                return "Medium"
        else:
            if num_ingredients >= INGREDIENT_THRESHOLD:
                return "Hard"
            else:
                return "Intermediate"