import search_tweets as st
import plot_map as pm

tweets, locations = st.generateTweetsWithHashtag("#covid19", 30)
pm.printTweets(tweets)
print("Number of locations on the map: " + str(len(locations)))

latitude, longitude = pm.generateLatLongLocations(locations)
print("Latitude: " + str(latitude) + " and longitude: " + str(longitude))
pm.plotMap(latitude, longitude, tweets)
