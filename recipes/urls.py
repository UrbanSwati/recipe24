from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.recipes, name="recipes-list"),
    url(r'^(?P<id>[\w]+)/$', views.recipe_details, name="recipe-detail"),
]