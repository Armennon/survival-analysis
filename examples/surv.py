import surival_analysis.model.*
import survival_analysis.visualizations.*

data = 'https://raw.githubusercontent.com/Armennon/survival-analysis/main/examples/telco.csv'

survival = data_dummy('telco.csv')
categorical = get_cat('telco.csv')
models_list = model_builder(survival)
optimal_model = choose_optimal_model(models_list)
aft_optimal_model = find_aft_model(optimal_model_name, survival)
plot_survival_function = plot_survival_function(optimal_model)
plot_hazard_function = plot_hazard_function(optimal_model)
pred = aft_optimal_model.predict_survival_function(survival)
survival_with_clv = get_CLV(pred, survival)
clv_dist = clv_dist(survival_with_clv)
categ_plots = clv_categorical_plots(survival, categorical)




print(f'{optimal_model_name} is the the most optimal model for the given dataset.')
plot_survival_function
plot_hazard_function
clv_dist
categ_plots
