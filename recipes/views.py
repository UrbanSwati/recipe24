from django.shortcuts import render
from .models import Recipe
from django.http import HttpResponse
# Create your views here.
def recipes(request):
    recipes = Recipe.objects.all()
    return render(request,'recipes/recipes.html', {'recipes': recipes})

def recipe_details(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request,'recipes/recipe_detail.html',{'recipe':recipe})