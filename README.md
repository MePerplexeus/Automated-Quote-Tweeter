# Automated-Quote-Tweeter
Automate tweets by preloading set of tweets to post over a period of time.

## How to use
Since it posts one quote (or qweet) per execution, there are three ways you can make it work.

1. Run it mannually on your computer. Plain and simple, everyday.

2. Make a system to run this script at set intervals (I'll probably make it later and have it on my github profile here or you can try and find it for yourself elsewhere until then)

3. A much easier and better way to actually automate it, use [Python Anywhere](https://pythonanywhere.com/). 
    - Make an account over at [Python Anywhere](https://pythonanywhere.com/) (Free one can run only one script each day)
    - Upload the Automated Quote Tweeter to your Python Anywhere account
    - Go to Tasks tab and add the 'auto-qweet.py' file path to the Scheduled tasks and set the time(in UTC). 
    - That's it. Just make sure to renew task expiry post 28 days.
    
## Notes
This does require you to get [twitter API](https://developer.twitter.com/en/products/twitter-api) and set the 
<kbd>consumer_key = 'CONSUMER_KEY'</kbd>
<kbd>consumer_secret = 'CONSUMER_SECRET'</kbd>
<kbd>access_token = 'ACCESS_TOKEN'</kbd>
<kbd>access_secret = 'ACCESS_SECRET'</kbd>
