import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from survival_analysis.model import (choose_optimal_model, 
                                                data_dummy, 
                                                get_cat)


def plot_survival_function(optimal_model):
  optimal_model.plot_survival_function()
  plt.title('Survival function')
  
def plot_hazard_function(optimal_model):  
  optimal_model.plot_cumulative_hazard()
  plt.title('Hazard function')
  

def clv_dist(survival):
  plt.hist(survival['CLV'])
  plt.title('CLV Distribution')
  plt.show()
  
def clv_categorical_plots(survival, categorical):
  plt.title('CLV density plots: compared for categorical variables')
  for i in categorical:
    sns.kdeplot(data=survival, x="CLV", hue = categorical[i], fill=False, common_norm=False, alpha=1)
    plt.show()
