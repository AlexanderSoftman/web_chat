#!flask/bin/python
from app import app

# for imitation of smtp catching in console, start command
# python -m smtpd -n -c DebuggingServer localhost:25

app.run(debug=False)
