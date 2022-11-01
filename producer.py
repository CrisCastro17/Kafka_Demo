from tweepy.streaming import Stream
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')
access_token = "871121738926632964-TunpyV6pH3MrfYABv83lYzVZsdi1y1U"
access_token_secret = "9RCNKN5NnUlTWV9KkjNfuj6DBct1WsgBaj3k4HRIyqeSy"
consumer_key = "2OFhEjwY7RaRB7Hxx3Q7U5kId"
consumer_secret = "XfJNGRtGOgFhMMF0VfwfJzWtHD3gmt5FzOUrz1y9vhHAf67Y7o"
topic_name = "twitter"
class StdOutListener(Stream):
  def on_data(self, data):
    producer.send(topic_name, bytes(data))
    print(data)
    return True

  def on_error(self, status):
    print(status)
  
if __name__ == '__main__':
  while True:
    l = StdOutListener(consumer_key, consumer_secret, access_token, access_token_secret)
    #auth = OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
    #stream = Stream(auth, l)
    l.filter(    track=["cristina","paso2021","elecciones","alberto fernandez","macri","milei","Vidal","santili","juntos por el cambio","frente de todos","elecciones argentina","14N","paso2021"]
    ,languages=["es"]
	)
               