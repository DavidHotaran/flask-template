from flask import Flask


def register_blueprints():
    from src.api.routes.ping import ping_api
    app.register_blueprint(ping_api, url_prefix='/api')


app = Flask(__name__)
register_blueprints()