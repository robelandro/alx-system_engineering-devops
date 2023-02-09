#!/usr/bin/python3

"""Module for count_words method."""

import requests


def count_words(subreddit, word_list, after="", word_dict={}):
	"""Queries the Reddit API, parses the title of all hot articles,
	and prints a sorted count of given keywords (case-insensitive,
	delimited by spaces. Javascript should count as javascript,
	but java should not)."""
	url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
	params = {"limit": 100, "after": after}
	response = requests.get(url, headers=headers, params=params,
							allow_redirects=False)
	if response.status_code != 200:
		return None
	data = response.json().get("data")
	after = data.get("after")
	posts = data.get("children")
	for post in posts:
		title = post.get("data").get("title").lower()
		for word in word_list:
			word = word.lower()
			if word in title:
				if word in word_dict:
					word_dict[word] += 1
				else:
					word_dict[word] = 1
	if after is not None:
		return count_words(subreddit, word_list, after, word_dict)
	else:
		if len(word_dict) == 0:
			return None
		sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
		for word in sorted_words:
			print("{}: {}".format(word[0], word[1]))
