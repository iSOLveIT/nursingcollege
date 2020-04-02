# Third-party modules
from flask import Flask
from flask_session import Session

# Built-in module
import os

# Initialise flask
app = Flask(__name__)

# Check Configuration section for more details
SESSION_COOKIE_NAME = "pantangcollege"
#SESSION_TYPE = 'filesystem'
SESSION_COOKIE_HTTPONLY = False
SESSION_KEY_PREFIX = 'pcollege'
#SESSION_FILE_DIR = "app_session"
app.config.from_object(__name__)
Session(app)

app.secret_key = os.urandom(75)

# Local modules
from package import routes