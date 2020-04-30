# Third-party modules
from package import app

# Built-in modules
import os

app.config['SECRET_KEY'] = os.urandom(125)  # Secret key


if __name__ == '__main__':
    app.run(debug=True)
