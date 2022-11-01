from tweepy.streaming import Stream
from tweepy import OAuthHandler
import tweepy as tw
from tweepy import Stream
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')
access_token = "871121738926632964-TunpyV6pH3MrfYABv83lYzVZsdi1y1U"
access_token_secret = "9RCNKN5NnUlTWV9KkjNfuj6DBct1WsgBaj3k4HRIyqeSy"
consumer_key = "2OFhEjwY7RaRB7Hxx3Q7U5kId"
consumer_secret = "XfJNGRtGOgFhMMF0VfwfJzWtHD3gmt5FzOUrz1y9vhHAf67Y7o"
topic_name = "twitter"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "RickyMartin"
date_since = "2021-09-28"

tweets = tw.Cursor(api.search_tweets,
              q=search_words,
              lang="es", #opcional
              since=date_since).items(5)
