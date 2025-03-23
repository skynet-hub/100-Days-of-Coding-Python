from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<id>')
def get_post(id):
    return render_template('post.html', posts=all_posts, id=int(id))
           

if __name__ == "__main__":
    app.run(debug=True)
