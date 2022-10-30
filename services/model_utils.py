import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go
from catboost import CatBoostClassifier, Pool

# Global variable that stores trained model instance
# MODEL = joblib.load(r"C:\Users\HP\Downloads\random.pkl")

# # Dictionary that converts frontend feature names to names understood by model
# display_to_model = {'age':'Age', 'sex':'Sex', 'cpt':'ChestPainType', 'bp':'RestingBP', 
#                     'chol':'Cholesterol', 'bs':'FastingBS', 'restingECG':'RestingECG',
#                     'maxHR':'MaxHR', 'exerciseAngina':'ExerciseAngina', 'oldpeak':'Oldpeak',
#                     'sts':'ST_Slope'}

def predict_hf(data:pd.DataFrame):

    model = CatBoostClassifier()

    model.load_model("thresholdstroke_pred")
    return model.predict_proba(data)


# def get_shap_df(data:pd.DataFrame):
    
#     shap_values = shap_values[:,:-1].reshape(shap_values.shape[0], len(MODEL.feature_names_))
#     shap_df = pd.DataFrame(shap_values, columns=MODEL.feature_names_).T
#     shap_df.columns = ['feature']
#     shap_df['AbsVal'] = np.abs(shap_df['feature'])
#     shap_df.sort_values('AbsVal', ascending=False, inplace=True)

#     return shap_df

# def plot_shap_values(data:pd.DataFrame):

#     shap_df = get_shap_df(data)

#     fig = go.Figure()
#     fig.add_trace(go.Bar(x=shap_df.index, y=shap_df.feature))
#     fig.update_layout(title='Patient Risk Factors')

#     return fig.to_json()

def get_shap_df(data:pd.DataFrame):
    model = CatBoostClassifier()

    model.load_model(r"C:\Users\HP\Downloads\thresholdstroke_pred")

    data_pool = Pool(data, cat_features=model.get_cat_feature_indices())

    shap_values = model.get_feature_importance(data_pool, type='ShapValues')
    
    shap_values = shap_values[:,:-1].reshape(shap_values.shape[0], len(model.feature_names_))
    shap_df = pd.DataFrame(shap_values, columns=model.feature_names_).T
    shap_df.columns = ['feature']
    shap_df['AbsVal'] = np.abs(shap_df['feature'])
    shap_df.sort_values('AbsVal', ascending=False, inplace=True)

    return shap_df

def plot_shap_values(data:pd.DataFrame):

    shap_df = get_shap_df(data)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=shap_df.index, y=shap_df.feature))
    fig.update_layout(title='Patient Risk Factors')

    return fig.to_json()












