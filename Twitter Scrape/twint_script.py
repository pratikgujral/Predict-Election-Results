import twint
import datetime
from datetime import date, timedelta
from tqdm import tqdm

# HYPERPARAMETERS
TRANSLATE_FLAG = False
TEMPORAL_FLAG = True
NUM_TWEETS = 20000
since = str(date.today() - timedelta(days=1))
until = str(date.today())

bjp_search_list = ["bjp","@BJP4India","@narendramodi","#BJPwinningUP","@AmitShah"]
bjp_search_list_2 = ["@myogiadityanath","yogi","@BJP4TamilNadu","@BJP4UP","@JPNadda","@CHARANJITCHANNI","channi"]
aap_search_list = ["aam aadmi party","#AAP","@AamAadmiParty","kejriwal","#ArvindKejriwal","@AAPPunjab","#KejriwalVsAll","@ArvindKejriwal","#AAPdePaap","@msisodia","@BhagwantMann"]
inc_search_list = ["@INCIndia","@RahulGandhi","Rahul Gandhi","@INCPunjab","@priyankagandhi","@INCUttarPradesh"]
general_search_list = ["#PunjabElections2022","#UPElections2022","#UttarPradeshElections2022"]
bsp_search_list = ["@Mayawati","@BSPIndia","bahujan samaj","mayawati","@AnandAkash_BSP","@satishmisrabsp"]
samajwadi_search_list = ["@yadavakhilesh","samajwadi","@samajwadiparty","shivpal yadav","#MulayamSinghYadav"]

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
    config.Translate = True
    config.TranslateDest = "en"
    config.Hide_output = True
    config.Limit = NUM_TWEETS
    if TEMPORAL_FLAG:
        config.Since = since
        config.Until = until
    config.Store_csv = True
    config.Output = fname
    twint.run.Search(config)



if __name__ == "__main__":

    for query in tqdm(bjp_search_list):
        print(query)
        fname = "data/bjp/" + query + "_" + str(date.today()) + ".csv"
        scrape_tweets_from_query(query,fname)
    # for query in tqdm(general_search_list):
    #     fname = "data/general/" + query + "_" + str(date.today()) + ".csv"
    #     scrape_tweets_from_query(query,fname)
    # for query in tqdm(bsp_search_list):
    #     fname = "data/bsp/" + query + "_" + str(date.today()) + ".csv"
    #     scrape_tweets_from_query(query,fname)
    # for query in tqdm(samajwadi_search_list):
    #     fname = "data/samajwadi/" + query + "_" + str(date.today()) + ".csv"
    #     scrape_tweets_from_query(query,fname)
    # for query in tqdm(bjp_search_list_2):
    #     fname = "data/bjp/" + query + "_" + str(date.today()) + ".csv"
    #     scrape_tweets_from_query(query,fname)


    # for query in aap_search_list:
    #     fname = "data/aap/" + query + "_" + str(date.today()) + ".csv"
    #     scrape_tweets_from_query(query,fname)
    # for query in bjp_search_list:
    #     fname = "data/bjp/" + query + "_" + str(date.today()) + ".csv"
    #     scrape_tweets_from_query(query,fname)
