import twitter_connection as tc
from geopy.geocoders import Nominatim


class Tweet:
    def __init__(self, text, location, longitude, latitude):
        """
        Tweet class constructor
        :param text: a tweet's text
        :param location: a tweet's location
        :param longitude: a tweet's longitude
        :param latitude: a tweet's latitude
        """
        self.text = text
        self.location = location
        self.longitude = longitude
        self.latitude = latitude


class Location:
    def __init__(self, lat, long):
        """
        Location class constructor
        :param lat: a location's latitude
        :param long: a location's longitude
        """
        self.latitude = lat
        self.longitude = long


def generate_tweets_with_hashtag(hashtag, number):
    """
    Function to connect to the Twitter API, search for the
    most recent number tweets with the hashtag, generate
    the coordinates of the location of each tweet (for the tweets
    that have valid locations)
    :param hashtag: hashtag that the user has inputted
    :param number: number of tweets that the user has inputted
    :return: tweets_with_hashtag (list of Tweet objects containing
    all the tweets generated) and locations (list of Location
    objects containing the coordinates of each generated tweet's
    location, if its location is valid)
    """
    tweets_with_hashtag = []
    api = tc.connect_to_twitter()
    geo_locator = Nominatim(user_agent="Project")
    locations = []

    # Search number of tweets with the hashtag posted in the last 30 days
    # Calculate their coordinates
    # Latitude 0 and longitude 0 <=> Gulf of Guinea
    for tweets in api.search_30_day(label="Recent", query=hashtag,
                                    maxResults=number):
        if tweets.user.location is not None:
            tweet_coordinates = geo_locator.geocode(tweets.user.location)

            if tweet_coordinates is not None:
                current_tweet = Tweet(tweets.text, tweets.user.location,
                                      tweet_coordinates.longitude,
                                      tweet_coordinates.latitude)
                current_location = Location(tweet_coordinates.latitude,
                                            tweet_coordinates.longitude)
                locations.append(current_location)
            else:
                current_tweet = Tweet(tweets.text, tweets.user.location, 0, 0)
        else:
            current_tweet = Tweet(tweets.text, tweets.user.location, 0, 0)

        tweets_with_hashtag.append(current_tweet)

    return tweets_with_hashtag, locations
