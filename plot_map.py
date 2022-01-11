import folium
from numpy import mean
import webbrowser


def create_map_markers(plotted_map, tweets):
    """
    Function to create map markers according to the
    locations of the tweets generated
    :param plotted_map: the map we want to plot
    :param tweets: list of Tweet objects containing all the
    tweets generated
    :return: void
    """
    for tweet in tweets:
        if tweet.location is not None and tweet.latitude != 0 \
                and tweet.longitude != 0:
            folium.Marker(location=[tweet.latitude, tweet.longitude],
                          popup=tweet.text).add_to(plotted_map)


def generate_lat_long_locations(locations):
    """
    Function to generate the initial coordinates of the map we generate
    :param locations: list of Location objects containing the
    coordinates of each generated tweet's location,
    if its location is valid
    :return: latitude (mean of the locations' latitudes)
    and longitude (mean of the locations' longitudes)
    """
    latitude = mean([location.latitude for location in locations])
    longitude = mean([location.longitude for location in locations])

    return latitude, longitude


def print_tweets(list_of_tweets):
    """
    Function to print all tweets generated (their text, location and
    coordinates)
    :param list_of_tweets: list of Tweet objects containing all the
    tweets generated
    :return: void
    """
    for t in list_of_tweets:
        print("Tweet text: " + str(t.text))
        print("Tweet location: " + str(t.location))
        print("Tweet coordinates: " + str(t.latitude) + " and "
              + str(t.longitude))
        print("----------------------------------------")


def plot_map(latitude, longitude, tweets):
    """
    Function to plot the generated tweets' locations on a map,
    save it in a html file and open it in browser
    :param latitude: latitude coordinate for the location
    attribute (when we make the map)
    :param longitude: longitude coordinate for the location
    attribute (when we make the map)
    :param tweets: list of Tweet objects containing all the
    tweets generated
    :return: void
    """
    # Create map
    # Location <=> latitude and longitude of the map
    # Tiles <=> how the map looks
    plotted = folium.Map(location=[latitude, longitude],
                         tiles="cartodb positron",
                         zoom_start=3, max_zoom=7)

    # Put markers on the map (the locations of the tweets)
    create_map_markers(plotted, tweets)
    path = "map.html"
    plotted.save(path)

    # Open map in browser
    webbrowser.open(path)
