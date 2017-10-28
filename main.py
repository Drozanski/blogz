from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:cheese@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = '12345'


class BlogTable(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))
    

    def __init__(self, title, body):
        self.title = title
        self.body = body
        



@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    if request.method == 'POST':
        Blogtitle = request.form["blog_title"]
        Blogbody = request.form["blog_body"]
        fail_title = ""
        fail_body = ""

    if title == "":
        fail_title = "Please fill in the title"
    if body == "":
        fail_body = "Please fill in the body"

    return render_template('newpost.html')


@app.route('/blog', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        Blogtitle = request.form['blog_title']
        Blogbody = request.form['blog_body']
        new_title = blog_title(Blogtitle)
        new_body = blog_body(Blogbody)
        db.session.add(new_title)
        db.session.add(new_body)
        db.session.commit()

    return render_template('newpost.html',title="Build-a-Blog!", Blogtitle=Blogtitle, Blogbody=Blogbody)


if __name__ == '__main__':
    app.run()


   
