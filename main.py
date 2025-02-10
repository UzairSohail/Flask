from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(),
                                             validators.Email()])
    password = PasswordField('password', validators=[DataRequired(), validators.Length(min=6), ])
    submit = SubmitField(label="submit")


app = Flask(__name__)

app.secret_key = "nacho_key"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    _form = MyForm()
    if _form.validate_on_submit():
        if _form.email.data == "admin@email.com" and _form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=_form)


if __name__ == '__main__':
    app.run(debug=True)
