#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot articles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords in hot article titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        if after is not None:
            print_counts(counts)
        return

    data = response.json().get("data", {})
    for post in data.get("children", []):
        words = post.get("data").get("title").lower().split()
        for word in word_list:
            counts[word.lower()] += words.count(word.lower())

    after = data.get("after")
    if after is None:
        print_counts(counts)
        return
    count_words(subreddit, word_list, after, counts)


def print_counts(counts):
    """Print keywords with a count above 0, by count then alphabetically."""
    found = [(word, count) for word, count in counts.items() if count > 0]
    for word, count in sorted(found, key=lambda item: (-item[1], item[0])):
        print("{}: {}".format(word, count))
