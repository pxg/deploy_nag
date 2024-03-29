from flask import Flask, request

from slack import post_to_slack

app = Flask(__name__)


def get_diff_url(head, prev_head):
    prev_head_short = prev_head[0:8]
    return f"https://github.com/pxg/deploy_nag/compare/{prev_head_short}...{head}"


@app.route("/", methods=["GET", "POST"])
def index():
    diff_url = get_diff_url(request.form["head"], request.form["prev_head"])
    print(request.form["user"])
    post_to_slack(diff_url)
    return "Hello Pete!"
