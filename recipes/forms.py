from django import forms
from .models import Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'tags']
        exclude = ['author']


class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['id', 'author', 'is_active', 'title', 'tags']
        exclude = ['author']

