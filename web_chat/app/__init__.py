import flask
import flask_sqlalchemy
app = flask.Flask(__name__)
app.config.from_object('config')
db = flask_sqlalchemy.SQLAlchemy(app)

from app import views, models
