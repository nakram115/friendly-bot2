# Dependencies
import numpy as np
import tweepy
import time
import json

consumer_key="kFjLsd3HrwjRF4VAOKXQ2fa1a"
consumer_secret= "Mq6Iu7azUwJ607TD13jzk6tngtbA2kYpZ0pXwyGHCCjffEpf5L"

access_token ="2675683644-bDoupHMkofhOY6DwnLYvCcgjmC6mmUTtvRXm2Ue"
access_token_secret= "4EiWrojlwjnOdaGfOS7tmSZ4LJJw7n20eey4dBNJmk8eN"

# Dependencies
import numpy as np
import tweepy
import time
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret



# Target Term
target_term = "@nakram115"

# Opening message
print("We're going live!")

# Create Thank You Function
def ThankYou():

    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Search for all tweets
    public_tweets = api.search(target_term, count=100, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets["statuses"]:

        # Get ID and Author of most recent tweet directed to me
        tweet_id = tweet["id"]
        tweet_author = tweet["user"]["screen_name"]

        # Print the tweet_id
        print(tweet_id)

        # Use Try-Except to avoid the duplicate error
        try:
            # Respond to tweet
            api.update_status(
                "Thank you @%s! Come again!" %
                tweet_author,
                in_reply_to_status_id=tweet_id)

            # Print success message
            print("Successful response!")

        except Exception:            # Print message if duplicate
            print("Already responded to this one!")

        # Print message to signify complete cycle
        print("We're done for now. I'll check again in 60 seconds.")

# Set timer to run every minute
while(True):
    ThankYou()
    time.sleep(60)
