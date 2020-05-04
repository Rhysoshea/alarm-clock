from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, AlarmForm
import schedule
import time
import webbrowser, os, sys
from app import set_alarm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rhys'}
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/alarm', methods=['GET', 'POST'])
def alarm():
    form = AlarmForm()
    if form.validate_on_submit():
        flash('Alarm set for {}'.format(form.time.data))
        
        h = form.time.data[:2]
        m = form.time.data[2:]
        set_alarm.main(h,m)
##        schedule.every().day.at("{}:{}".format(h,m)).do(job)
        return redirect(url_for('index'))
    
    return render_template('alarm.html', title='Sign In', form=form)
