from flask import Flask
from flask_migrate import Migrate
from .views import api_view
from .models import db

def create_app(config='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    db.init_app(app)
    migrate  = Migrate(app, db)
    app.register_blueprint(api_view)
    return app