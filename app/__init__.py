from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate as migrate_function, upgrade
from sqlalchemy_utils.functions import database_exists


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
    print("Database doesn't exist, creating a new one...")
    db.create_all()
    with app.app_context():
        upgrade()
        migrate_function()

from app import routes, models