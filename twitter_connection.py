import tweepy as tw

# app keys
consumer_key = 'DTNhUzQ7EHUI9XHQZ9xuUrc2G'
consumer_secret = 'JShGSkczHzAMOAY5WZFk6vpSUETsm6XVkaWbaFDIdySTeIZJS5'
access_token = '1466436088105422863-H7TXzq461PEVPTDDP7a7FHsovrXz7y'
access_token_secret = '734ljvDU0Al2NW1WOwiR3NVndigHxRUuYRGcqeDbN06JF'

# connecting to Twitter, using the Twitter tweepy API
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tw.API(auth, wait_on_rate_limit=True)
