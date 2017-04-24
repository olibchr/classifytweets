#!/bin/bash
sudo apt-get update
wait
sudo apt-get install python2.7
wait
sudo apt-get install python-virtualenv 
wait
cd ~
sudo wget https://github.com/recap/pumpkin/archive/tracula.zip
wait
sudo apt-get install unzip
unzip tracula.zip
wait
pip install netaddr
wait
pip install ujson
wait
pip install pika
wait
pip install pystun
wait
cd pumpkin-tracula
sudo python setup.py install
wait
cd ~/
git clone https://github.com/olibchr/classifytweets
pip install nltk
wait
pip install numpy
wait
pip install dateutil
wait
cd classifytweets
mkdir ~/nltk_data
mkdir ~/nltk_data/classifiers
cp ./movie_reviews_NaiveBayes.pickle ~/nltk_data/classifiers/


