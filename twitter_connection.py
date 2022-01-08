import tweepy as tw

# App keys
api_key = 'DTNhUzQ7EHUI9XHQZ9xuUrc2G'
api_secret = 'JShGSkczHzAMOAY5WZFk6vpSUETsm6XVkaWbaFDIdySTeIZJS5'
token_key = '1466436088105422863-H7TXzq461PEVPTDDP7a7FHsovrXz7y'
token_secret = '734ljvDU0Al2NW1WOwiR3NVndigHxRUuYRGcqeDbN06JF'


def connect_to_twitter():
    """
    Function to connect to the Twitter API with the api key and secret,
    token key and secret generated in the Twitter developer portal
    :return: api (the connection to the API)
    """
    auth = tw.OAuthHandler(api_key, api_secret)
    auth.set_access_token(token_key, token_secret)
    auth.secure = True
    api = tw.API(auth, wait_on_rate_limit=True)
    return api
