import os
import pandas as pd
from tqdm import tqdm

#combine all json files in a folder into multiple json files
folder = "data/feb_scrape/bjp/"
file_bjp_up = "data/feb_scrape/bjp/bjp_up.json"
file_bjp_punjab = "data/feb_scrape/bjp/bjp_punjab.json"
file_bjp_rest = "data/feb_scrape/bjp/bjp_rest.json"

def combine(folder, fname):
    files = os.listdir(folder)
    combined = []
    for file in tqdm(files):
        try:
            df = pd.read_json(folder + file, lines=True)
            combined.append(df["renderedContent"])
        except:
            print(file)
    combined_df = pd.DataFrame({"content" : combined})
    combined_df.to_csv(fname, index=False)

combine("misc/", "misc.csv")