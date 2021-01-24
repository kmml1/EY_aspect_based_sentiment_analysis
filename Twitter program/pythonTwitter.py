# Import the Twython class
from twython import Twython
import pandas as pd
import json
import credentials

CONSUMER_KEY= "cFaUmZoT5TCHEplyb99WfGYmP"
CONSUMER_SECRET= "I8tSyQv4g9HoEdkpZndsiRfVkmc6mjpLNLR9YHnBwraWG1WPk8"

def min(s,low):
    if (low < s):
        return low         
    else: 
        return s
# Instantiate an object
python_tweets = Twython(CONSUMER_KEY, CONSUMER_SECRET)

hashtags = ["kwarantanna", "vege", "IgaŚwiatek","hot16challange","fitness","krolowezycia","kryzys","ikea","łódź","haloween","kawa","radom","karmieniepiersia","pomidorowa","COVID19","nvidia","poniedziałek","biedronka"]

for hashtag in hashtags:

    lowest = None
    # Create our query
    query = {'q': '#'+hashtag,
            'count': 10,
            'lang': 'pl',
            'tweet_mode': 'extended',
            }
    # Search tweets
    dict_ = { 'date': [], 'text': []}
    for status in python_tweets.search(**query)['statuses']:
    
        dict_['date'].append(status['created_at'])

        if 'retweeted_status' in status.keys():
            s = status['retweeted_status']['full_text'].replace(",",";")
        else:
            s = status['full_text'].replace(",",";")

        dict_['text'].append(s)
        if lowest is None:
            lowest =  status['id']
        else:
            lowest = min(status['id'],lowest)
        lowest_tmp = None
        while (lowest != lowest_tmp):
            lowest_tmp = lowest
            query = {'q': '#'+hashtag,
                    'count': 100,
                    'lang': 'pl',
                    'tweet_mode': 'extended',
                    'max_id': lowest,
            }
            for status in python_tweets.search(**query)['statuses']:
            
                dict_['date'].append(status['created_at'])

                if 'retweeted_status' in status.keys():
                    s = status['retweeted_status']['full_text'].replace(",",";")
                else:
                    s = status['full_text'].replace(",",";")

                dict_['text'].append(s)
                if lowest is None:
                    lowest =  status['id']
                else:
                    lowest = min(status['id'],lowest)

    df = pd.DataFrame(dict_)
    df.to_csv('saved_tweets_'+hashtag +'.csv') 
    #df.sort_values(by='favorite_count', inplace=True, ascending=False)


