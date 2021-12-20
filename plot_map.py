import folium
from geopy.geocoders import Nominatim
from numpy import mean


def locationsLongLat(data):
    geo_locator = Nominatim(user_agent="Project")
    latitudes = []
    longitudes = []

    for tweet in data:
        location = tweet.location

        if location is not None:
            # generate latitude and longitude for the given location
            geolocation = geo_locator.geocode(location)

            if geolocation is not None:
                latitudes.append(geolocation.latitude)
                longitudes.append(geolocation.longitude)

    return latitudes, longitudes


def createMapMarkers(plotted_map, latitude, longitude):
    lg = len(longitude)

    for i in range(lg):
        folium.Marker(location=[latitude[i], longitude[i]]).add_to(plotted_map)


def generateLatLongLocations(lat, long):
    latitude = mean(lat)
    longitude = mean(long)

    return latitude, longitude


def printTweets(list_of_tweets):
    for t in list_of_tweets:
        print("Tweet text: " + str(t.text))
        print("Tweet location: " + str(t.location))
        print("----------------------------------------")


def plotMap(latitudes, longitudes, latitude, longitude):
    # create map
    # location <=> latitude and longitude of the map
    # tiles <=> how the map looks
    plotted = folium.Map(location=[latitude, longitude], tiles='cartodb positron',
                         zoom_start=3, max_zoom=7)

    # put markers on the map (the locations of the tweets)
    createMapMarkers(plotted, latitudes, longitudes)
    plotted.save("map.html")
