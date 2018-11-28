from flask import Flask, render_template, Markup, request, flash, session, redirect
import random
from config import Config
import sqlite3
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
    
@MyApp.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'thedude' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            session['username'] =  request.form['username']
            session['logged_in'] = True
            #user_count = db_query('SELECT COUNT(*) FROM USERS WHERE username = ?', [username])
            #if(user_exists[0][0] == 1):
                #password_true = query_db('SELECT COUNT(*) FROM USERS WHERE username = ? AND password = ?', (username, password))
            #if(password_true[0][0] == 1):
                #session['username'] = "username"
            flash('You were successfully logged in')
            return redirect('/secret')
            
    return render_template('login.html', error=error, title='Sign In')
    
@MyApp.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect('/index')
    
@MyApp.route('/about')
def about():
    return render_template('about.html', title='About')
    
@MyApp.route('/secret')
def secret():
    #if request.method != 'POST':
        error = None
        if session['logged_in'] == True:
            return render_template('secret.html')
        else:
            error = 'You must be logged in to access this page!'
        return render_template('login.html', error=error, title='Sign In')
        
   

   
### DATABASE SECTION ###
def db_query(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('lab.db')
    return db
    
if __name__ == "__main__":
        MyApp.run(debug=true)

