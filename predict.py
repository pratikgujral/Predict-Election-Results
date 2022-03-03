import numpy as np
import pandas as pd
from tqdm import tqdm
import time

polarity_donald = np.load("Datasets/Validation/US/hashtag_donaldtrump_polarity.npy")
subjectivity_donald = np.load("Datasets/Validation/US/hashtag_donaldtrump_subjectivity.npy")
bnb_donald = np.load("Datasets/Validation/US/hashtag_donaldtrump_sentiment_BNB.npy")

polarity_biden = np.load("Datasets/Validation/US/hashtag_joebiden_polarity.npy")
subjectivity_biden = np.load("Datasets/Validation/US/hashtag_joebiden_subjectivity.npy")
bnb_biden = np.load("Datasets/Validation/US/hashtag_joebiden_sentiment_BNB.npy")

df_donald = pd.read_csv("Datasets/Validation/US/hashtag_donaldtrump.csv",lineterminator='\n')
df_donald["vader"] = polarity_donald
df_donald["model"] = bnb_donald
df_donald["opinion"] = subjectivity_donald

df_biden = pd.read_csv("Datasets/Validation/US/hashtag_joebiden.csv",lineterminator='\n')
df_biden["vader"] = polarity_biden
df_biden["model"] = bnb_biden
df_biden["opinion"] = subjectivity_biden

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New York', 'New Mexico', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
stateCodes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
stateMapping = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 
                  'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NY': 'New York', 'NM': 'New Mexico', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT':  'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV':  'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}

#Filter to tweets only from US States
def filter(df_donald):

    df_donald['country']=df_donald['country'].replace({"United States of America" : "US", "United States" : "US"})
    df_donald = df_donald.loc[df_donald['country'] == "US"] 
    df_filtered = df_donald
    print(len(df_donald.index))
    print(len(df_filtered.index))
    print(df_donald.iterrows())
    i = 0
    
    # loop = tqdm(len(df_donald.index),leave=True)
    for index, row in df_donald.iterrows():
        i+=1
        flag = 0
        t1 = time.time()
        if row.state in states:
            flag = 2
            t2 = time.time()
            print(t2-t1)
            print("state")
        elif row.state_code in stateCodes:
            row['state'] = stateMapping[row.state_code]
            flag = 1
            t2 = time.time()
            print(t2-t1)
            print("state code")
        elif (isinstance(row.user_location,float)==False):
            words = row.user_location.split(',')
            for word in words:
                check = word.strip()
                if check in states:
                    row['state'] = check
                    flag = 1
                    break
                elif check in stateCodes:
                    row['state'] = stateMapping[check]
                    flag = 1
                    break
            t2 = time.time()
            print(t2-t1)
            print("location")
        if (flag==1):
            df_filtered.loc[index, 'state'] = row['state']
            print(row['state'])
            t2 = time.time()
            print(t2-t1)
            print("update state")
        elif (flag == 0):
            df_filtered = df_filtered.drop(index = index)
            print(row.country)
            t2 = time.time()
            print(t2-t1)
            print("drop")
        # loop.update(1)
        print(i)


    return df_filtered

if __name__ == "__main__":

    df_donald = filter(df_donald)
    print("Donald Done")
    df_biden = filter(df_biden)
    print("Biden Done")

    df_donald.to_csv("Datasets/Validation/US/hashtag_donaldtrump_filtered.csv")
    df_biden.to_csv("Datasets/Validation/US/hashtag_joebiden_filtered.csv")