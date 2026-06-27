#!/usr/bin/python3
"""
Recursively queries Reddit API and returns list of hot post titles.
"""
import requests
def recurse(subreddit, hot_list=[], after=None):
     url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
     headers = {
         "User-Agent": "python:reddit.recursion:v1.0"
     }
     params = {
          "limit": 100
     }
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
            return None
         data = response.json()
         posts = data["data"]["children"]
         for post in posts:
             hot_list.append(post["data"]["title"])
             after = data["data"]["after"]
         if after is not None:
             return recurse(subreddit, hot_list, after)
         return hot_list
     except (requests.RequestException, ValueError, KeyError):
         return None

