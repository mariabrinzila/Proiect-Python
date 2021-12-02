import tweepy as tw

# app keys
consumer_key = 'DTNhUzQ7EHUI9XHQZ9xuUrc2G'
consumer_secret = 'JShGSkczHzAMOAY5WZFk6vpSUETsm6XVkaWbaFDIdySTeIZJS5'
access_token = '1466436088105422863-H7TXzq461PEVPTDDP7a7FHsovrXz7y'
access_token_secret = '734ljvDU0Al2NW1WOwiR3NVndigHxRUuYRGcqeDbN06JF'

# connecting to Twitter, using the Twitter tweepy API
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tw.API(auth, wait_on_rate_limit=True)

# searching for tweets containing the hashtag COVID19
"""for tweets in api.search_tweets(q="#COVID19", count=100):
    print(tweets.text)
    print(tweets.user.location)
    print("###########################")
"""

# tweets with the hashtag COVID19 posted in the last 30 days
for tweets in api.search_30_day(label="Recent", query="#COVID19", maxResults=10):
    print(tweets.text)
    print(tweets.user.location)
    print("----------------")

"""auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tw.API(auth, wait_on_rate_limit=True)
client = tw.Client(bearer_token='')

# Replace with your own search query
query = 'covid'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)"""
