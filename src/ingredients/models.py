from django.db import models

# Create your models here.

# Delete the entire file content and paste this
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'
    
    def __str__(self):
        return self.name    
    def used_in_recipes_count(self):
        """Returns count of recipes using this ingredient"""
        from recipes.models import Recipe
        count = 0
        for recipe in Recipe.objects.all():
            if self.name.lower() in [ing.lower() for ing in recipe.get_ingredients_list()]:
                count += 1
        return count