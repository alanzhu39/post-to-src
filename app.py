from flask import Flask
from instaloader import Instaloader, Post

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/api/<shortcode>")
def api(shortcode):
  L = Instaloader()
  post = Post.from_shortcode(L.context, shortcode)
  return post.video_url
