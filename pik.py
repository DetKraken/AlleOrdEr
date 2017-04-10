import tweepy
import time

def ordTest(tid,txtArray):
    print "Start : %s" % time.ctime()
    time.sleep(1200)
    print "End : $s" % time.ctime()

def set_text(txtfile):
    wordList = []
    with open(txtfile, 'r') as f:
        for line in f:
            wordList.append(line)
    wordList.sort()
    f.close()
    return wordList

def AlleOrdEr(pretext, words):
    f.close()
    for i in range(0, len(words)):
        api.update_status('{0}{1}'.format(pretext, words[i]))
        time.sleep(600)


with open('/var/www/html/kraken.work/Twitter_bots/AlleOrdEr/Pik/src/keys.txt', 'r') as f:
    keys = f.read()
    keyList = keys.split(";")
    f.close()

ck = keyList[0]
cs = keyList[1]
at = keyList[2]
ats = keyList[3]
auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(at, ats)
api = tweepy.API(auth)

AlleOrdEr("Pik ",set_text('/var/www/html/kraken.work/Twitter_bots/AlleOrdEr/Pik/src/danish_words.text'))