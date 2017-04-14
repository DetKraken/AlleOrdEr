#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time

keyList = []

def AlleOrdEr(pretext, words):
    #Create a function that calls and gets total tweets so I dont have to manually edit this shit pls~
    for i in range(122, len(words)):
        tweet = '{0}{1}'.format(pretext, words[i])
        tweet = tweet.decode('unicode_escape').encode('utf-8')
        api.update_status(tweet)
        time.sleep(1800)

def setText(txtFile):
    wordList = []
    with open(txtFile, 'r') as f:
        for line in f:
            wordList.append(line)
    wordList.sort()
    return wordList

with open('/src/keys.txt', 'r') as f:
    keys = f.read()
    keyList = keys.split(';')
    f.close()

auth = tweepy.OAuthHandler(keyList[0],keyList[1])
auth.set_access_token(keyList[2],keyList[3])
api = tweepy.API(auth)

AlleOrdEr("Pik ", setText('/src/danish_words.text'))
