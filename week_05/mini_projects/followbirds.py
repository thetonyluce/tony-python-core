'''
Using the tweepy package, build a script that classifies a group of twitter handles
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''
import tweepy
import time
from pprint import pprint
from secret import *


# Twitter Dev Keys
auth = tweepy.OAuthHandler('Dnca7mdz0RQDu19lBErAs1UKF', 'a6fk9bm4toqmLVuGwPdatA3PNUEIcySe4kGtWmZl2AVTfLc0wO')
auth.set_access_token('2337431-hVrCFQoG8RXavr9mlNJP7sk0XmsWOHqudSMZX7zE9E',
                      'yxlMDkYnBZfS9UeeNqYVNixZpIQSpPySD0W7LQ5aeUvoH')

# API setting
api = tweepy.API(auth)


# class Twitterer(object):
#     def __init__(self, name, profession):
#         self.name = name
#         self.profession = profession


# API calls - prints based on number of followers
for user in tweepy.Cursor(api.friends, screen_name="tonyluce").items(200):
    friends_followers = (user.screen_name, user.followers_count)

    if user.followers_count > 999999:
        print(f"$$$ Chamillionaire: {user.screen_name}, {user.followers_count} followers.")

    elif user.followers_count > 99999:
        print(f"$$ Hunnies of Thousies: {user.screen_name}, {user.followers_count} followers.")

    elif user.followers_count > 9999:
        print(f"$ Still Cool: {user.screen_name}, {user.followers_count} followers.")

    else:
        print(f"Needs Work: {user.screen_name}, {user.followers_count} followers.")
