import tweepy
import time


FILE_NAME = 'last_seen_id.txt'


def store_last_seen_id(lastseenid, filename):
    fp = open(filename, 'w')
    fp.write(str(lastseenid))
    fp.close()
    return

def retrieve_last_seen_id(filename):
    fp = open(filename, 'r')
    last_seen_id = int(fp.read())
    fp.close()
    return last_seen_id
    

#initialize these keys with your developer's account
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def reply_to_tweets():
    print ("Replying to tweets")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#replyme' in mention.full_text.lower():
            reply = " Found you.. I'll reply you in -2 seconds..... Oops I already replied. My bad :("
            api.update_status('@' + mention.user.screen_name +
                                                             reply, mention.id)


while True:
    reply_to_tweets()
    time.sleep(15)
            
