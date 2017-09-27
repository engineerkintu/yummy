#app/recipe/views.py

from flask import render_template
from flask_login import login_required

from . import recipe

@recipe.route('/view_recipe')
def view_recipes():
    """
    Render the view recipes page on /view_recipe route
    """
    return render_template('recipe/view_recipes.html', title="Recipes")

@recipe.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipes():
    """
    Handles requests to the /add_recipe route
    Add recipe to the database through the add recipe form
    """
    form = AddRecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(form.recipe_name.data,
                        form.ingredient.data,
                        form.making_steps.data,
                        form.people_served.data,
                        form.category.data,
                        form.cook.data)

@recipe.route('/edit_recipes', method=['GET', 'POST'])
def editRecipes():
    """
    Handles requests to the /edit_recipe route
    Edit a recipe in the database through the add recipe form
    """
    form = EditRecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(form.recipe_name.data,
                        form.ingredient.data,
                        form.making_steps.data,
                        form.people_served.data,
                        form.category.data,
                        form.cook.data)
    
              
                        
