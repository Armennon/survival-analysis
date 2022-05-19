import matplotlib.pyplot as plt
import seaborn as sns
# from survival_analysis.model import *


def plot_survival_function(optimal_model):
    """
    Method to plot the survival function of the optimal model.
        
    Parameters
    ----------
    model : Lifelines model
        Previously returned optimal model.
    Returns
    -------
    matplotlib object  
        Survival function of the model.
    """
  optimal_model.plot_survival_function()
  plt.title('Survival function')
  
  
  
def plot_hazard_function(optimal_model):  
    """
    Method to plot the hazard function of the optimal model.
        
    Parameters
    ----------
    model : Lifelines model
        Previously returned optimal model.
    Returns
    -------
    matplotlib object  
        Hazard function of the model.
    """
  optimal_model.plot_cumulative_hazard()
  plt.title('Hazard function')
  

def clv_dist(survival):
    """
    Method to plot the CLV distribution.
        
    Parameters
    ----------
    model : Lifelines model
        Previously returned optimal model.
    survival: pandas DataFrame
        Previously dummified DataFrame.
    Returns
    -------
    matplotlib object  
        Distribution function of CLV.
    """
  plt.hist(survival['CLV'])
  plt.title('CLV Distribution')
  plt.show()

  
  
def clv_categorical_plots(survival, categorical):
    """
    Method to plot the CLV distribution.
        
    Parameters
    ----------
    survival: pandas DataFrame
        Previously dummified DataFrame.
    categorical: pandas DataFrame
        DataFrame containing categorical variables
    Returns
    -------
    matplotlib object  
        Distribution functions of each CLV categorical variable.
    """
  plt.title('CLV density plots: compared for categorical variables')
  for i in categorical:
    sns.kdeplot(data=survival, x="CLV", hue = categorical[i], fill=False, common_norm=False, alpha=1)
    plt.show()
