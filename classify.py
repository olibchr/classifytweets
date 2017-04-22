import nltk, json
from nltk.corpus import stopwords
import datetime, numpy
from flask import Flask, request, jsonify
from dateutil import parser
import matplotlib
import sys
app = Flask(__name__)


class Tweet():
    def __init__(self, date, text):
        self.date = parser.parse(date)
        self.text = text
        self.prediciton = None
        self.serialized = {}
    def serialize(self):
        self.serialized = {
            'date': self.date,
            'text': self.text,
            'prediction': self.prediciton
        }
        return self.serialized


@app.route('/', methods=['POST'])
def predict_class():
    data = json.loads(request.form['tweets'])
    tweets = []
    for t in data:
        tweets.append(Tweet(t['date'], t['tweet']))
    for t in tweets:
        print t
        tokens = nltk.word_tokenize(t.text)
        filtered_tokens = [i.lower() for i in tokens if i.lower() not in stop]
        feats = dict([(word, True) for word in filtered_tokens])
        t.prediciton = classifier.classify(feats)
    return jsonify([e.serialize() for e in tweets]), 200, {'ContentType':'application/json'}


if __name__ == '__main__':
    classifier = nltk.data.load("classifiers/movie_reviews_NaiveBayes.pickle")
    stop = set(stopwords.words('english'))
    app.run(host='0.0.0.0', debug=True)












