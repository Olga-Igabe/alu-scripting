#!/usr/bin/python3
"""Query the Reddit API for the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    for post in response.json().get("data", {}).get("children", [])[:10]:
        print(post.get("data").get("title"))
