import numpy as np
import pandas as pd
from tqdm import tqdm
import time

def update_df(df_donald,name,vader_df,trained_df,op_vader,op_trained):
    
    loop = tqdm(total = len(df_donald.index))
    if (name == "Trump"):
        
        for index, row in df_donald.iterrows():
            # update vader count (!Idea1)
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
                vader_df.at[row.state,'Trump Total count'] += 1
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
                op_vader.at[row.state,'Trump Total count'] += 1
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
            loop.update(1)
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
                vader_df.at[row.state,'Biden Total count'] += 1
            

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
                op_vader.at[row.state,'Biden Total count'] += 1

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

if __name__ == "__main__":
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New York', 'New Mexico', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
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
        'Biden Negative Sum',
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
            'Biden Negative Sum',
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
            'Biden Negative Sum',
            'Biden Total Sum'])


    tweets_location_plan1 = tweets_location_plan1.fillna(0)
    tweets_location_plan2= tweets_location_plan2.fillna(0)
    tweets_location_plan3 = tweets_location_plan3.fillna(0)
    tweets_location_plan4 = tweets_location_plan4.fillna(0)
    print("Updating Trump")
    tweets_location_plan1, tweets_location_plan2, tweets_location_plan3, tweets_location_plan4 =update_df(df_donald,"Trump",tweets_location_plan1, tweets_location_plan2, tweets_location_plan3, tweets_location_plan4)
    print("Updating Biden")
    tweets_location_plan1, tweets_location_plan2, tweets_location_plan3, tweets_location_plan4 =update_df(df_biden,"Biden",tweets_location_plan1, tweets_location_plan2, tweets_location_plan3, tweets_location_plan4)

    tweets_location_plan1.to_csv("Datasets/Validation/US/statewise_total_idea1.csv")
    tweets_location_plan2.to_csv("Datasets/Validation/US/statewise_total_idea2.csv")
    tweets_location_plan3.to_csv("Datasets/Validation/US/statewise_total_idea3.csv")
    tweets_location_plan4.to_csv("Datasets/Validation/US/statewise_total_idea4.csv")