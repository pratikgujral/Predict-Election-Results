import os
import pandas as pd
from tqdm import tqdm

#combine all json files in a folder
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