from flask import Flask, render_template, request
import requests
from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

gmail_user = os.environ.get("GMAIL")
passw = os.environ.get("PASS")


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        message = "Message successfully sent"
        with SMTP("smtp.gmail.com") as server:
            server.starttls()
            server.login(user=gmail_user, password=passw)
            text= f"subject: New Message\n\n Name: {data["name"]}\n email: {data["email"]}\ncell Number: {data["phone"]}\nMessage: {data["message"]}"
            server.sendmail(from_addr=gmail_user, to_addrs="magobowltcode@gmail.com", msg=text)
            print("Sent successfully")
        return render_template("contact.html", message=message)
    message = "Contact Us."
    return render_template("contact.html", message=message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
