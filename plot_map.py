import folium
from numpy import mean


def createMapMarkers(plotted_map, tweets):
    """
    Function to create map markers according to the locations of the tweets generated
    :param plotted_map: the map we want to plot
    :param tweets: list of Tweet objects containing all the tweets generated
    :return: void
    """
    for tweet in tweets:
        if tweet.location is not None and tweet.latitude != 0 and tweet.longitude != 0:
            folium.Marker(location=[tweet.latitude, tweet.longitude], popup=tweet.text).add_to(plotted_map)


def generateLatLongLocations(locations):
    """
    Function to generate the coordinates of the map we generate it with
    :param locations: list of Location objects containing the coordinates of each generated tweet's location,
    if its location is valid
    :return: latitude (mean of the locations' latitudes) and longitude (mean of the locations' longitudes)
    """
    latitude = mean([location.latitude for location in locations])
    longitude = mean([location.longitude for location in locations])

    return latitude, longitude


def printTweets(list_of_tweets):
    """
    Function to print all tweets generated (their text, location and coordinates)
    :param list_of_tweets: list of Tweet objects containing all the tweets generated
    :return: void
    """
    for t in list_of_tweets:
        print("Tweet text: " + str(t.text))
        print("Tweet location: " + str(t.location))
        print("Tweet coordinates: " + str(t.latitude) + " and " + str(t.longitude))
        print("----------------------------------------")


def plotMap(latitude, longitude, tweets):
    """
    Function to plot the generated tweets' locations on a map and save it in a html file
    :param latitude: latitude coordinate for the location attribute (when we make the map)
    :param longitude: longitude coordinate for the location attribute (when we make the map)
    :param tweets: list of Tweet objects containing all the tweets generated
    :return: void
    """
    # create map
    # location <=> latitude and longitude of the map
    # tiles <=> how the map looks
    plotted = folium.Map(location=[latitude, longitude], tiles='cartodb positron',
                         zoom_start=3, max_zoom=7)

    # put markers on the map (the locations of the tweets)
    createMapMarkers(plotted, tweets)
    plotted.save("map.html")
