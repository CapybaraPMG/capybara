from flask import Flask
from flask import render_template


#Importing the blueprints defined in views
from views.events.routes import event_views
from views.users.routes import user_views

app = Flask(__name__)


#Registering the blueprints
app.register_blueprint(event_views)
app.register_blueprint(user_views)


@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
