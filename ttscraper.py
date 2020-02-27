# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:57:59 2019

@author: Tainara
"""

from twitterscraper.query import query_tweets_from_user
import pandas as pd

class DadosTwitter:
    
    def colherdados(self, user, instagram):
        tweets = query_tweets_from_user(user, 1000)
        
        df = pd.DataFrame(t.__dict__ for t in tweets)
        dftweets = df.to_json(orient='records')
        
        file = open('perfis/'+instagram+'/twitter_'+user+'.json', 'w')
        file.write(dftweets)
        file.close()


    