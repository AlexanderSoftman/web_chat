import flask
import logging

app = flask.Flask(__name__)
app.config.from_object("config")

# import app.views

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


@app.route("/")
@app.route("/index")
def test_function():
    LOG.critical("/ called")
    user = {'nickname': 'Alexander'}
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
        "index.html", user=user, posts=posts)


@app.route("/test")
def test_function_2():
    my_counter["counter"] += 1
    print("test_function_2 called " + str(my_counter["counter"]))
    return "PRVIET ALEXANDER + " + str(my_counter["counter"])
