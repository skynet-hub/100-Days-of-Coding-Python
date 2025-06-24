from flask import Flask, render_template
import requests

app = Flask(__name__)

#Global variables
n_point = "https://api.npoint.io/23273a526eb74d54881c"

#Getting json from API
response = requests.get(n_point)
all_posts = response.json()


@app.route('/')
def Home():
    return render_template('index.html', posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/posts/<int:id>')
def post(id):
    index = int(id - 1)
    return render_template('post.html', posts=all_posts, index = index)

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5500)