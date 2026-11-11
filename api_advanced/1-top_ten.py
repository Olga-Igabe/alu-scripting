#!/usr/bin/python3
"""Query the Reddit API for the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        posts = response.json().get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    except Exception:
        print(None)
