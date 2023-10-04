from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import EmailField
#StringField is the box on the website to submit strings and submit is to submit 
from wtforms import StringField, SubmitField
#The validators are if the user didn't put something in the field we want something to pop up 
#and tell the user that he didn't sumbit anything.
from wtforms.validators import DataRequired, Email, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret key"
moment = Moment(app)
bootstrap = Bootstrap(app) 

#Should not be here if pushed to git (the above key)
from datetime import datetime

class NamerForm(FlaskForm):
    name = StringField("What is your name ?", validators=[DataRequired()])
    mail = EmailField("What is your email?", validators=[DataRequired(), Email("Please enter your email")])
    submit = SubmitField("Submit")


 


#This is for page not found error 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404error.html'), 404

#This is for server problem
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500error.html'), 500


@app.route('/home')
def home_p():
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def name_p():

    form = NamerForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_mail = session.get('mail')
        if old_name is not None and old_name != form.name.data and old_mail is not None and old_mail != form.mail.data:
            flash('Looks like you have changed your name!')
            flash('Looks like you have changed your mail!')
        elif old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        elif old_mail is not None and old_mail != form.mail.data:
            flash('Looks like you have changed your mail!')
            #return redirect(url_for('home_p'))
        # name = form.name.data
        # mail = form.mail.data
        # Clear the session variables
 
        session['name'] = form.name.data
        session['mail'] = form.mail.data
        return redirect(url_for('name_p'))

        # form.name.data = ''
        # form.mail.data = ''   
    return render_template("name.html", name = session.get('name'), form = form, mail = session.get('mail'))

