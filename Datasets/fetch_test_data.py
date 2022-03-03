import os
import numpy as np
import pandas as pd
from tqdm import tqdm

data_source = "../Twitter Scrape/data/"
output_path = "Testing/"
categories = ["bjp"]

for category in tqdm(categories):
    path = data_source + category + "/"
    files = os.listdir(path)
    query_df_map = {}
    for file in files:
        print(file)
        if file!=(".DS_Store"):
            query = file.split("2022")[0]
            if query[-1]=="_":
                query = query[:-1]
            df = pd.read_csv(path + file)
            # [TODO]: pre processing of parties
            if query not in query_df_map:
                query_df_map[query] = df
            else:
                query_df_map[query] = pd.concat([query_df_map[query],df])
        for query in query_df_map:
            query_df_map[query]["query"] = query
    df = pd.DataFrame()
    for query in query_df_map:
        df = pd.concat([df,query_df_map[query]])
    df.to_csv(output_path + category + ".csv",index=False)


