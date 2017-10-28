
from flask import Flask, request, redirect, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:cheese@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = '12345'

blog_posts = []

db = SQLAlchemy(app)


class blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return '<BlogPost %r>' % self.body


@app.route('/add', methods=['POST', 'GET'])
def add():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        if not title or not body:
            flash("Incorrect title or body!")
            return redirect('/add')

       

        blog_post = blog(title, body)
        db.session.add(blog_post)
        db.session.commit()
        new_url = "/?id=" + str(blog_post.id)
        return redirect(new_url)

    return render_template('add-blog.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.args.get('id'):
        id = request.args.get('id')
        blog_page = blog.query.filter_by(id=id).first()
        return render_template('blog_page.html', blog_page=blog_page)

    return render_template('view.html', title="Build a Blog", blog_posts=blog.query.all())


if __name__ == '__main__':
    app.run()
