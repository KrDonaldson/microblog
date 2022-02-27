from app import app
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'test'}
    posts = [
        {
            'author': {'username': 'This User'},
            'body': 'This is the body of This user\'s post.'
        },
        {
            'author': {'username': 'That User'},
            'body': 'This is the body of That user\'s post.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format (
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title ='Sign In', form=form)