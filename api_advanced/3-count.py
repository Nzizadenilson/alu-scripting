#!/usr/bin/python3
"""
Recursively queries Reddit API and counts keywords in hot article titles.
"""
import re
import requests
def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    if after is None:
        word_map = {}
        for word in word_list:
            w = word.lower()
            word_map[w] = word_map.get(w, 0) + 1
    else:
        word_map = word_list
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:reddit.keyword:v1.0"
    }
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(
             url,
             headers=headers,
             params=params,
             allow_redirects=False
        )
        if response.status_code != 200:
            return
        data = response.json()

        posts = data["data"]["children"]

        for post in posts:
             title = post["data"]["title"].lower()

             words = re.findall(r"[a-z0-9]+", title)
             for w in words:
                 if w in word_map:
                     counts[w] = counts.get(w, 0) + word_map[w]
             after = data["data"]["after"]
             if after:
                 return count_words(subreddit, word_map, after, counts)
             sorted_counts = sorted(
                 counts.items(),
                 key=lambda x: (-x[1], x[0])
             )
             for k, v in sorted_counts:
                 print("{}: {}".format(k, v))
    except:
        return 




