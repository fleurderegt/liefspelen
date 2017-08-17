from django.contrib import admin

from .models import Game, Category, Tag, Season, Environment, Material

myModels = [Game, Category, Tag, Season, Environment, Material]
admin.site.register(myModels)