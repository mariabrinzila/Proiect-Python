import twitter_connection as tc


class Tweet:
    def __init__(self, text, location):
        self.text = text
        self.location = location


def generateTweetsWithHashtag(hashtag, number):
    tweets_with_hashtag = []
    API = tc.connectToAPI()

    # search the tweets with the hashtag COVID19 posted in the last 30 days
    for tweets in API.search_30_day(label="Recent", query=hashtag, maxResults=number):
        current_tweet = Tweet(tweets.text, tweets.user.location)
        tweets_with_hashtag.append(current_tweet)

    return tweets_with_hashtag
