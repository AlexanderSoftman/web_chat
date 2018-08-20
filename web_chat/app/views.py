import logging
from app import app, oid, db, lm
import flask
import app.forms as forms
import app.models as models
import flask_login
import datetime

LOG = logging.getLogger(__name__)

# posts = [
#     {
#         'author': {'nickname': 'Alexander'},
#         'body': "hello, i'am Alexander Fomin"
#     },
#     {
#         'author': {'nickname': 'Alexey'},
#         'body': "Hi, Alexander, what you done for this morning?"
#     },
#     {
#         'author': {'nickname': 'Sergey'},
#         'body': "Hi, guys, i'am also here"
#     }

# ]

# $('#test').text("dsds")
# Object [ h1#test ]
# setInterval(functon(){})
# SyntaxError: missing ) after argument list[Learn More] debugger eval code:1:21
# var counter=0;
# undefined
# counter\
# SyntaxError: illegal character[Learn More] debugger eval code:1:7
# counter
# 0
# setInterval(function(){$('#test').text(''+counter);}, 100);
# 2
# setInterval(function(){$('#test').text('' + counter); console.log('xxx');}, 1000);
# 3
# xxx
# debugger eval code:1:55
# var xxx=12;
# undefined
# xxx
# debugger eval code:1:55
# setInterval(function(){$('#test').text('' + counter); counter += 1; console.log('xxx');}, 1000);
my_counter = {"counter": 0}


@app.before_request
def before_request():
    flask.g.user = flask_login.current_user
    if flask.g.user.is_authenticated:
        flask.g.user.last_seen = datetime.datetime.utcnow()
        db.session.add(flask.g.user)
        db.session.commit()


@app.route("/login", methods=['GET', 'POST'])
@oid.loginhandler
def login():
    user = flask.g.get('user', None)
    if user is not None and user.is_authenticated:
        print("login::before redirect to index page")
        return flask.redirect(flask.url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        flask.session['remember_me'] = form.remember_me.data
        print("login::oid.try_login")
        return oid.try_login(
            form.openid.data, ask_for=[
                'nickname', 'email'])
    print("login::flask.render_template")
    return flask.render_template(
        'login.html',
        title='Sign In',
        form=form,
        providers=app.config['OPENID_PROVIDERS'])


@app.route("/")
@app.route("/index")
@flask_login.login_required
def index():
    print("login::index start")
    user = flask.g.get('user', None)
    print("login::user: %s" % (user,))
    posts = [
        {
            'author': {'nickname': 'Alexander'},
            'body': "hello, i'am Alexander Fomin"
        },
        {
            'author': {'nickname': 'Alexey'},
            'body': "Hi, Alexander, what you done for this morning?"
        },
        {
            'author': {'nickname': 'Sergey'},
            'body': "Hi, guys, i'am also here"
        }
    ]
    return flask.render_template(
        "index.html",
        user=user,
        posts=posts)


@app.route("/test")
def test():
    my_counter["counter"] += 1
    print("test called " + str(my_counter["counter"]))
    return "PRVIET ALEXANDER + " + str(my_counter["counter"])


@app.route("/logout")
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('index'))


@oid.after_login
def after_login(resp):
    print("in after_login method")
    if resp.email is None or resp.email == "":
        flask.flash('Invalid login. Please try again')
        return flask.redirect(flask.url_for('login'))
    user = models.User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        nickname = models.User.make_unique_nickname(
            nickname)
        user = models.User(
            nickname=nickname,
            email=resp.email,
            role=models.ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in flask.session:
        remember_me = flask.session['remember_me']
        flask.session.pop('remember_me', None)
    flask_login.login_user(user, remember=remember_me)
    return flask.redirect(
        flask.request.args.get('next') or
        flask.url_for('index'))


@lm.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)


@app.route('/user/<nickname>')
@flask_login.login_required
def user(nickname):
    user = models.User.query.filter_by(nickname=nickname).first()
    if user is None:
        flask.flash('User' + nickname + ' not found.')
        return flask.redirect(flask.url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return flask.render_template(
        'user.html',
        user=user,
        posts=posts)


@app.route('/edit', methods=['GET', 'POST'])
@flask_login.login_required
def edit():
    form = forms.EditForm()
    if form.validate_on_submit():
        flask.g.user.nickname = form.nickname.data
        flask.g.user.about_me = form.about_me.data
        db.session.add(flask.g.user)
        db.session.commit()
        flask.flash('Your changes have been saved')
        return flask.redirect(flask.url_for('edit'))
    else:
        form.nickname.data = flask.g.user.nickname
        form.about_me.data = flask.g.user.about_me
    return flask.render_template('edit.html', form=form)


@app.errorhandler(404)
def not_found_error(error):
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return flask.render_template('500.html'), 500
