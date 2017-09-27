from app import app
from app import models

import unittest

class BasicTestCase(unittest.TestCase):
    """

    def test_index(self):
        """Initial test to ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

class UserTestCase(unittest.TestCase):
    def test_user(self):
        """Has used been created """
        peter = models.User('eng.gmail.com','peter','devos','balu','h677')
        user_id = 1
        user1_id = peter.user_id
        self.assertEqual(peter_id,user_id)

    def test_recipe(self):
        """ test if a recipe object has been created """
        katogo = models.Recipe('katogo','cassava and beans','boil it','1 kilogram',3,1,2)
        recipe_id = 1
        katogo_id = katogo.recipe_id
        self.assertEqual(katogo_id,recipe_id)

    def test_recipe_category(self):
        """ test if a recipe category was created """
        vegs = models.RecipeCategory('Vegetables',2)
        cat_id = 1
        vegs_id = vegs.cat_id
        self.assertEqual(vegs_id,cat_id)
    

if __name__=='__main'__:
    unittest.main()
    """
        
        

