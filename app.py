from flask import Flask, render_template, jsonify
from config import settings
import sys


# Importing the blueprints defined in views
from views.events.routes import event_views
from views.users.routes import user_views

app = Flask(__name__)


# Registering the blueprints
app.register_blueprint(event_views)
app.register_blueprint(user_views)


@app.route("/")
def index():
    return jsonify("Ok! ✅"), 200


@app.route("/health", methods=["GET"])
def health_check():
    api_health = {"status": "Ok!", "message": "API is up and running"}
    return jsonify(api_health), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(settings.PORT), debug=True)
