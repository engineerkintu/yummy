from flask_login import UserMixin
from wekzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(object):
    """
    Create a User table
    """
    user_id = 0
   def __init__(self,email,username,first_name,last_name, password_hash):
       self.user_id +=1
       self.email=email
       self.username=username
       self.last_name=last_name
       self.password_hash=password_hash
       



    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def passsword(self, password):
        """
        Set password to a hashed password
        """
        raise AttributeError('password is not a readable attribute.')

    def verify_password(self, password):
        """
         Check if hashed password matches actual password
         """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    #Set up user_loader
    @login_manager.user_loarder
    def load_user(user_id):
        return User.query,get(int(user_id))


class RecipeCategory(object):
    cat_id = 0
    def __init__(self,category_name, user):
        self.cat_id += 1
        self.category_name = category_name
        self.user = user

   
    

class Recipe(object):
    recipe_id = 0
    def __init__(self, recipe_name,ingredient, making_steps, people_served, quantity_expected, cat, user):
        self.recipe_id += 1
        self.recipe_name = recipe_name
        self.ingredient = ingredient
        self.making_steps = making_steps
        self.quantity_epected = quantity_expected
        self.people_served = people_served
        self.category = cat
        self.cook = user

   


    
        
    
    
    
        
    

    
