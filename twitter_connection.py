import tweepy as tw

# App keys
API_KEY = 'DTNhUzQ7EHUI9XHQZ9xuUrc2G'
API_SECRET = 'JShGSkczHzAMOAY5WZFk6vpSUETsm6XVkaWbaFDIdySTeIZJS5'
TOKEN_KEY = '1466436088105422863-H7TXzq461PEVPTDDP7a7FHsovrXz7y'
TOKEN_SECRET = '734ljvDU0Al2NW1WOwiR3NVndigHxRUuYRGcqeDbN06JF'


def connect_to_twitter():
    """
    Function to connect to the Twitter API with the api key and secret,
    token key and secret generated in the Twitter developer portal
    :return: api (the connection to the API)
    """
    auth = tw.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
    auth.secure = True
    api = tw.API(auth, wait_on_rate_limit=True)
    return api
