"""
Need to have snscrape installed 

pip install snscrape
"""

import os
from tqdm import tqdm

if not os.path.exists("data/all"):
    os.makedirs("data/all")

bjp_search_list = ["bjp","@BJP4India","@narendramodi","@AmitShah"]
bjp_search_list_2 = ["@JPNadda","@CHARANJITCHANNI","channi"]
aap_search_list = ["aam aadmi party","#AAP","@AamAadmiParty","kejriwal","#ArvindKejriwal","@AAPPunjab","#KejriwalVsAll","@ArvindKejriwal","#AAPdePaap","@msisodia","@BhagwantMann"]
inc_search_list = ["@INCIndia","@RahulGandhi","Rahul Gandhi","@INCPunjab","@priyankagandhi"]
general_search_list = ["#PunjabElections2022"]

date_prefix = "2022-02-"

all_list = bjp_search_list + bjp_search_list_2 + aap_search_list + inc_search_list + general_search_list
for i in tqdm(range(4,18)):
    start_date = date_prefix + str(i)
    end_date = date_prefix + str(i+1)
    for query in tqdm(all_list):
        os.system(f"snscrape --jsonl --max-results 1000 --since {start_date} twitter-search '{query} until:{end_date} lang:en' > data/all/{query}-tweets-{i}.json")