from survival_analysis import *

data = 'https://raw.githubusercontent.com/Armennon/survival-analysis/main/examples/telco.csv'

survival = data_dummy(data)
categorical = get_cat(data)
models_list = model_builder(survival)
optimal_model = choose_optimal_model(models_list)
optimal_model_name = optimal_model_name(optimal_model)
aft_optimal_model = find_aft_model(optimal_model_name, survival)
plot_survival_function = plot_survival_function(optimal_model)
plot_hazard_function = plot_hazard_function(optimal_model)
pred = aft_optimal_model.predict_survival_function(survival)
survival_with_clv = get_CLV(pred, survival)
clv_dist = clv_dist(survival_with_clv)
categ_plots = clv_categorical_plots(survival, categorical)




# print(f'{optimal_model_name} is the the most optimal model for the given dataset.')
# print(survival_with_clv)
# print(plot_survival_function)
# print(plot_hazard_function)
# print(clv_dist)
# print(categ_plots)
