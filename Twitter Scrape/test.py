import twint
import datetime
from datetime import date, timedelta
from tqdm import tqdm

# HYPERPARAMETERS
TRANSLATE_FLAG = False
TEMPORAL_FLAG = True
NUM_TWEETS = 40000

bjp_search_list = ["bjp","@BJP4India","@narendramodi","#BJPwinningUP","@AmitShah"]
bjp_search_list_2 = ["@myogiadityanath","yogi","@BJP4TamilNadu","@BJP4UP","@JPNadda","@CHARANJITCHANNI","channi"]
aap_search_list = ["aam aadmi party","#AAP","@AamAadmiParty","kejriwal","#ArvindKejriwal","@AAPPunjab","#KejriwalVsAll","@ArvindKejriwal","#AAPdePaap","@msisodia","@BhagwantMann"]
inc_search_list = ["@INCIndia","@RahulGandhi","Rahul Gandhi","@INCPunjab","@priyankagandhi","@INCUttarPradesh"]
general_search_list = ["#PunjabElections2022","#UPElections2022","#UttarPradeshElections2022"]
bsp_search_list = ["@Mayawati","@BSPIndia","bahujan samaj","mayawati","@AnandAkash_BSP","@satishmisrabsp"]
samajwadi_search_list = ["@yadavakhilesh","samajwadi","@samajwadiparty","shivpal yadav","#MulayamSinghYadav"]

def scrape_tweets_from_query(query,fname,since,until):
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

def process_date(date_prefix, num, flag):
    # Start (00:00:00)
    if flag == 0:
        if num<10:
            return date_prefix+"0"+str(num) + " 00:00:00"
        else:
            return date_prefix+str(num) + " 00:00:00"
    # End (23:59:59)
    else:
        if num<10:
            return date_prefix+"0"+str(num) + " 23:59:59"
        else:
            return date_prefix+str(num) + " 23:59:59"

if __name__ == "__main__":

    search_list = bjp_search_list + bjp_search_list_2 + aap_search_list + inc_search_list + general_search_list + bsp_search_list + samajwadi_search_list
    
    since = str("2022-02-")
    until = str("2022-02-")

    # # get all dates between start and end date
    # start = datetime.datetime.strptime(since, "%Y-%m-%d")
    # end = datetime.datetime.strptime(until, "%Y-%m-%d")
    # date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1)]


    for date in tqdm(range(1,19)):
        for query in tqdm(search_list):
            fname = "data/all/" + query + "_" + str(date) + ".csv"
            since_fin = process_date(since,date,0)
            until_fin = process_date(until,date+1,1)
            #print(query, ": ", since_fin, until_fin)
            scrape_tweets_from_query(query,fname,since_fin,until_fin)
