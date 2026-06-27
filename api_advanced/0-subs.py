#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:reddit.subscribers:v1.0"
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        return 0
    except (requests.RequestException, ValueError, KeyError):
        return 0
