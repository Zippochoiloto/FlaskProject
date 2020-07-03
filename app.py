from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
  id = db.Column(db.Interger, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  content = db.Column(db.Text, nullable=False)


all_posts = [
  {
    'title': 'Post 1',
    "content": "this is the content of post1",
    'author': 'The Anh'
  },
  {
    'title': 'Post 2',
    "content": "this is the content of post2"
  },
  {
    'title': 'Post 3',
    "content": "this is the content of post3"
  },
]

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/posts')
def posts():
  return render_template('post.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>',methods=['GET'])
def hello(name, id):
  return "Hello, " + name + ',your id is :' + str(id)

def get_req():
  return 'You can only get this webpage'

if __name__ == "__main__":
  app.run(debug=True)