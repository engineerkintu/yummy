from flask import Flask
from config import app_config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    from app import models
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import auth as home_blueprint
    app.register_blueprint(home_blueprint)

    from .recipes import auth as recipes_blueprint
    app.register_blueprint(recipes_blueprint)

    from .recipe_category import auth as recipe_category_blueprint
    app.register_blueprint(recipe_category_blueprint)

    Bootstrap(app)
    

    return app
