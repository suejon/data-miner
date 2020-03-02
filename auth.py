import tweepy
from tweepy import OAuthHandler
from os import environ

consumer_key = environ.get('CONSUMER_KEY')
consumer_secret = environ.get('CONSUMER_SECRET')
access_token = environ.get('ACCESS_TOKEN')
access_secret = environ.get('ACCESS_SECRET')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
  print(status.text)