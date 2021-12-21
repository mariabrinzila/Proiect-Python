import twitter_connection as tc
from geopy.geocoders import Nominatim


class Tweet:
    def __init__(self, text, location, longitude, latitude):
        self.text = text
        self.location = location
        self.longitude = longitude
        self.latitude = latitude


class Location:
    def __init__(self, lat, long):
        self.latitude = lat
        self.longitude = long


def generateTweetsWithHashtag(hashtag, number):
    tweets_with_hashtag = []
    API = tc.connectToAPI()
    geo_locator = Nominatim(user_agent="Project")
    locations = []

    # search number of tweets with the hashtag posted in the last 30 days
    # calculate their coordinates
    # latitude 0 and longitude 0 <=> Gulf of Guinea
    for tweets in API.search_30_day(label="Recent", query=hashtag, maxResults=number):
        if tweets.user.location is not None:
            tweet_coordinates = geo_locator.geocode(tweets.user.location)

            if tweet_coordinates is not None:
                current_tweet = Tweet(tweets.text, tweets.user.location, tweet_coordinates.longitude,
                                      tweet_coordinates.latitude)
                current_location = Location(tweet_coordinates.latitude, tweet_coordinates.longitude)
                locations.append(current_location)
            else:
                current_tweet = Tweet(tweets.text, tweets.user.location, 0, 0)
        else:
            current_tweet = Tweet(tweets.text, tweets.user.location, 0, 0)
        tweets_with_hashtag.append(current_tweet)

    return tweets_with_hashtag, locations
