from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

# Create the application object
app = Flask(__name__)

app.secret_key = "my precious"

# Use decorators to link the function to a url
@app.route('/')
def home():
    # return "Index page - Test for Echo!"
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

# Start the server with the run() method
if __name__ == '__main__':
    app.run(debug=True)

