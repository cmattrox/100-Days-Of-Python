import requests
from flask import Flask, render_template

app = Flask(__name__)


res = requests.get("https://api.npoint.io/24f9ec237e7811a417a1").json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=res)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in res:
        print(blog_post)
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run()
