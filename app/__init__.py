from flask import Flask, current_app
from app.config import Config
from sqlalchemy_utils.functions import database_exists
from flask_migrate import Migrate, upgrade, migrate as migrate_function
from app.extensions import db


migrate = Migrate()

def create_app(config_class='Config'):
    app = Flask(__name__)
    app.config.from_object(f"app.config.{config_class}")

    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import bp

    app.register_blueprint(bp)


    return app

app = create_app('Config')


if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
    print("Database doesn't exist, creating a new one...")
    with app.app_context():
        upgrade()
        migrate_function()
        
        
        
                

from app import models
