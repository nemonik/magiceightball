from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import random

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
answers = [
    "It is certain",
    "It is decidedly so", 
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

class MagicEightBallForm(Form):
    name = TextField('Ask your question:', validators=[validators.required()])
 
def answer(question):
    return answers[random.randint(0,19)]


@app.route("/", methods=['GET', 'POST'])
def questionForm():
    form = MagicEightBallForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        question=request.form['question']
 
        if question:
            flash(answer(question))
        else:
            flash('Error: You must ask a question.')
 
    return render_template('magicEightBall.html', form=form)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
