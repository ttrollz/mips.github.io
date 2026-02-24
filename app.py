import hashlib
import time
from flask import Flask, render_template, request, redirect, url_for, session
import re

app = Flask(__name__)
app.secret_key = 'insanely-super-secret-key'


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])

# -= POSTRESQL INTERACTION =-
# app.config['HOST'] = 'localhost'
# app.config['USER'] = 'root'
# app.config['DB_PASSWORD'] = 'db password'
# app.config['DB_NAME'] = 'db name'
# -= END POSTGRESQL =-


def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        # =- Hashing of password =-

        # -= Fetch from db =-

    account = 1

    if account: # Account er en struct der indeholder datafelterne, her can vi evt. bruge cursor.fetch
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']
        return render_template('index.html', msg = 'Logged in successfully!')
    else: msg = 'Incorrect username/password!'

    return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(url_for('login'))

@app.route('/register')

def register():
    #add code later?
    msg = ''



if __name__ == '__main__':
    app.run(debug=True)