import numpy as np
import pandas as pd
from tqdm import tqdm
import time

# polarity_donald = np.load("Datasets/Validation/US/hashtag_donaldtrump_polarity.npy")
# subjectivity_donald = np.load("Datasets/Validation/US/hashtag_donaldtrump_subjectivity.npy")
# bnb_donald = np.load("Datasets/Validation/US/hashtag_donaldtrump_sentiment_BNB.npy")

# polarity_biden = np.load("Datasets/Validation/US/hashtag_joebiden_polarity.npy")
# subjectivity_biden = np.load("Datasets/Validation/US/hashtag_joebiden_subjectivity.npy")
# bnb_biden = np.load("Datasets/Validation/US/hashtag_joebiden_sentiment_BNB.npy")

# df_donald = pd.read_csv("Datasets/Validation/US/hashtag_donaldtrump.csv",lineterminator='\n')
# df_donald["vader"] = polarity_donald
# df_donald["model"] = bnb_donald
# df_donald["opinion"] = subjectivity_donald

# df_biden = pd.read_csv("Datasets/Validation/US/hashtag_joebiden.csv",lineterminator='\n')
# df_biden["vader"] = polarity_biden
# df_biden["model"] = bnb_biden
# df_biden["opinion"] = subjectivity_biden

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New York', 'New Mexico', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
stateCodes = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
stateMapping = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 
                  'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NY': 'New York', 'NM': 'New Mexico', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT':  'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV':  'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}


def update_df(df_donald,name,vader_df,trained_df,op_vader,op_trained):
    
    loop = tqdm(len(df_donald.index))
    if (name == "Trump"):
        
        for index, row in tqdm(df_donald.iterrows()):
            # update vader count (!Idea1)
            
            start = time.time()
            if (row.vader>0):

                vader_df.at[row.state, 'Trump Positive Sum'] += row.vader
                vader_df.at[row.state,'Trump Total Sum'] += row.vader
                vader_df.at[row.state,'Trump Positive count'] += 1
                vader_df.at[row.state,'Trump Total count'] += 1
                # end = time.time()
                # print(end-start)
                # print("update vader+")
            elif (row.vader<0):
                vader_df.at[row.state,'Trump Negative Sum'] += row.vader
                vader_df.at[row.state,'Trump Total Sum'] += row.vader
                vader_df.at[row.state,'Trump Negative count'] += 1
                vader_df.at[row.state,'Trump Total count'] += 1
                # end = time.time()
                # print(end-start)
                # print("update vader-")
            else:
                vader_df.at[row.state,'Trump Neutral count'] += 1
                # end = time.time()
                # print(end-start)
                # print("update vader=")

            start = time.time()
            # update trained count (!Idea2)
            if (row.model>0):
                
                trained_df.at[row.state,'Trump Positive count'] += 1
                trained_df.at[row.state,'Trump Total count'] += 1
                # end = time.time()
                # print(end-start)
                # print("update trained+")
                
            else:
                trained_df.at[row.state,'Trump Negative count'] += 1
                trained_df.at[row.state,'Trump Total count'] += 1
                # end = time.time()
                # print(end-start)
                # print("update trained-")

            start = time.time()
            # update weighted count (!Idea3)
            if (row.vader>0):
                op_vader.at[row.state,'Trump Positive Sum'] += row.vader*row.opinion
                op_vader.at[row.state,'Trump Total Sum'] += row.vader*row.opinion
                op_vader.at[row.state,'Trump Positive count'] += 1
                op_vader.at[row.state,'Trump Total count'] += 1
                # end = time.time()
                # print(end-start)
                # print("vader weight+")
            elif (row.vader<0):
                op_vader.at[row.state,'Trump Negative Sum'] += row.vader*row.opinion
                op_vader.at[row.state,'Trump Total Sum'] += row.vader*row.opinion
                op_vader.at[row.state,'Trump Negative count'] += 1
                op_vader.at[row.state,'Trump Total count'] += 1
                # end = time.time()
                # print(end-start)
                # print("vader weight-")
            else:
                op_vader.at[row.state,'Trump Neutral count'] += 1
                # end = time.time()
                # print(end-start)
                # print("vader weight=")

            start = time.time()
            # update weighted count (!Idea4)
            if (row.model>0):
                op_trained.at[row.state,'Trump Positive Sum'] += row.vader*row.opinion
                op_trained.at[row.state,'Trump Total Sum'] += row.vader*row.opinion
                op_trained.at[row.state,'Trump Positive count'] += 1
                op_trained.at[row.state,'Trump Total count'] += 1
                # end = time.time()
                # print(end-start)
                # print("trained weight+")
            else:
                op_trained.at[row.state,'Trump Negative Sum'] += row.vader*row.opinion
                op_trained.at[row.state,'Trump Total Sum'] += row.vader*row.opinion
                op_trained.at[row.state,'Trump Negative count'] += 1
                op_trained.at[row.state,'Trump Total count'] += 1
                # end = time.time()
                # print(end-start)
                # print("trained weight-")
    
    elif (name == "Biden"):
        for index, row in df_donald.iterrows():
            # update vader count (!Idea1)
            if (row.vader>0):
                vader_df.at[row.state, 'Biden Positive Sum'] += row.vader
                vader_df.at[row.state,'Biden Total Sum'] += row.vader
                vader_df.at[row.state,'Biden Positive count'] += 1
                vader_df.at[row.state,'Biden Total count'] += 1
            elif (row.vader<0):
                vader_df.at[row.state,'Biden Negative Sum'] += row.vader
                vader_df.at[row.state,'Biden Total Sum'] += row.vader
                vader_df.at[row.state,'Biden Negative count'] += 1
                vader_df.at[row.state,'Biden Total count'] += 1
            else:
                vader_df.at[row.state,'Biden Neutral count'] += 1
            

            # update trained count (!Idea2)
            if (row.model>0):
                trained_df.at[row.state,'Biden Positive count'] += 1
                trained_df.at[row.state,'Biden Total count'] += 1
                
            else:
                trained_df.at[row.state,'Biden Negative count'] += 1
                trained_df.at[row.state,'Biden Total count'] += 1

            # update weighted count (!Idea3)
            if (row.vader>0):
                op_vader.at[row.state,'Biden Positive Sum'] += row.vader*row.opinion
                op_vader.at[row.state,'Biden Total Sum'] += row.vader*row.opinion
                op_vader.at[row.state,'Biden Positive count'] += 1
                op_vader.at[row.state,'Biden Total count'] += 1
            elif (row.vader<0):
                op_vader.at[row.state,'Biden Negative Sum'] += row.vader*row.opinion
                op_vader.at[row.state,'Biden Total Sum'] += row.vader*row.opinion
                op_vader.at[row.state,'Biden Negative count'] += 1
                op_vader.at[row.state,'Biden Total count'] += 1
            else:
                op_vader.at[row.state,'Biden Neutral count'] += 1

            # update weighted count (!Idea4)
            if (row.model>0):
                op_trained.at[row.state,'Biden Positive Sum'] += row.vader*row.opinion
                op_trained.at[row.state,'Biden Total Sum'] += row.vader*row.opinion
                op_trained.at[row.state,'Biden Positive count'] += 1
                op_trained.at[row.state,'Biden Total count'] += 1
            else:
                op_trained.at[row.state,'Biden Negative Sum'] += row.vader*row.opinion
                op_trained.at[row.state,'Biden Total Sum'] += row.vader*row.opinion
                op_trained.at[row.state,'Biden Negative count'] += 1
                
                op_trained.at[row.state,'Biden Total count'] += 1
        loop.update(1)
    
    return (vader_df,trained_df,op_vader,op_trained)
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

    # df_donald = filter(df_donald)
    # print("Donald Done")
    # df_donald.to_csv("Datasets/Validation/US/hashtag_donaldtrump_filtered.csv")
    
    # df_biden = filter(df_biden)
    # print("Biden Done")
    # df_biden.to_csv("Datasets/Validation/US/hashtag_joebiden_filtered.csv")


    df_donald = pd.read_csv("Datasets/Validation/US/hashtag_donaldtrump_filtered.csv",lineterminator='\n')
    df_biden = pd.read_csv("Datasets/Validation/US/hashtag_joebiden_filtered.csv",lineterminator='\n')

    tweets_location_plan1 = pd.DataFrame(index = [state for state in states],columns=
        ['Trump Positive count',
        'Trump Negative count',
        'Trump Neutral count',
        'Trump Total count',
        'Biden Positive count',
        'Biden Negative count',
        'Biden Neutral count',
        'Biden Total count',
        
        'Trump Positive Sum',
        'Trump Negative Sum',
        'Trump Total Sum',
        'Biden Positive Sum',
        'Biden Neutral count',
        'Biden Total Sum'])

    tweets_location_plan2 = pd.DataFrame(index = [state for state in states],columns=
            ['Trump Positive count',
            'Trump Negative count',
            'Trump Neutral count',
            'Trump Total count',
            'Biden Positive count',
            'Biden Negative count',
            'Biden Neutral count',
            'Biden Total count'])

    tweets_location_plan3 = pd.DataFrame(index = [state for state in states],columns=
            ['Trump Positive count',
            'Trump Negative count',
            'Trump Neutral count',
            'Trump Total count',
            'Biden Positive count',
            'Biden Negative count',
            'Biden Neutral count',
            'Biden Total count',
            
            'Trump Positive Sum',
            'Trump Negative Sum',
            'Trump Total Sum',
            'Biden Positive Sum',
            'Biden Neutral count',
            'Biden Total Sum'])

    tweets_location_plan4 = pd.DataFrame(index = [state for state in states],columns=
            ['Trump Positive count',
            'Trump Negative count',
            'Trump Neutral count',
            'Trump Total count',
            'Biden Positive count',
            'Biden Negative count',
            'Biden Neutral count',
            'Biden Total count',
            
            'Trump Positive Sum',
            'Trump Negative Sum',
            'Trump Total Sum',
            'Biden Positive Sum',
            'Biden Neutral count',
            'Biden Total Sum'])


    tweets_location_plan1 = tweets_location_plan1.fillna(0)
    tweets_location_plan2= tweets_location_plan2.fillna(0)
    tweets_location_plan3 = tweets_location_plan3.fillna(0)
    tweets_location_plan4 = tweets_location_plan4.fillna(0)
    print("Updating Trump")
    tweets_location_plan1, tweets_location_plan2, tweets_location_plan3, tweets_location_plan4 =update_df(df_donald,"Trump",tweets_location_plan1, tweets_location_plan2, tweets_location_plan3, tweets_location_plan4)
    print("Updating Biden")
    tweets_location_plan1, tweets_location_plan2, tweets_location_plan3, tweets_location_plan4 =update_df(df_donald,"Trump",tweets_location_plan1, tweets_location_plan2, tweets_location_plan3, tweets_location_plan4)

    tweets_location_plan1.to_csv("Datasets/Validation/US/statewise_total_idea1.csv")
    tweets_location_plan2.to_csv("Datasets/Validation/US/statewise_total_idea2.csv")
    tweets_location_plan3.to_csv("Datasets/Validation/US/statewise_total_idea3.csv")
    tweets_location_plan4.to_csv("Datasets/Validation/US/statewise_total_idea4.csv")
        
    