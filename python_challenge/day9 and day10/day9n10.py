import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")

db[new] = requests.get(new).json()
db[popular] = requests.get(popular).json()

# index page


@app.route("/")
def home():
    rst = request.args.get('order_by', 'popular')
    if rst == 'new':
        print(rst)
        return render_template('newlist.html', db=db[new].get('hits'))
    elif rst == 'popular':
        return render_template('index.html', db=db[popular].get('hits'))


@app.route("/<id>")
def news_comment(id):
    comments_url = f"https://hn.algolia.com/api/v1/items/{id}"
    temp = requests.get(comments_url).json()
    t_title = temp.get('title')
    t_author = temp.get('author')
    t_url = temp.get('url')
    t_points = temp.get('points')
    t_db = temp.get('children')

    return render_template(
        'detail.html',
        title=t_title,
        author=t_author,
        url=t_url,
        points=t_points,
        db=t_db
    )


app.run(host="0.0.0.0")
