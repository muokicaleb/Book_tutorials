from datetime import datetime
from flask import Flask
from flask import render_template
from flask_moment import Moment
from flask_bootstrap import Bootstrap


app = Flask(__name__)
moment = Moment(app)
Bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


if __name__ == '__main__':
    app.run(debug=True)
