#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return 0

    try:
        data = response.json()
        return data["data"]["subscribers"]
    except (ValueError, KeyError):
        return 0
