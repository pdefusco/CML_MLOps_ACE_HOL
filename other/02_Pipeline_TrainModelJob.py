# ###########################################################################
#
#  CLOUDERA APPLIED MACHINE LEARNING PROTOTYPE (AMP)
#  (C) Cloudera, Inc. 2021
#  All rights reserved.
#
#  Applicable Open Source License: Apache 2.0
#
#  NOTE: Cloudera open source products are modular software products
#  made up of hundreds of individual components, each of which was
#  individually copyrighted.  Each Cloudera open source product is a
#  collective work under U.S. Copyright Law. Your license to use the
#  collective work is as provided in your written agreement with
#  Cloudera.  Used apart from the collective work, this file is
#  licensed for your use pursuant to the open source license
#  identified above.
#
#  This code is provided to you pursuant a written agreement with
#  (i) Cloudera, Inc. or (ii) a third-party authorized to distribute
#  this code. If you do not have a written agreement with Cloudera nor
#  with an authorized and properly licensed third party, you do not
#  have any rights to access nor to use this code.
#
#  Absent a written agreement with Cloudera, Inc. (“Cloudera”) to the
#  contrary, A) CLOUDERA PROVIDES THIS CODE TO YOU WITHOUT WARRANTIES OF ANY
#  KIND; (B) CLOUDERA DISCLAIMS ANY AND ALL EXPRESS AND IMPLIED
#  WARRANTIES WITH RESPECT TO THIS CODE, INCLUDING BUT NOT LIMITED TO
#  IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY AND
#  FITNESS FOR A PARTICULAR PURPOSE; (C) CLOUDERA IS NOT LIABLE TO YOU,
#  AND WILL NOT DEFEND, INDEMNIFY, NOR HOLD YOU HARMLESS FOR ANY CLAIMS
#  ARISING FROM OR RELATED TO THE CODE; AND (D)WITH RESPECT TO YOUR EXERCISE
#  OF ANY RIGHTS GRANTED TO YOU FOR THE CODE, CLOUDERA IS NOT LIABLE FOR ANY
#  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE OR
#  CONSEQUENTIAL DAMAGES INCLUDING, BUT NOT LIMITED TO, DAMAGES
#  RELATED TO LOST REVENUE, LOST PROFITS, LOSS OF INCOME, LOSS OF
#  BUSINESS ADVANTAGE OR UNAVAILABILITY, OR LOSS OR CORRUPTION OF
#  DATA.
#
# ###########################################################################

!pip3 install -r requirements.txt

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import cdsw
import cmlapi
import time
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, LabelEncoder, Binarizer
from sklearn.pipeline import Pipeline
from src.api import ApiUtility
import pickle

# You can access all models with API V2

client = cmlapi.default_client()

# Collect data from Model Metrics Store

# You can use an APIV2-based utility to access the latest model's metadata. For more, explore the src folder
apiUtil = ApiUtility()

Model_AccessKey = apiUtil.get_latest_deployment_details_allmodels()["model_access_key"]
Deployment_CRN = apiUtil.get_latest_deployment_details_allmodels()["latest_deployment_crn"]
Model_CRN = apiUtil.get_latest_deployment_details_allmodels()["model_crn"]

# Get the various Model Endpoint details
HOST = os.getenv("CDSW_API_URL").split(":")[0] + "://" + os.getenv("CDSW_DOMAIN")
model_endpoint = (
    HOST.split("//")[0] + "//modelservice." + HOST.split("//")[1] + "/model"
)

project_id = os.environ["CDSW_PROJECT_ID"]

# Read in the model metrics dict
model_metrics = cdsw.read_metrics(
    model_crn=Model_CRN, model_deployment_crn=Deployment_CRN
)

# This is a handy way to unravel the dict into a big pandas dataframe
metrics_df = pd.io.json.json_normalize(model_metrics["metrics"])

y = metrics_df['metrics.final_label'].dropna()
y = y.astype("int")
X = metrics_df.filter(like="input_data").dropna().drop(columns=['metrics.input_data.conversion'])
X.columns = X.columns.str.replace('metrics.input_data.','')

# Load most up to date model
def load_latest_model_version():

    model_dir = "/home/cdsw/models"
    models_list = os.listdir(model_dir)
    models_dates_list = [model_path.replace(".sav","") for model_path in models_list if "final" in model_path]
    model_dates = [int(i.split('_')[2]) for i in models_dates_list]
    latest_model_index = np.argmax(model_dates)
    latest_model_path = model_dir + "/" + models_list[latest_model_index]

    loaded_model = pickle.load(open(latest_model_path, 'rb'))

    return loaded_model

def store_latest_model_version(model):

    now = time.time()
    filename = "/home/cdsw/models/final_model_{}.sav".format(round(now))

    pickle.dump(model, open(filename, 'wb'))

loaded_model = load_latest_model_version()
loaded_model.fit(X, y)
store_latest_model_version(loaded_model)
