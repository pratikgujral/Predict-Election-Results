import numpy as np
import pandas as pd
from tqdm import tqdm
import time



def update_df(df,name,vader_df,trained_df,op_vader,op_trained):
    
    # loop = tqdm(total = len(df_donald.index))
    if (name == "Trump"):
        for state in tqdm(states):
            state_df = df.loc[df['state'] == state]

            positive_trump_sum_vader = 0
            positive_trump_count_vader = 0
            positive_trump_count_model = 0
            negative_trump_sum_vader = 0
            neutral_trump_count_vader = 0
            negative_trump_count_vader = 0

            negative_trump_count_model = 0
            positive_trump_opinion_vader_sum = 0
            positive_trump_opinion_vader_count = 0
            negative_trump_opinion_vader_count = 0
            negative_trump_opinion_vader_sum = 0

            positive_trump_opinion_model_sum = 0
            positive_trump_opinion_model_count = 0
            negative_trump_opinion_model_count = 0
            negative_trump_opinion_model_sum = 0

            for index, row in state_df.iterrows():

                if (row.vader>0):
                    positive_trump_sum_vader += row.vader
                    positive_trump_count_vader += 1
                    positive_trump_opinion_vader_sum += row.vader*row.opinion
                    positive_trump_opinion_vader_count += 1

                elif (row.vader<0):
                    negative_trump_sum_vader += row.vader
                    negative_trump_count_vader += 1
                    negative_trump_opinion_vader_sum += row.vader*row.opinion
                    negative_trump_opinion_vader_count += 1

                else:
                    neutral_trump_count_vader += 1

                if (row.model>0):
                    positive_trump_count_model += 1
                    positive_trump_opinion_model_sum += row.opinion
                    positive_trump_opinion_model_count+=1

                else:
                    negative_trump_count_model += 1
                    negative_trump_opinion_model_sum += row.opinion
                    negative_trump_opinion_model_count += 1

            vader_df.at[row.state, 'Trump Positive Sum'] = positive_trump_sum_vader
            vader_df.at[row.state,'Trump Total Sum'] = positive_trump_sum_vader + abs(negative_trump_sum_vader)
            vader_df.at[row.state,'Trump Positive count'] = positive_trump_count_vader
            vader_df.at[row.state,'Trump Total count'] = positive_trump_count_vader + negative_trump_count_vader + neutral_trump_count_vader
            vader_df.at[row.state,'Trump Neutral count'] = neutral_trump_count_vader
            vader_df.at[row.state,'Trump Negative Sum'] = abs(negative_trump_sum_vader)
            vader_df.at[row.state,'Trump Negative count'] = negative_trump_count_vader

            trained_df.at[row.state,'Trump Positive count'] = positive_trump_count_model
            trained_df.at[row.state,'Trump Total count'] = positive_trump_count_model + negative_trump_count_model
            trained_df.at[row.state,'Trump Negative count'] = negative_trump_count_model

            op_vader.at[row.state,'Trump Positive Sum'] = positive_trump_opinion_vader_sum
            op_vader.at[row.state,'Trump Positive count'] = positive_trump_opinion_vader_count
            op_vader.at[row.state,'Trump Total Sum'] = abs(negative_trump_opinion_vader_sum) + positive_trump_opinion_vader_sum
            op_vader.at[row.state,'Trump Total count'] = abs(negative_trump_opinion_vader_count) + positive_trump_opinion_vader_count
            op_vader.at[row.state,'Trump Negative Sum'] = abs(negative_trump_opinion_vader_sum)
            op_vader.at[row.state,'Trump Negative count'] = negative_trump_opinion_vader_count
            op_vader.at[row.state,'Trump Neutral count'] = neutral_trump_count_vader

            op_trained.at[row.state,'Trump Positive Sum'] = positive_trump_opinion_model_sum
            op_trained.at[row.state,'Trump Total Sum'] = abs(negative_trump_opinion_model_sum) + positive_trump_opinion_model_sum
            op_trained.at[row.state,'Trump Positive count'] = positive_trump_opinion_model_count
            op_trained.at[row.state,'Trump Total count'] = negative_trump_opinion_model_count + positive_trump_opinion_model_count
            op_trained.at[row.state,'Trump Negative Sum'] = abs(negative_trump_opinion_model_sum)
            op_trained.at[row.state,'Trump Negative count'] = negative_trump_opinion_model_count

    else:
       for state in states:
            state_df = df.loc[df['state'] == state]

            positive_biden_sum_vader = 0
            positive_biden_count_vader = 0
            positive_biden_count_model = 0
            negative_biden_sum_vader = 0
            neutral_biden_count_vader = 0
            negative_biden_count_vader = 0

            negative_biden_count_model = 0
            positive_biden_opinion_vader_sum = 0
            positive_biden_opinion_vader_count = 0
            negative_biden_opinion_vader_count = 0
            negative_biden_opinion_vader_sum = 0

            positive_biden_opinion_model_sum = 0
            positive_biden_opinion_model_count = 0
            negative_biden_opinion_model_count = 0
            negative_biden_opinion_model_sum = 0

            for index, row in state_df.iterrows():

                if (row.vader>0):
                    positive_biden_sum_vader += row.vader
                    positive_biden_count_vader += 1
                    positive_biden_opinion_vader_sum += row.vader*row.opinion
                    positive_biden_opinion_vader_count += 1

                elif (row.vader<0):
                    negative_biden_sum_vader += row.vader
                    negative_biden_count_vader += 1
                    negative_biden_opinion_vader_sum += row.vader*row.opinion
                    negative_biden_opinion_vader_count += 1

                else:
                    neutral_biden_count_vader += 1

                if (row.model>0):
                    positive_biden_count_model += 1
                    positive_biden_opinion_model_sum += row.opinion
                    positive_biden_opinion_model_count+=1

                else:
                    negative_biden_count_model += 1
                    negative_biden_opinion_model_sum += row.opinion
                    negative_biden_opinion_model_count += 1

            vader_df.at[row.state, 'Biden Positive Sum'] = positive_biden_sum_vader
            vader_df.at[row.state,'Biden Total Sum'] = positive_biden_sum_vader + abs(negative_biden_sum_vader)
            vader_df.at[row.state,'Biden Positive count'] = positive_biden_count_vader
            vader_df.at[row.state,'Biden Total count'] = positive_biden_count_vader + negative_biden_count_vader + neutral_biden_count_vader
            vader_df.at[row.state,'Biden Neutral count'] = neutral_biden_count_vader
            vader_df.at[row.state,'Biden Negative Sum'] = abs(negative_biden_sum_vader)
            vader_df.at[row.state,'Biden Negative count'] = negative_biden_count_vader

            trained_df.at[row.state,'Biden Positive count'] = positive_biden_count_model
            trained_df.at[row.state,'Biden Total count'] = positive_biden_count_model + negative_biden_count_model
            trained_df.at[row.state,'Biden Negative count'] = negative_biden_count_model

            op_vader.at[row.state,'Biden Positive Sum'] = positive_biden_opinion_vader_sum
            op_vader.at[row.state,'Biden Positive count'] = positive_biden_opinion_vader_count
            op_vader.at[row.state,'Biden Total Sum'] = abs(negative_biden_opinion_vader_sum) + positive_biden_opinion_vader_sum
            op_vader.at[row.state,'Biden Total count'] = abs(negative_biden_opinion_vader_count) + positive_biden_opinion_vader_count
            op_vader.at[row.state,'Biden Negative Sum'] = abs(negative_biden_opinion_vader_sum)
            op_vader.at[row.state,'Biden Negative count'] = negative_biden_opinion_vader_count
            op_vader.at[row.state,'Biden Neutral count'] = neutral_biden_count_vader

            op_trained.at[row.state,'Biden Positive Sum'] = positive_biden_opinion_model_sum
            op_trained.at[row.state,'Biden Total Sum'] = abs(negative_biden_opinion_model_sum) + positive_biden_opinion_model_sum
            op_trained.at[row.state,'Biden Positive count'] = positive_biden_opinion_model_count
            op_trained.at[row.state,'Biden Total count'] = negative_biden_opinion_model_count + positive_biden_opinion_model_count
            op_trained.at[row.state,'Biden Negative Sum'] = abs(negative_biden_opinion_model_sum)
            op_trained.at[row.state,'Biden Negative count'] = negative_biden_opinion_model_count

    return (vader_df,trained_df,op_vader,op_trained)

if __name__ == "__main__":
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New York', 'New Mexico', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    df_donald = pd.read_csv("Datasets/Validation/US/hashtag_donaldtrump_filtered.csv")
    df_biden = pd.read_csv("Datasets/Validation/US/hashtag_joebiden_filtered.csv")

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
            'Trump Total count',
            'Biden Positive count',
            'Biden Negative count',
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
            'Trump Total count',
            'Biden Positive count',
            'Biden Negative count',
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