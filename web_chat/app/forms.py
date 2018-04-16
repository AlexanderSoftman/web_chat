import flask_wtf
import wtforms


class LoginForm(flask_wtf.FlaskForm):
    openid = wtforms.TextField(
        'openid', validators=[wtforms.validators.Required()])
    remember_me = wtforms.BooleanField(
        'remember_me', default=False)
