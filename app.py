from flask import Flask, render_template, Markup, request
import random
from config import Config
#import MyApp
#from app.forms import LoginForm


MyApp = Flask(__name__)
MyApp.config.from_object(Config)

@MyApp.route("/")
@MyApp.route("/index")
def index():
    user = {'username': 'Kaylan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    
@MyApp.route('/pics')
def pics():
    return render_template('pics.html', title='Pictures')
    
@MyApp.route('/poems')
def poems():
    return render_template('poems.html', title='Poems')
    
@MyApp.route('/updates')
def updates():
    return render_template('updates.html', title='Updates')
    
@MyApp.route('/login')
def login():
    return render_template('login.html', title='Sign In')
    
@MyApp.route('/about')
def about():
    return render_template('about.html', title='About')
    
if __name__ == "__main__":
        MyApp.run(debug=true)

