import flask
import flask_sqlalchemy
import flask_login
import flask_openid
import config
import os

app = flask.Flask(__name__)
app.config.from_object('config')

oid = flask_openid.OpenID(
    app,
    os.path.join(config.basedir, 'tmp'))

db = flask_sqlalchemy.SQLAlchemy(app)


lm = flask_login.LoginManager()
lm.init_app(app)
lm.login_view = 'login'


from app import views
