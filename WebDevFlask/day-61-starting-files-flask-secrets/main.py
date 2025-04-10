from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4, message='Password needs to be a minimum of 4 characters')])
    submit = SubmitField(label='Login')


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:    
        return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)