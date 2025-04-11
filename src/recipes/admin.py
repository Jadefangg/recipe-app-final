from django.contrib import admin
from recipes.models import Recipe
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_time', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'ingredients')


admin.site.register(Recipe)
# Register the Recipe model with the Django admin site.