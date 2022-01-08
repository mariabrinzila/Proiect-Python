import search_tweets as st
import plot_map as pm
from tkinter import messagebox


def submitted_input(hashtag_variable, number_variable):
    """
    Function to take the input from the user, troubleshoot for errors,
    process it, when there no longer are any errors and call the function
    that generates number_variable.get() tweets with the hashtag
    hashtag_variable.get() after processing the input
    :param hashtag_variable: the variable that has the hashtag
    the user typed in
    :param number_variable: the variable that has the number of tweets
    the user typed in
    :return: void
    """
    hashtag = hashtag_variable.get()
    number = number_variable.get()
    error = False
    print("The user has chosen the hashtag " + str(hashtag) +
          ". The user has chosen the number of tweets " + str(number))

    # Troubleshoot for errors (hashtag)
    if hashtag[0] != '#':
        messagebox.showerror("Error:", "Sorry but the hashtag needs to start "
                                       "with the # character. Please try "
                                       "again!")
        error = True

    # Troubleshoot for errors (number)
    if number < 10 or number > 500:
        messagebox.showerror("Error:", "Sorry but the number of tweets has "
                                       "to be at least 10 and less than "
                                       "500. Please try again!")
        error = True

    if not error:
        generate_output(hashtag, number)


def generate_output(hashtag, number):
    """
    Function to search for the most recent number tweets with the
    hashtag given by the user and plot these tweets on a map
    :param hashtag: the hashtag inputted by the user
    :param number: the number of tweets inputted by the user
    :return: void
    """
    tweets, locations = st.generate_tweets_with_hashtag(hashtag, number)
    pm.print_tweets(tweets)
    print("Number of locations on the map: " + str(len(locations)))

    latitude, longitude = pm.generate_lat_long_locations(locations)
    print("Latitude: " + str(latitude) + " and longitude: " + str(longitude))
    pm.plot_map(latitude, longitude, tweets)
