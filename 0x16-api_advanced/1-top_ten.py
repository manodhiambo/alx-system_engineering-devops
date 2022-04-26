#!/usr/bin/python3
""" Program that use Reddit API and query How many subs are there? and list the
top ten"""
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit"""
    # me.json is a modhash token to prevent CSRF
    url_hot = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': 'My User Agent'}
    req = requests.get(url_hot, headers=h, allow_redirects=False,
                       params={'limit': 10})

    if (req.status_code == 200):
        req_json = req.json()
        list_hot = req_json['data']['children']
        for i in range(len(list_hot)):
            title = list_hot[i]['data']['title']
            print(title)
    else:
        print("None")
