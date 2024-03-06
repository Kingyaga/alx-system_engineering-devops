#!/usr/bin/python3
""" Advance API module """
import json
import requests


def number_of_subscribers(subreddit):
    """ Get number of subscribers for a subreddit """
    try:
        headers = {'User-Agent': '0x16-api_advanced:project:\
        v1.0.0 (by /u/Moh\'King Yaga'}
        count = requests.get('https://www.reddit.com/r/{}/about.json'.format(
                             subreddit), headers=headers)
        count.raise_for_status()
        return count.json().get('data', {}).get('subscribers', 0)
    except Exception:
        return 0
