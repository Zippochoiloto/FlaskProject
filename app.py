from flask import Flask, render_template

app = Flask(__name__)

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