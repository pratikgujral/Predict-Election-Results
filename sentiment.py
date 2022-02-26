import pickle
from unicodedata import name
import pandas as pd
from preprocess import preprocessList

def load_models():
    # Load the vectoriser.
    file = open('Training/vectoriser-ngram-(1,2).pickle', 'rb')
    vectoriser = pickle.load(file)
    file.close()
    # Load the LR Model.
    file = open('Training/Sentiment-BNB.pickle', 'rb')
    BNBmodel = pickle.load(file)
    file.close()
    
    return vectoriser, BNBmodel

def predict(vectoriser, model, text):
    # Predict the sentiment
    textdata = vectoriser.transform(preprocessList(text))
    sentiment = model.predict(textdata)
    
    # Make a list of text with sentiment.
    data = []
    for text, pred in zip(text, sentiment):
        data.append((text,pred))
        
    # Convert the list into a Pandas DataFrame.
    df = pd.DataFrame(data, columns = ['text','sentiment'])
    df = df.replace([0,1], ["Negative","Positive"])
    return df

if __name__ == '__main__':
    vectoriser, BNBmodel = load_models()
    text = ["I love this movie!", "This is a terrible movie!"]
    df = predict(vectoriser, BNBmodel, text)
    print(df)
