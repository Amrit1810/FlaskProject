from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from database import data_fetch, update_pass, data_fill
import hashlib
from datetime import datetime


views = Blueprint('views', __name__)

@views.route('/login', methods=['GET', 'POST'])
def login():
    no_records = False

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user_data = data_fetch(email, str(hashlib.sha1(password.encode()).hexdigest()))
        if user_data:
            user_data = user_data[0]
            session['user_data'] = user_data
            print(f"Logged in user: {session['user_data']['primaryKey']}")
            return redirect(url_for('views.profile'))
        else:
            no_records = True

    return render_template('login.html', no_records=no_records)



@views.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        user_data = {
            'primaryKey': hashlib.sha1((request.form['email']+str(hashlib.sha1(request.form['password'].encode()).hexdigest())).encode()).hexdigest(),
            'name': request.form['name'],
            'age': request.form['age'],
            'gender': request.form['gender'],
            'linkedinProfURL': request.form['linkedinProfURL'],
            'designation': request.form['designation'],
            'country': request.form['country'],
            'disabled': request.form['disabled'],
            'FreshExp': request.form['FreshExp'],
            'joinedDate': datetime.now().strftime("%B %d, %Y"),
            'profileDescription': request.form['profileDescription'],
            'username': request.form['username'],
            'email': request.form['email'],
            'password': request.form['password'],
        }

        data_fill(**user_data)
        print('New User Registered!')

        # Use the user_data dictionary as needed (e.g., store it in a database)


        return render_template('login.html', user_data=user_data)
    return render_template('reg.html')


# views.py
@views.route('/profile')
def profile():
    if 'user_data' in session:  # Updated key to 'user_data'
        # Retrieve user_data from the session
        user_data = session.get('user_data', None)
        print('profile', user_data)
        print(user_data)
        if user_data is not None:
            # Render the profile template with user data
            return render_template('profile.html', user=user_data)
        else:
            # Handle the case where user_data is not provided
            return render_template('profile.html', user={})
    else:
        return redirect(url_for('views.login'))





@views.route('/passreset', methods=['GET', 'POST'])
def passreset():
    if request.method == 'POST':
        email = request.form.get('email')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if new_password == confirm_password:
            flash('Password successfully reset. Please login with your new password.', 'success')
            update_pass(email, new_password)
            return redirect(url_for('views.login'))
        else:
            flash('Passwords do not match. Please try again.', 'error')

    return render_template('passreset.html')


@views.route('/logout', methods=['POST'])
def logout():
    if 'user' in session:
        username = session['user']
        session.pop('user', None)
        print(f'Logout successful for {username}', 'success')
    return redirect(url_for('views.login'))