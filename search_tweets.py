import twitter_connection as tc


class Tweet:
    def __init__(self, text, location):
        self.text = text
        self.location = location


tweets_with_hashtag = []

# search the tweets with the hashtag COVID19 posted in the last 30 days
# put all these tweets in a list
for tweets in tc.api.search_30_day(label="Recent", query="#COVID19", maxResults=10):
    current_tweet = Tweet(tweets.text, tweets.user.location)
    tweets_with_hashtag.append(current_tweet)
