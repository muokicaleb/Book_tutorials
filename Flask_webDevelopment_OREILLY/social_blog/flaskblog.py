from flask import Flask 
from forms import RegistrationForm, LoginForm
from flask import render_template
from flask import url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = '315742e55f9228cea7c3d52418bda5e3'

posts = [
        {
            'author': 'John Smith',
            'title': 'first post',
            'content': '1st post content',
            'date_posted': 'Jan 14 1996'
            },
        {
            'author': 'Jane Doe',
            'title': '2nd post',
            'content': '2nd post content',
            'date_posted': 'Jan 14 1996'
            }
        ]


@app.route("/")
@app.route("/index")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register', form=form)

@app.route("/login")
def login:
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
