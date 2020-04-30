# Third-party modules
from flask import Flask
from flask_session import Session

# Initialise flask
app = Flask(__name__)

# Check Configuration section for more details
SESSION_COOKIE_NAME = "name_for_cookie"
SESSION_TYPE = 'filesystem'
SESSION_COOKIE_HTTPONLY = False
SESSION_KEY_PREFIX = 'prefixaddedToSessionkey'
SESSION_FILE_DIR = "app_session"
app.config.from_object(__name__)
Session(app)

# Local modules
from package import routes
