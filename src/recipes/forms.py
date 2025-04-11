#recipes/forms.py
from django import forms
from .models import Recipe 
from categories.models import Category

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'cooking_time', 'category']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 4}),
        }

class RecipeSearchForm(forms.Form):
    search_query = forms.CharField(required=False, label='Search by name or ingredients')
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Filter by category'
    )
    max_cooking_time = forms.IntegerField(
        required=False,
        min_value=1,
        label='Max cooking time (minutes)'
    )
    difficulty = forms.ChoiceField(
        choices=[
            ('', 'Any difficulty'),
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('intermediate', 'Intermediate'),
            ('hard', 'Hard')
        ],
        required=False,
        label='Difficulty'
    )        