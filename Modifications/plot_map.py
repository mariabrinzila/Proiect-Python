import os
import time
from selenium import webdriver
import folium
from numpy import mean
from tkinter import Text, Scrollbar


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


def print_tweets(list_of_tweets, list_of_locations, window):
    """
    Function to print all tweets generated (their text, location and
    coordinates)
    :param window: main window
    :param list_of_locations: list of locations' coordinates
    :param list_of_tweets: list of Tweet objects containing all the
    tweets generated
    :return: void
    """
    # Generate tweet information and number of locations
    tweet_info = "Tweet info:"
    lines = [tweet_info]

    for t in list_of_tweets:
        tweet_info = "Tweet text: " + str(t.text)
        lines.append(tweet_info)
        tweet_info = "Tweet location: " + str(t.location)
        lines.append(tweet_info)
        tweet_info = "Tweet coordinates: " + str(t.latitude) + " and " \
                     + str(t.longitude)
        lines.append(tweet_info)
        tweet_info = "----------------------------------------"
        lines.append(tweet_info)

    nr_locations = "Number of locations on the map: " + str(len(list_of_locations))
    lines.append(nr_locations)

    # Text widget with scrollbar to show tweet information and number of locations
    text_widget = Text(window, width=50, height=20, wrap="none")
    vertical_scroll = Scrollbar(window, orient='vertical', command=text_widget.yview)
    horizontal_scroll = Scrollbar(window, orient='horizontal', command=text_widget.xview)
    text_widget['yscrollcommand'] = vertical_scroll.set
    text_widget['xscrollcommand'] = horizontal_scroll.set
    text_widget.insert('end', "\n".join(lines))

    # Add text widget and scrollbar in grid
    text_widget.grid(column=0, row=4, sticky='nwes', padx=2, pady=2)
    horizontal_scroll.grid(column=0, row=5, sticky='we')
    vertical_scroll.grid(column=1, row=4, sticky='nws')


def plot_map(latitude, longitude, tweets):
    """
    Function to plot the generated tweetsS locations on a map,
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
                         zoom_start=1, max_zoom=7)

    # Put markers on the map (the locations of the tweets)
    create_map_markers(plotted, tweets)
    path = "map.html"

    # Save map as html
    delay = 5
    tmpurl = 'file://{path}/{mapfile}'.format(path=os.getcwd(), mapfile=path)
    plotted.save(path)

    # Save map as png
    browser = webdriver.Chrome("F:\chromedriver.exe")
    browser.get(tmpurl)
    time.sleep(delay)
    browser.save_screenshot("map.png")
    browser.quit()
