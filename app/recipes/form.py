from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired


from ..models import Recipe


class AddRecipesForm(FlaskForm):
    """
    Form for entering recipe
    """

    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    people_served = StringField('Number of Plates')
    quantity = StringField('Quantity')
    ingredient = StringField('Ingredient')
    making_steps = StringdField('Making Steps')
    category = StringField('Category')
    cook = StringField('Cook')
    submit = SubmitField('Save')

class EditRecipeForm(FlaskForm):
    """
    Form for editing recipe
    """
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    people_served = StringField('Number of Plates')
    quantity = StringField('Quantity')
    ingredient = StringField('Ingredient')
    making_steps = StringdField('Making Steps')
    category = StringField('Category')
    cook = StringField('Cook')
    submit = SubmitField('Save')
    
    

    


