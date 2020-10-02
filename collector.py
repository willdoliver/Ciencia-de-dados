# -*- encoding: utf-8 -*-
from TwitterAPI import TwitterAPI
import GetOldTweets3 as got
from dotenv import load_dotenv
import simplejson as json
import os
load_dotenv()

# Try to find old data
# https://www.yelp.com/dataset

# Um registro no website da API fornece as credenciais indicadas aqui
twitter_api = TwitterAPI(consumer_key=os.getenv("TWITTER_API_KEY"),
              consumer_secret=os.getenv("TWITTER_API_SECRET_KEY"),
              access_token_key=os.getenv("TWITTER_ACCESS_TOKEN"),
              access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")) 

# Busca twitts em tempo real de acordo com palavra determinada
filters = {"track": ["covid-19", "infected"]} #palavra que deseja buscar em tweets

stream = twitter_api.request('statuses/filter', filters).get_iterator()

fsaida = open('saidaColetaStream.txt','w')

for item in stream:
   itemString = json.dumps(item)
   fsaida.write(itemString+'\n')



