import twint
import datetime
from datetime import date, timedelta

# HYPERPARAMETERS
TRANSLATE_FLAG = False
TEMPORAL_FLAG = True
NUM_TWEETS = 1000
since = str(datetime.datetime(2022, 2, 15))
until = str(datetime.datetime(2022, 2, 17))

search_list = ["aam aadmi party"]

def scrape_tweets_from_query(query,fname):
    config = twint.Config()
    config.Search = query
    if TRANSLATE_FLAG:
        config.Translate = True
        config.TranslateDest = "en"
    else:
        config.Lang = "en"
    config.Hide_output = True
    if TEMPORAL_FLAG:
        config.Since = since
        config.Until = until
    config.Limit = NUM_TWEETS
    config.Store_csv = True
    config.Output = fname
    twint.run.Search(config)

def scrape_tweets_from_user(username,fname):
    config = twint.Config()
    config.Username = username
    if TRANSLATE_FLAG:
        config.Translate = True
        config.TranslateDest = "en"
    # else:
    #     config.Lang = "en"
    config.Hide_output = True
    config.Limit = NUM_TWEETS
    if TEMPORAL_FLAG:
        config.Since = since
        config.Until = until
    config.Store_csv = True
    config.Output = fname
    twint.run.Search(config)



if __name__ == "__main__":
    for query in search_list:
        fname = "data/" + query + "_" + str(date.today()) + ".csv"
        scrape_tweets_from_query(query,fname)