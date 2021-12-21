import folium
from numpy import mean


def createMapMarkers(plotted_map, tweets):
    for tweet in tweets:
        if tweet.location is not None and tweet.latitude != 0 and tweet.longitude != 0:
            folium.Marker(location=[tweet.latitude, tweet.longitude], popup=tweet.text).add_to(plotted_map)


def generateLatLongLocations(locations):
    latitude = mean([location.latitude for location in locations])
    longitude = mean([location.longitude for location in locations])

    return latitude, longitude


def printTweets(list_of_tweets):
    for t in list_of_tweets:
        print("Tweet text: " + str(t.text))
        print("Tweet location: " + str(t.location))
        print("Tweet coordinates: " + str(t.latitude) + " and " + str(t.longitude))
        print("----------------------------------------")


def plotMap(latitude, longitude, tweets):
    # create map
    # location <=> latitude and longitude of the map
    # tiles <=> how the map looks
    plotted = folium.Map(location=[latitude, longitude], tiles='cartodb positron',
                         zoom_start=3, max_zoom=7)

    # put markers on the map (the locations of the tweets)
    createMapMarkers(plotted, tweets)
    plotted.save("map.html")
