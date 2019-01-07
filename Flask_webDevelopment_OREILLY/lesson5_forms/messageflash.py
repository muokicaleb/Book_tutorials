from flask import Flask
from flask import flash
from flask import redirect
from flask import session
from flask import url_for
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
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name ')
            session['name'] = form.name.data 
            form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    app.run(debug=True)

