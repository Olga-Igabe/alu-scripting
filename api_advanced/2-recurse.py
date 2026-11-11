#!/usr/bin/python3
"""Recursively query the Reddit API for all hot article titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot article titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return hot_list or None

    data = response.json().get("data", {})
    titles = [post.get("data").get("title")
              for post in data.get("children", [])]
    hot_list = hot_list + titles

    after = data.get("after")
    if after is None:
        return hot_list or None
    return recurse(subreddit, hot_list, after)
