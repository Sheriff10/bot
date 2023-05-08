#Importing modules/libraries
import tweepy
import time

# Initialization code
# auth = tweepy.OAuthHandler("oK8Eh25QWf5an627XHuMYvN4B", "qDpoWkhY5llw3wy6rw7XagO1SJdGMuNsf9iSaopJaTIvrl5lzO")
# auth.set_access_token("1654339388036509696-jPfBF9AU28Nug9W7B3bm8oo6Ha9nye", "30lDtHSgorYkCiM1wxyU7hT7VoSRp5J3Nm0ob53vZp6uI")
# api = tweepy.API(auth)

bearer_token="AAAAAAAAAAAAAAAAAAAAAGY6nQEAAAAAF6IEJtnyTKlDOdqk0cmJOdZ1wJo%3DY1hJd1bxCZDRAfhNKkoSNg3GgmkyjMxzC9WyVVCxbmIhFTuBxh"
consumer_key="oK8Eh25QWf5an627XHuMYvN4B"
consumer_secret="qDpoWkhY5llw3wy6rw7XagO1SJdGMuNsf9iSaopJaTIvrl5lzO"
access_token="1654339388036509696-jPfBF9AU28Nug9W7B3bm8oo6Ha9nye"
access_token_secret="30lDtHSgorYkCiM1wxyU7hT7VoSRp5J3Nm0ob53vZp6uI"

client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# here we get your id to use it to find tweets you're tag in
user = client.get_me()
try:
    # we get the mentions
    mentions = client.get_users_mentions(user.data.id)
    # then we loop through it
    for mention in mentions:
        print(mention)
    print("Authentication OK")
except Exception as e:
    print("Error during authentication")
    print(e)



# HERE'S THE PROBLEM SECTION.
# Trying tp keep the stream active but it's giving error

search_terms = ["python", "programming", "coding"]

# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when the stream is working
    def on_connect(self):
        print("Connected")


    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        # Displaying tweet in console
        if tweet.referenced_tweets == None:
            print(tweet.text)
            client.like(tweet.id)

            # Delay between tweets
            time.sleep(0.5)
        

# Creating Stream object
stream = MyStream(bearer_token=bearer_token)

# Adding terms to search rules
# It's important to know that these rules don't get deleted when you stop the
# program, so you'd need to use stream.get_rules() and stream.delete_rules()
# to change them, or you can use the optional parameter to stream.add_rules()
# called dry_run (set it to True, and the rules will get deleted after the bot
# stopped running).
for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

# Starting stream
stream.filter(tweet_fields=["referenced_tweets"])