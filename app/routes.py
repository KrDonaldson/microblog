from app import app
from flask import render_template

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
