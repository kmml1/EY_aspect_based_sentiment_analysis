import datetime
import calendar
from twython import Twython
import pandas as pd
import json
import credentials
import sentimentModel
import azureDBconnections


def min(s,low):
    if (low < s):
        return low         
    else: 
        return s

def refreshDB(i):
    CONSUMER_KEY= credentials.CONSUMER_KEY
    CONSUMER_SECRET= credentials.CONSUMER_SECRET
    python_tweets = Twython(CONSUMER_KEY, CONSUMER_SECRET)

    hashtags = ["kwarantanna", "vege", "IgaŚwiatek","hot16challange","fitness","krolowezycia","kryzys","ikea","łódź","haloween","kawa","radom","karmieniepiersia","pomidorowa","COVID19","nvidia","poniedziałek","biedronka"]
    my_date = datetime.date.today()
    my_date = my_date - datetime.timedelta(days=i)
    day = str(calendar.day_name[my_date.weekday()])[0:3]
    for hashtag in hashtags:
        azureDBconnections.create(hashtag)
    for hashtag in hashtags:

        lowest = None
        # Create our query
        query = {'q': '#'+hashtag,
                'count': 10,
                'lang': 'pl',
                'tweet_mode': 'extended',
                }
        # Search tweets
        
        lowest = None
        lowest_tmp = 1
        while (lowest != lowest_tmp):
            lowest_tmp = lowest
            query = {'q': '#'+ hashtag,
                    'lang': 'pl',
                    'tweet_mode': 'extended',
                    'max_id': lowest,
            }
            for status in python_tweets.search(**query)['statuses']:
            
                if (str(status['created_at'])[0:3] == day and status['id']!=lowest):
                    if 'retweeted_status' in status.keys():
                        s = status['full_text'].replace(",",";")
                    else:
                        s = status['full_text'].replace(",",";")
                        s = s.replace("'","")
                        tmp = sentimentModel.sentiment(s)
                        sentiment = 0
                        if (tmp < 0.5 ):
                            sentiment = -1
                        if (tmp > 0.5):
                            sentiment = 1
                        
                        azureDBconnections.insert(hashtag,s,status['created_at'],sentiment)
                    
                if lowest is None:
                    lowest =  status['id']
                else:
                    lowest = min(status['id'],lowest)
