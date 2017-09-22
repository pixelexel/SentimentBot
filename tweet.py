import tweepy
from textblob import TextBlob


consumer_key= 'ZCNfouynyIW3PIikLGmaOiiIq'
consumer_secret= '6FE7ZrB8c06N4Sxt9YU3LUU16Nft6quAILqPaBAgEpylYVW8GW'

access_token= '911236262580776960-X8hvHurq7Z7whzrgLCvJLgIoVYy0rNG'
acces_token_secret= 'NSfkaqitOg5srws3FqcHBevBkwovMGy97JdCPJhEgx0QC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

word = raw_input('') #Change to input if using Python3
public_tweets = api.search(word)

positive_tweets = 0.0
total_tweets = 0.0

for tweet in public_tweets:

	analysis = TextBlob(tweet.text)

	total_tweets += 1.0

	if analysis.sentiment.polarity > 0: #POSITIVE sentiments
		positive_tweets += 1.0


if positive_tweets/total_tweets >0.8:
	print('Twitter loves ' + word)

elif positive_tweets/total_tweets > 0.5:
	print('Twitter has good things to say about ' + word)

elif positive_tweets/total_tweets > 0.3:
	print('Twitter doesn\'t really like ' + word)
else:
	print('Twitter hates ' + word)
