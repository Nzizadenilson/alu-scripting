#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:reddit.hot:v1.0"
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )
        
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    except (requests.RequestException, ValueError, KeyError):
        print(None)

