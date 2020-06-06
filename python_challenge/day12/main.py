from flask import Flask, render_template, request, redirect
from scrapper import aggregate_subreddits
import requests

app = Flask("RedditNews")

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


@app.route("/")
def home():
    return render_template("home.html", subreddits=subreddits)


@app.route("/read")
def read():
    selected = []
    for subreddit in subreddits:
        if subreddit in request.args:
            selected.append(subreddit)
    posts = aggregate_subreddits(selected)
    posts.sort(key=lambda post: post['votes'], reverse=True)
    return render_template("read.html", selected=selected, posts=posts)


@app.route("/add", methods=['POST'])
def add_subreddit():
    subreddit = request.form['new-subreddit']

    if '/r/' in subreddit:
        text_alarm = f'Write the name without /r/'
        return render_template('add.html', text=text_alarm)

    url = f"https://www.reddit.com/r/{subreddit}"
    rst = requests.get(url).status_code
    # print(f"{url}: {rst}")
    if rst == 404:
        text_alarm = 'That subreddit does not exist.'
        return render_template('add.html', text=text_alarm)
    else:
        subreddits.append(subreddit)
        return redirect("/")


app.run(host="0.0.0.0")
