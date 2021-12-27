import search_tweets as st
import plot_map as pm
from tkinter import messagebox
import main as m


def submittedInput():
    hashtag = m.hashtag_variable.get()
    number = m.number_variable.get()
    error = False
    print("The user has chosen the hashtag " + str(hashtag) +
          ". The user has chosen the hashtag " + str(number))

    # troubleshooting for errors
    if hashtag[0] != '#':
        messagebox.showerror("Error:", "Sorry but the hashtag needs to start with the # character. "
                                       "Please try again!")
        error = True

    if number < 10 or number > 500:
        messagebox.showerror("Error:", "Sorry but the number of tweets has to be at least 10 and less "
                                       "than 500. Please try again!")
        error = True

    if not error:
        generateOutput(hashtag, number)


def generateOutput(hashtag, number):
    tweets, locations = st.generateTweetsWithHashtag(hashtag, number)
    pm.printTweets(tweets)
    print("Number of locations on the map: " + str(len(locations)))

    latitude, longitude = pm.generateLatLongLocations(locations)
    print("Latitude: " + str(latitude) + " and longitude: " + str(longitude))
    pm.plotMap(latitude, longitude, tweets)
