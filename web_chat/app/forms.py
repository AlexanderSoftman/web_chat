import flask_wtf
import wtforms


class LoginForm(flask_wtf.FlaskForm):
    openid = wtforms.TextField(
        'openid', validators=[wtforms.validators.Required()])
    remember_me = wtforms.BooleanField(
        'remember_me', default=False)


class EditForm(flask_wtf.FlaskForm):
    nickname = wtforms.TextField('nickname', validators=[
        wtforms.validators.Required()])
    about_me = wtforms.TextAreaField(
        'about_me',
        validators=[
            wtforms.validators.Length(
                min=0,
                max=140)])
    # FIND ME!!!!!

