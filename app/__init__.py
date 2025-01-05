from flask import Flask


def create_app():
    app = Flask(__name__)

    # Načtení konfigurace
    app.config.from_object('config.config.Config')  # Důležité! Nastavena úplná cesta

    # Importy routes nebo blueprintů
    from app.views.routes import views

    app.register_blueprint(views, url_prefix='/')


    return app
