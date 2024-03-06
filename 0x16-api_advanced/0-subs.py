#!/usr/bin/python3
"""
Module for querying the Reddit API for a given subreddit's subscriber count.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    try:
        headers = {'User-Agent': '0x16-api_advanced:project: v1.0.0 (by /u/Moh\'King Yaga'}
        count = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers)
        count.raise_for_status()
        return count.json().get('data', {}).get('subscribers', 0)
    except Exception:
        return 0