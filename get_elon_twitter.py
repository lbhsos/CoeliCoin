import twitter
import requests
import pprint 
from time import sleep
import json
from dotenv import load_dotenv
import os

load_dotenv()
twitter_consumer_key = os.environ["twitter_consumer_key"]
twitter_consumer_secret = os.environ["twitter_consumer_secret"]
twitter_access_token = os.environ["twitter_access_token"]
twitter_access_secret = os.environ["twitter_access_secret"]

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

account = "@elonmusk"
last_sid = float('-inf')
SLACK_URL=os.environ["SLACK_URL"]
while True:
    statuses = twitter_api.GetUserTimeline(screen_name=account, count=50, include_rts=False, exclude_replies=True)
    twits = statuses[:5]
    twits.reverse()
    
    for twit in twits:
        if twit.id > last_sid:

            last_sid = twit.id
            text_dat = twit.text + "\n" + 'https://twitter.com/elonmusk/status/'+str(twit.id)
            requests.post(SLACK_URL, data = json.dumps({"text":text_dat}))

    sleep(3)



