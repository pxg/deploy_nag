import os

import requests


# TODO: type hints
def get_slack_user(email):
    # TOOD: will the email address always be a zero deposit one?
    # TODO: connect to Slack API to get user for email address
    # TODO: tests
    return "Pete"


# TODO: type hints
def post_to_slack(diff_url):
    # TODO: Add @ message work properlly
    message = f"There's new code on UAT. Can it be deployed to production? {diff_url}."
    post_message_to_slack(message)
    print(message)
    return


def post_message_to_slack(text, blocks=None):
    """
    Technique from https://keestalkstech.com/2019/10/simple-python-code-to-send-message-to-slack-channel-without-packages/
    TODO: Research using blocks
    """
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        {
            "token": os.environ.get("SLACK_TOKEN"),
            "channel": "petes-playground",
            "text": text,
        },
    ).json()
    import pdb; pdb.set_trace()
    return response
