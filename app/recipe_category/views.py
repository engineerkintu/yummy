
@recipe.route('/add_recipe_category', methods=['GET', 'POST'])
@login_required
def add_recipes_category():
    """
    Handles requests to the /add_recipe_category route
    Add recipe category to the database through the add recipe form
    """
    form = AddRecipeCategoryForm()
    if form.validate_on_submit():
        recipe = Recipe(form.category_name.data,
                        
                        form.user.data)

@recipe.route('/edit_recipes', method=['GET', 'POST'])
@login_required
def edit_recipes_category():
    """
    Handles requests to the /edit_recipe_category route
    Edit a recipe category in the database through the add recipe form
    """
    form = EditRecipeCategoryForm()
    if form.validate_on_submit():
        recipe = Recipe(form.category_name.data,
                        
                        form.user.data)
