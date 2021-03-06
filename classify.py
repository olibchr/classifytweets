__author__ = 'oliver'

###START-CONF
##{
##"object_name": "classify",
##"object_poi": "my-classify-1234",
##"auto-load" : false,
##"parameters": [ {
##                  "name": "tweets",
##                  "description": "tweets to classify",
##                  "required": true,
##                  "type": "String",
##                  "state" : "UNCLASSIFIED"
##              } ],
##"return": [
##              {
##                  "name": "predictions",
##                  "description": "all predictions",
##                  "required": true,
##                  "type": "String",
##                  "state" : "PREDICTED"
##               }
##
##          ] }
##END-CONF

import nltk, json
import datetime, numpy
from dateutil import parser
import sys
from pumpkin import *



classifier = nltk.data.load("classifiers/movie_reviews_NaiveBayes.pickle")

class TTweet():
    def __init__(self, date, text):
        self.date = parser.parse(date)
        self.text = text
        self.prediction = None
        self.serialized = {}
    def serialize(self):
        self.serialized = {
            'date': self.date,
            'text': self.text,
            'prediction': self.prediciton
        }
        return self.serialized

class greet(PmkSeed.Seed):
    def __init__(self, context, poi=None):
        PmkSeed.Seed.__init__(self, context,poi)
        pass
    def run(self, pkt, tweets):
        """ Data is transformed at intermediate points on its way
        to a destination. In this case we are simply adding
        "hello" to a name to form a greeting. This will be
        dispatched and received by a collector.
        """
        data = json.loads(tweets)
        tweets = []
        for t in data:
            tweets.append(TTweet(t['date'], t['tweet']))
        for t in tweets:
            print t
            tokens = nltk.word_tokenize(t.text)
            feats = dict([(word, True) for word in tokens])
            t.prediction = classifier.classify(feats)
        for r in allTweets:
            r.serialize()
        self.dispatch(pkt, [e.serialized for e in tweets], "PREDICTED")
        pass













