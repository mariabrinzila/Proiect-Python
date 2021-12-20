import search_tweets as st
import plot_map as pm

tweets = st.generateTweetsWithHashtag("#covid19", 15)
pm.printTweets(tweets)

latitudes, longitudes = pm.locationsLongLat(tweets)
latitude, longitude = pm.generateLatLongLocations(latitudes, longitudes)
print("Number of locations on the map: " + str(len(latitudes)))
print("Latitude: " + str(latitude) + " and longitude: " + str(longitude))

pm.plotMap(latitudes, longitudes, latitude, longitude)
