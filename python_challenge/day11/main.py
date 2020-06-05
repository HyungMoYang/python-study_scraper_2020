import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

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

app = Flask("DayEleven")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/read")
def reddits_reader():
    check_list = []  # form chcek list
    sub_list = []  # list of reddit post

    # get check_list
    for sub_reddit in subreddits:
        rst = request.args.get(f"{sub_reddit}")
        if rst == 'on':
            check_list.append(sub_reddit)

    # get sub_reddits data
    for sub in check_list:
        url = f"https://www.reddit.com/r/{sub}/top/?t=month"
        rst = requests.get(url, headers=headers)
        soup = BeautifulSoup(rst.text, "html.parser")

        body = soup.find("div", {"class": "_1OVBBWLtHoSPfGCRaPzpTf"})
        card = body.find_all("div", {"class": "_3xuFbFM3vrCqdGuKGhhhn0"})

        for idx, ca in enumerate(card):
            card_side = ca.find("div", {"class": "_23h0-EcaBUorIHC-JZyh6J"})
            card_main = ca.find("article", {"class": "yn9v_hQEhjlRNZI0xspbA"})
            # card_main = ca.find("div", {"class":"_1poyrkZ7g36PawDueRza-J"})

            title = card_main.find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
            vote = card_side.find("div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"})
            url = card_main.find(
                "a", {"class": "SQnoC3ObvgnGjWt90zD9Z"})['href']

            if "k" in vote.get_text():
                continue

            # if "k" in vote.get_text():
            #   temp = vote.get_text().replace("k", "")
            #   upvote = int(float(temp)) * 1000 # ?? float()쓸때 소수점 어떻게 살리지?
            # else:
            #   upvote = int(vote.get_text())

            sub_list.append(
                {"title": title.get_text(),
                 "upvotes": int(vote.get_text()),
                 "url": url,
                 "sub": f"r/{sub}"}
            )

    # sorting the sub_list
    sorted_sub_list = sorted(sub_list, reverse=True,
                             key=lambda sub_list: (sub_list["upvotes"]))

    return render_template(
        "read.html",
        sorted_sub_list=sorted_sub_list,
        check_list=check_list
    )


app.run(host="0.0.0.0")

