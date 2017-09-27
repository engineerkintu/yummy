# app/recipe_category/__init__.py

from flask import Blueprint

recipe_category = Blueprint('recipe_category', __name__)

from . import views
