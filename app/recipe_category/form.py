from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired


from ..models import RecipeCategory(FlaskForm)
class AddRecipeCategory(FlaskForm):
    
    """
    Form for entering recipe category
    """
    category_name = StringField('Category Name', validators = [DataRequired])
    user = StringField('Cook')
    submit = SubmitField('Save')


class EditRecipeCategory(FlaskForm):
    
    """
    Form for editing recipe category
    """
    category_name = StringField('Category Name', validators = [DataRequired])
    user = StringField('Cook')
    submit = SubmitField('Save')
    
     
     
    
    
    

    

