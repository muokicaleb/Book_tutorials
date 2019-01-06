from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard string'

bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None 
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data 
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True)

