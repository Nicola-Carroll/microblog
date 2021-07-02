from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Captain Charlie Hook Hand'}
    posts = [
        {
            'author': {'username': 'Jimbo'},
            'body': 'Excellent bounty find today lads :)'
        },
        {
            'author': {'username': 'Susan (for a boy)'},
            'body': 'The seas are restless tonight'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
