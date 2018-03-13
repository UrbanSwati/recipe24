from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(default='default-image.jpg', blank=True)
    rating = models.DecimalField(max_digits=1, decimal_places=0)
    prep_time = models.CharField(max_length=30)
    cooking_time = models.CharField(max_length=30)
    servings = models.DecimalField(max_digits=2, decimal_places=0)
    ingredients = models.TextField()
    cooking_instructions = models.TextField()

    def __str__(self):
        return self.title