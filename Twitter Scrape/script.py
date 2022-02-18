import twint
import datetime
from datetime import date, timedelta

# HYPERPARAMETERS
TRANSLATE_FLAG = False
TEMPORAL_FLAG = False
NUM_TWEETS = 1000
since = str(datetime.datetime(2022, 2, 4))
until = str(datetime.datetime(2022, 2, 5))


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
    else:
        config.Lang = "en"
    config.Hide_output = True
    config.Limit = NUM_TWEETS
    if TEMPORAL_FLAG:
        config.Since = since
        config.Until = until
    config.Store_csv = True
    config.Output = fname
    twint.run.Search(config)

def scrape_replies_on_tweet(tweet_id,fname):
    config = twint.Config()
    config.Tweet_id = tweet_id
    if TRANSLATE_FLAG:
        config.Translate = True
        config.TranslateDest = "en"
    else:
        config.Lang = "en"
    config.Get_replies = True
    config.Store_csv = True
    config.Output = fname
    twint.run.Search(config)


if __name__ == "__main__":
    #scrape_tweets_from_query("covid", "tweets_covid19.csv")
    #scrape_tweets_from_user("AmitShah", "tweets_amit.csv")
    #scrape_replies_on_tweet("1489956615902343177", "tweets_replies.csv")
    scrape_tweets_from_query("aam aadmi party", "tweets_aam_aadmi.csv")