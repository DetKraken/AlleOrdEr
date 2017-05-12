#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time

def AlleOrdEr(pretext, words, tweetCount):
    #Create a function that calls and gets total tweets so I dont have to manually edit this shit pls~
    for i in range(tweetCount, len(words)):
        tweet = '{0}{1}'.format(pretext, words[i])
        tweet = tweet.decode('unicode_escape').encode('utf-8')
        api.update_status(tweet)
        break

def setText(txtFile):
    wordList = []
    with open(txtFile, 'r') as f:
        for line in f:
            wordList.append(line)
    wordList.sort()
    return wordList

def tweetCount(dir):
    cache = open(dir, 'r+')
    contents = int(cache.read())
    print(contents)
    cache.seek(0)
    cache.truncate()
    cache.write(str(contents+1))
    return contents

dir = 'localdir'
keyList = []

with open('{0}src/keys.txt'.format(dir), 'r') as f:
    keys = f.read()
    keyList = keys.split(';')
    f.close()

auth = tweepy.OAuthHandler(keyList[0],keyList[1])
auth.set_access_token(keyList[2],keyList[3])
api = tweepy.API(auth)
AlleOrdEr("Pik ", setText('{0}src/danish_words.text'.format(dir)), tweetCount('{0}src/count.txt'.format(dir)))