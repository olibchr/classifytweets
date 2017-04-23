__author__ = 'oliver'

###START-CONF
##{
##"object_name": "plot",
##"object_poi": "my-plot-1234",
##"auto-load" : false,
##"parameters": [ {
##                  "name": "predictions",
##                  "description": "predictions to plot",
##                  "required": true,
##                  "type": "String",
##                  "state" : "PREDICTED"
##              } ],
##"return": [
##
##          ] }
##END-CONF

import nltk, json
from nltk.corpus import stopwords
import datetime, numpy, time
from flask import Flask, request, jsonify
from dateutil import parser
import matplotlib.pyplot as plt
import sys
from pumpkin import *


class Tweet():
    def __init__(self, date, prediction):
        self.date = parser.parse(date)
        self.prediction = prediction

class greet(PmkSeed.Seed):
    def __init__(self, context, poi=None):
        PmkSeed.Seed.__init__(self, context,poi)
        pass
    def run(self, pkt, predictions):
        """ Data is transformed at intermediate points on its way
        to a destination. In this case we are simply adding
        "hello" to a name to form a greeting. This will be
        dispatched and received by a collector.
        """
        data = json.loads(predictions)
        tweets = []
        for t in data:
            tweets.append(Tweet(t['date'], t['prediction']))
        dates = []
        predictions = []
        t = 0
        while(t<len(tweets)):
            subSet = tweets[t:len(tweets)/10+t]
            this_date = 0
            this_pred = []
            for tweet in subSet:
                this_pred += tweet.prediction
                this_date += time.mktime(tweet.date)
            this_pred = this_pred/len(subSet)
            this_date = this_date/len(subSet)
            dates.append(this_date)
            predictions.append(this_pred)
            t += len(subSet)
        plt.plot(dates, predictions)
        plt.savefig('predictions.png', bbox_inches='tight')
        pass












