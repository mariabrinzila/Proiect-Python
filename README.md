# Python Project (name: Twitter, type: A, id: 2)
By: Brinzila Maria, 3B5

Table of Contents
=================
  * [Project description](#1-project-description)
  * [Twitter communication](#2-twitter-communication)
  * [Tweet search](#3-tweet-search)
  * [Map plotting](#4-map-plotting)
  * [Graphic user interface](#5-graphic-user-interface)
  * [Files included](#6-files-included) 

## 1. Project description
The project is designed to generate x amount of tweets with a certain hashtag and plot their locations on a map (the x number of tweets and the hashtag are given by the user).

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/description.png?raw=true) 

## 2. Twitter communication
In order to get the tweets with the hashtag specified by the user, I first needed to connect to the Twitter API. Thus, I created a Twitter account, signed up for a developer account, created a development app (Python-Project2022) with the type of account I had (Essential). 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/twitter_developer_account.png?raw=true) 
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/twitter_app.png?raw=true) 

After the app's creation, a few keys and tokens were created automatically (consumer key, consumer secret, bearer token, access token and secret), which are essentially the app's credentials without which I can't connect to the Twitter API. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/app_credentials.png?raw=true) 

Twitter has a bots and spam detection system that banned my app a few hours after its creation but after sending them an email and explaining why I need to use the API, they unbanned my app. Also, because I needed to search for the most recent tweets, I upgraded my account to Elevated by completing an online form (in order to have more access and privileges). 

To connect to Twitter in python, I used *tweepy*, used constants to store my app's credentials (API_KEY <=> consumer key, API_SECRET <=> consumer secret, TOKEN_KEY <=> access token key and TOKEN_SECRET <=> access token secret), performed the authentification process using the consumer key and secret, set the access token key and secret and connected to the API. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/app_credentials_python.png?raw=true) 
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/python_connection_to_twitter.png?raw=true) 

## 3. Tweet search
Given the hashtag that the tweets contain and the number of tweets from the user and after connecting to the Twitter API, I used the *search_30_day* function provided by the API, which searches for number tweets (given to the *maxResults* parameter) posted in the last 30 days with a certain hashtag (given to the *query* paramater). The result of this function is a list of tweets. In order to store the tweets and their locations, I created the Tweet class and the Location class: a Tweet object stores all the information for each tweet and a Location object stores the coordinates for each location).

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/tweet_class.png?raw=true) 
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/location_class.png?raw=true)

After generating the tweets, for each of them that had a location associated to it, I generated it's coordinates (latitude and longitude) with *Nominatim* from geopy.geocoders and if these coordinates exist (there could be tweets that have a location but for that particular location, the coordinates can't be generated), I put that certain tweet, its location and coordinates in a list.

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/print_tweet_location.png?raw=true) 
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/print_tweet_no_location.png?raw=true)

## 4. Map plotting
After generating the tweets and their locations and coordinates (for those that have a location and the coordinates can be generated), I plotted the map using *folium*. First I generated the coordinates for when the map first opens (for the *location* parameter) by calculating the mean for each coordinate: the latitude is the mean of all the latitudes I previously generated and longitude is the mean of the previously generated longitudes. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/map_initial_coordinates.png?raw=true)

For the map creation, I used the *cartodb positron* tiles so that the locations on the map are all in English, the zoom when one opens the map is 3 (the *zoom_start* parameter) and the maximum that one can zoom the map is 7 (the *max_zoom* parameter). 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/map_creation.png?raw=true)

After creating the map, I created the markers for the tweets that have locations and coordinates and for each marker, when one presses on it, the tweet's text pops up (the *popup* parameter). 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/map_markers.png?raw=true)

After creating the map and the markers, I saved the map in the *map.html* file and made sure that when the user presses the button to submit the hashtag and the number of tweets and after they are generated, the map opens automatically, without the user having to manually open the file (with the help of *webbrowser*). 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/map.png?raw=true)

## 5. Graphic user interface
The project's GUI is quite simple: the user is asked to input the hashtag they want the tweets to contain and the number of tweets. After the user inputs these 2 things and presses the *All done* button, their input is processed and troubleshot for errors. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/troubleshoot_hashtag.png?raw=true)
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/troubleshoot_number.png?raw=true)

The hashtag must contain the *#* on the first position and must not contain spaces and the number of tweets must be between 10 and 500. If the user doesn't comply to these guidelines, an error message box appears on the screen telling them what the guidelines are. The process of generating the tweets and plotting them on a map doesn't begin until the user's input is right according to these guidelines. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/hashtag_error_%23.png?raw=true)
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/hashtag_error_spaces.png?raw=true)
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/number_error.png?raw=true)

After the user's input complies to the guidelines, the tweets are generated and plotted on the map. The map is then automatically opened for the user to see. After that, the user can search another hashtag and/or number of tweets (there is no limit for how many searches the user can do) and after they are done searching and seeing the tweets plotted on the map, they can close the window or press the *Done searching* button. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/GUI.png?raw=true)
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/generate_output.png?raw=true)

The GUI was created with *tkinter* with a couple widgets (asking user for the hasthtag and number of tweets), entries (where the user writes the input) and buttons (*All done* and *Done searching*), all of which are organized in a grid. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/window.png?raw=true)
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/window_grid.png?raw=true)
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/get_hashtag.png?raw=true)
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/get_number.png?raw=true)

The buttons have action functions that perform the desired actions: *button_action_function* (calls the *submitted_input* function with the hashtag and number of tweets parameters that check if the input is compliant to the guidelines and if so, searches for the according tweets and plots them on the map) and *close_window*. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/buttons.png?raw=true)
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/button_functions.png?raw=true)

An important observation is that if the tweet search results in 0 tweets or if none of the generated tweets have loctions/coordinates, then an error message box appears on the screen letting the user know.

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/no_locations_error.png?raw=true)

## 6. Files included
  * *twitter_connection.py* <=> make the connection to the Twitter API
  * *search_tweets.py* <=> search in the Twitter database for tweets with a certain hashtag and a certain number of tweets that are given as parameters posted in the last 30 days
  * *plot_map.py* <=> calculate the mean of the coordinates of the locations in a list given as a parameter, create a map, create markers for the locations in the list given as a parameter and with the popup the tweet's text, print the tweets and their locations and coordinates, save map, open map
  * *get_input_generate_output.py* <=> take the user's input, troubleshoot for errors, generate the output by calling the functions from the previous files
  * *graphic_user_interface.py* <=> create the GUI in a class (the GraphicInterface class)
  * *main.py* <=> make a GraphicInterface object that opens the GUI
