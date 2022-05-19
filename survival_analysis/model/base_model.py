import pandas as pd
import numpy as np


from lifelines import WeibullFitter,\
                      LogNormalFitter,\
                      LogLogisticFitter,\
                      WeibullAFTFitter,\
                      LogNormalAFTFitter,\
                      LogLogisticAFTFitter



def data_dummy(data):
  df = pd.read_csv(data)
  num = df.select_dtypes(include='number')
  cat = df.drop(num, axis = 1)
  
  cat_col = cat.columns
  survival = pd.get_dummies(df,
                columns=cat_col,
                prefix=cat_col,
                drop_first=True)
  return survival


def get_cat(data):
  df = pd.read_csv(data)
  num = df.select_dtypes(include='number')
  cat = df.drop(num, axis = 1)
  return cat

def model_builder(survival_df):
  wb = WeibullFitter()
  wb_aft = WeibullAFTFitter()
  log = LogNormalFitter()
  log_aft = LogNormalAFTFitter()
  loglogis = LogLogisticFitter()
  loglog_aft = LogLogisticAFTFitter()
  model_aft = {'model': [wb, log, loglogis], 'model_aft': [wb_aft, log_aft, loglog_aft]}
  ls = {"model": [],"AIC": []}
  for model in [wb, log, loglogis]:
      model.fit(durations = survival_df["tenure"], event_observed = survival_df["churn_Yes"])
      ls["model"].append(model)
      ls["AIC"].append(model.AIC_)
  return ls


def choose_optimal_model(models_list):
  min_aic = min(models_list['AIC'])
  vals = list(models_list['AIC'])
  keys = list(models_list['model'])
  for i in vals:  
    if i == min_aic:
      k =  keys[vals.index(i)]
      name = k.__class__.__name__
  return k


def optimal_model_name(model):
  return model.__class__.__name__




def find_aft_model(optimal_model_name, survival_df):
  wb_aft = WeibullAFTFitter()
  log_aft = LogNormalAFTFitter()
  loglog_aft = LogLogisticAFTFitter()
  if optimal_model_name == 'WeibullFitter':
    aft = wb_aft
  elif optimal_model_name == 'LogNormalFitter':
    aft = log_aft
  else:
    aft = loglog_aft
  aft.fit(survival_df, duration_col='tenure', event_col='churn_Yes')
  return aft

pred = aft_optimal_model.predict_survival_function(survival)

def get_CLV(pred, survival):
  m = 1300
  r = 0.1
  predt = pred.T
  rangee = range(0, len(predt.columns-1))
  for i in rangee:
    predt.iloc[:, i] = predt.iloc[:, i].values/(1+r/12)**(rangee[i])
  rsum = predt.sum(axis = 1)
  predt['CLV'] = m*rsum
  survival['Rank'] = survival['CLV'].rank()
  survival.sort_values("CLV", ascending=False, inplace = True)
  survival.drop('Rank', axis = 1, inplace = True)
  print('Dataframe with ranked CLV value for each customer')
  return survival
  

