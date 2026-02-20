import hashlib
import time
from flask import Flask

app = Flask(__name__)


@app.route('/')

def flask_app():

    password = b'Humm3rsupp3!'

    password_hash = hashlib.sha256(password)

    print(password_hash)

    return 'Done'


if __name__ == '__main__':
    app.run()