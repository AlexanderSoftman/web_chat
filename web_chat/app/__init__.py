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

# # setup SMTP debug info
# if not app.debug:
#     import logging
#     credentials = None
#     if config.MAIL_USERNAME or config.MAIL_PASSWORD:
#         credentials = (
#             config.MAIL_USERNAME,
#             config.MAIL_PASSWORD)
#     mail_handler = logging.handlers.SMTPHandler(
#         (config.MAIL_SERVER, config.MAIL_PORT),
#         'no-reply@' + config.MAIL_SERVER,
#         config.ADMINS,
#         'microblog failure',
#         credentials)
#     mail_handler.setLevel(logging.ERROR)
#     app.logger.addHandler(mail_handler)

# # setup file debug info - ten files with 1 Mb size each
# if not app.debug:
#     import logging
#     file_handler = logging.handlers.RotatingFileHandler(
#         'tmp/web_chat.log',
#         'a',
#         1 * 1024 * 1024,
#         10)
#     file_handler.setFormatter(
#         logging.Formatter(
#             "%(asctime)s %(levelname)s: %(message)s \
#             [in %(pathname)s:%(lineno)d]"))
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('microblog startup')


from app import views
