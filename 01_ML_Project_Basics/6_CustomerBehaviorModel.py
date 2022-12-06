from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
import cdsw
import pandas as pd
import pickle

customer_behavior_model = pickle.load(open('/home/cdsw/01_ML_Project_Basics/models/final_model.sav', 'rb'))

#Inputs:
#recency            int64
#history          float64
#used_discount      int64
#used_bogo          int64
#is_referral        int64
#channel           object -> one hot encoded
#offer             object -> one hot encoded

#Target:
#conversion         int64
@cdsw.model_metrics
def predict(data):
    df = pd.DataFrame(data, index=[0])
    #df.columns = ['recency', 'history', 'used_discount', 'used_bogo', 'is_referral', 'channel', 'offer']
    print(df.columns)
    print(df.head())
    df['recency'] = df['recency'].astype(float)
    df['history'] = df['history'].astype(float)
    df['used_discount'] = df['used_discount'].astype(float)
    df['used_bogo'] = df['used_bogo'].astype(float)
    df['is_referral'] = df['is_referral'].astype(float)

    cdsw.track_metric("input_data", dict(df))
    pred = customer_behavior_model.predict(df)[0]
    print(pred)
    print(type(pred))
    cdsw.track_metric("prediction", float(pred))

    return {'result': pred}

#  Web  329.08             1  No Offer           6       1     1
#recency history used_discount used_bogo is_referral channel offer

#{
#  "recency": “6”,
#  "history": "329.08",
#  "used_discount": “1”,
#  "used_bogo": "1",
#  "is_referral": "1",
#  "channel": "Web",
#  "offer": "No Offer"
#}

#{
#  "result": "1"
#}
