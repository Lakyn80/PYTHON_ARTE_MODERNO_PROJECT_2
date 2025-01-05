from flask import Flask


def create_app():
    app = Flask(__name__)

    # Načtení konfigurace
    app.config.from_object('config.config.Config')  # Důležité! Nastavena úplná cesta

    # Importy routes nebo blueprintů
    with app.app_context():
        from . import routes

    return app
