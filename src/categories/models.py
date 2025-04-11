from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Model representing a recipe category
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    # Meta options for plural form
    class Meta:
        #this is used to define the plural form of the model name in the admin interface
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        """String representation of the category"""
        return self.name

# update the Recipe model to include a category field !!!!