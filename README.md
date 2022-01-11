# Proiect Python (Twitter, tip: A, id: 2)
By: Brinzila Maria, 3B5

Table of Contents
=================
  * [Project Description](#1-project-description)
  * [Twitter Communication](#2-twitter-communication)
  * [Tweet search](#3-tweet-search)
  * [Map plotting](#4-map-plotting)
  * [Graphic User Interface](#5-graphic-user-interface)
  * [Files Included](#6-files-included) 

## 1. Project Description
The project is designed to generate x amount of tweets with a certain hashtag and plot their locations on a map (the x number of tweets and the hashtag are given by the user).

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/description.png?raw=true) 

## 2. Twitter Communication
In order to get the tweets with the hashtag specified by the user, I first needed to connect to the Twitter API. Thus, I created a Twitter account, signed up for a developer account, created a development app (Python-Project2022) with the type of account I had (Essential). 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/twitter_developer_account.png?raw=true) 
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/twitter_app.png?raw=true) 

After the app's creation, a few keys and tokens were created automatically (consumer key, consumer secret, bearer token, access token and secret), which are essentially the app's credentials without which I can't connect to the Twitter API. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/app_credentials.png?raw=true) 

Twitter has a bots and spam detection system that banned my app a few hours after its creation but after sending them an email and explaining why I need to use the API, they unbanned my app. Also, because I needed to search for the most recent tweets, I upgraded my account to Elevated by completing an online form (in order to have more access and privileges). <br/> <br/>

To connect to Twitter in python, I used *tweepy*, used constants to store my app's credentials (API_KEY <=> consumer key, API_SECRET <=> consumer secret, TOKEN_KEY <=> access token key and TOKEN_SECRET <=> access token secret), performed the authentification process using the consumer key and secret, set the access token key and secret and connected to the API. 

![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/app_credentials_python.png?raw=true) 
![alt text](https://github.com/mariabrinzila/Proiect-Python/blob/main/README_photos/python_connection_to_twitter.png?raw=true) 


