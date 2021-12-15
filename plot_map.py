import search_tweets as st
import folium
from geopy.geocoders import Nominatim


def createMapMarkers(plotted_map, data):
    geo_locator = Nominatim(user_agent="Project")

    for tweet in data:
        location = tweet.location
        text = tweet.text
        if location is not None:
            # generate latitude and longitude for the given location
            geolocation = geo_locator.geocode(location)

            if geolocation is not None:
                folium.Marker(location=[geolocation.latitude, geolocation.longitude],
                              popup=text).add_to(plotted_map)


def printTweets(list_of_tweets):
    for t in list_of_tweets:
        print("Tweet text: " + str(t.text))
        print("Tweet location: " + str(t.location))
        print("----------------------------------------")


def plotMap(hashtag, number):
    tweets = st.generateTweetsWithHashtag(hashtag, number)
    printTweets(tweets)

    # create map
    plotted = folium.Map(location=[0, 0], zoom_start=3)

    # put markers on the map (the locations of the tweets)
    createMapMarkers(plotted, tweets)
    plotted.save("map.html")
