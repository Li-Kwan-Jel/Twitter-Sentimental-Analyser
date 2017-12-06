import tweepy
from textblob import TextBlob
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key='YPF6r1F8FfVfW24gQ9FE6aEt9'
consumer_secret='vkNtbeFYgvJ20xZyQ2eFlF56O8imDg7YeYvlZTXpSsVIdsGgGm'


access_token='930688710726815744-m5jgG2afGmQKiA4TM4iJtHbKqdSG7Jo'
access_token_secret='47tbmHOGWk2xUT6W6OrlC352oOcdVRZ6zoSfjnYz41DMc'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")