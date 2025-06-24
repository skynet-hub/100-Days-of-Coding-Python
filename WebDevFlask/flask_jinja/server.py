from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_num = randint(0, 9)
    year = datetime.now().year
    return render_template('index.html', num=random_num, year=year)

@app.route('/guess/<string:name>')
def profile(name):
    params = {
        "name": name
    }
    response = requests.get("https://api.genderize.io", params=params)
    data = response.json()
    gender = data["gender"]

    response2 = requests.get("https://api.agify.io", params=params)
    data2 = response2.json()
    age = data2["age"]

    return render_template('profile.html', name=name, gender=gender, age=age) 

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)