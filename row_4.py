from flask import Flask, request, redirect, url_for, render_template, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management and CSRF protection

# In-memory storage for demonstration purposes; use a database in production
users = {
    'user1': {'email': 'old@example.com', 'password': generate_password_hash('password')},
}

@app.before_request
def load_user():
    username = session.get('username')
    if username:
        g.user = users[username]

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('change_email'))
        else:
            flash('Invalid login')
    return render_template('login.html')

@app.route('/change-email', methods=['GET', 'POST'])
def change_email():
    if not g.user:
        return redirect(url_for('login'))

    if request.method == 'POST':
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']

        if check_password_hash(g.user['password'], confirm_password):
            if old_email == g.user['email']:
                if old_email != new_email:
                    users[session['username']]['email'] = generate_password_hash(new_email)
                    flash('Email changed successfully')
                    return redirect(url_for('change_email'))
                else:
                    flash('New email must be different from the old one')
            else:
                flash('Old email does not match your current account email')
        else:
            flash('Incorrect password')

    return render_template('change_email.html', user=g.user)

if __name__ == '__main__':
    app.run(debug=True)