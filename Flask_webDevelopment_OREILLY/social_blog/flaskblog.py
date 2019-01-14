from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
        {
            'author':'John Smith',
            'title':'first post',
            'content': '1st post content',
            'date_posted': 'Jan 14 1996'
            },
        { 
            'author':'Jane Doe',            
            'title':'2nd post',
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


if __name__ == "__main__":
    app.run(debug=True)

