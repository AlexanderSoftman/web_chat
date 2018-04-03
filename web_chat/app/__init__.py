import flask
import logging

app = flask.Flask(__name__)
LOG = logging.getLogger(__name__)

posts_history = [
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


@app.route("/")
def test_function():
    LOG.critical("/ called")
    user = {'nickname': 'Alexander'}
    return flask.render_template(
        "index.html", user=user, posts_history=posts_history)

