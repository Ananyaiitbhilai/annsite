

import os
import tweepy 
import configparser
import pandas as pd
    consumer_key='uxIhmpOUkeeMYrRhVstivIkne'
    consumer_secret='bQ6w3mkKHfo0fNISOJVZpJxDfFv5VLfgdhsAkhRW17689Skqsd'
    access_token='1366592995944898562-XGRWIlU6JaFUpMpVxlIogug7g1CmUE'
    access_token_secret='3QXzoKiNCwvNk94cn7uM805Degfa7P6qYGFllMP8RGgjw'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    tweets=tweepy.Cursor(api.search,
                tweet=inp,
                lang="en",
                rpp=100, count=20,
                )
    tweets
    tweet_details=[[tweet.geo,tweet.text,tweet.user.screen_name,tweet.user.location]for tweet in tweets]
    tweet_df=pd.DataFrame(data=tweet_details, columns=['geo','text','user',"location"])
    pd.set_option('max_colwidth', 800)
output="hello"%(sys.argv[1],tweet_df.head(20))
    print(output)