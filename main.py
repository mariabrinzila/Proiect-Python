import search_tweets as st

for t in st.tweets_with_hashtag:
    print("Tweet text:")
    print(t.text)
    print("Tweet location: " + str(t.location))
    print("----------------------------------------")
