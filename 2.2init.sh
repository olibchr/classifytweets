#!/bin/bash
sudo apt-get --assume-yes update
sudo apt-get install python2.7
wait
sudo apt-get install python-virtualenv 
wait
cd ~
sudo wget https://github.com/recap/pumpkin/archive/tracula.zip
wait
sudo apt-get --assume-yes install unzip
unzip tracula.zip
wait
pip install --upgrade pip
wait
pip2 install netaddr
wait
pip2 install ujson
wait
pip2 install pika
wait
pip2 install pystun
wait
cd pumpkin-tracula
sudo python setup.py install
wait
cd ~/
git clone https://github.com/olibchr/classifytweets
pip2 install nltk
wait
pip2 install numpy
wait
pip2 install python-twitter
wait
cd classifytweets
mkdir ~/nltk_data
mkdir ~/nltk_data/classifiers
cp ./movie_reviews_NaiveBayes.pickle ~/nltk_data/classifiers/
cd ~/
mkdir ~/tmp
mkdir ~/tmp/rx


