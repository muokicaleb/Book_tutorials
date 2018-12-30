from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/index')
def baseindex():
    # this route uses inherited template
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
