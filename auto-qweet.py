# Tweeter

import tweepy

class Bot:
    def __init__(self, keys):
        self._consumer_key = keys[0]
        self._consumer_secret = keys[1]
        self._access_token = keys[2]
        self._access_secret = keys[3]

        try:
            auth = tweepy.OAuthHandler(self._consumer_key,
                                       self._consumer_secret)
            auth.set_access_token(self._access_token, self._access_secret)

            self.client = tweepy.API(auth)
            if not self.client.verify_credentials():
                raise tweepy.TweepError
        except tweepy.TweepError as e:
            print('ERROR : connection failed. Check your OAuth keys.')
        else:
            print('Connected as @{}, you can start to tweet !'.format(self.client.me().screen_name))
            self.client_id = self.client.me().id

    def get_last_tweet(self):
        tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
        print(tweet.text)
        return tweet

    def tweet(self, status):
        try:
            tweet = self.client.update_status(status)
            return tweet
        except:
            print('Tweet Update Unsuccessfull..')

def quote_of_the_day():
    try:
        with open("quotes.txt", "r") as f:
            quotes = f.readlines()
            todays_quote = quotes[0].strip('\n')
            print('todays quote is\n'+todays_quote)

        with open("quotes.txt", "w") as f:
            for quote in quotes:
                if quote != quotes[0]:
                    f.write(quote)
        return todays_quote
    except:
        print('Out of Qweets')

tweetThis = quote_of_the_day()

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'

perplexeus_bot = Bot([consumer_key, consumer_secret, access_token, access_secret])

perplexeus_bot.tweet(tweetThis)
