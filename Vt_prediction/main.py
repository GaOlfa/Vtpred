import pandas as pd
import numpy as np
from pathlib import Path
from correction import df_mutation
import json
import utils
import os
import warnings
from model_tuning import hyperparameters_tuning
warnings.filterwarnings("ignore")



def main():

    data = pd.read_csv(path, delimiter=',')
    #data = df_mutation(data)
    #data.drop_duplicates()
    #columns = list(data.columns[1:35])
    #data = data[~(data[columns] == 0).all(axis=1)]
    # separation the data type columns [ object and numeric ]
    X, y = utils.data_processing(data.copy())
    X_train, X_test, y_train, y_test = utils.split_data(X, y)

    trainer = utils.MyModels(X_train, y_train, X_test, y_test)

    # best_grid_dtr = hyperparameters_tuning('dtr', param_grid_dtr, X_train, y_train)
    # #print(best_grid_dtr)
    # print("Decision Tree Regressor Results:\n")
    # test_pred, train_pred = trainer.DecisionTreeRegressor(best_grid_dtr)
    # print('Test set evaluation:\n_____________________________________')
    # utils.print_evaluate(y_test, test_pred)
    # print('Train set evaluation:\n_____________________________________')
    # utils.print_evaluate(y_train, train_pred)
    # results_df = pd.DataFrame(data=[["Decision Tree Regressor", *utils.evaluate(y_test, test_pred)]],
    #                           columns=['Model', 'MAE', 'MSE', 'RMSE', 'R2 Square'])
    # #print(results_df)
    #
    #

    best_grid_rf = hyperparameters_tuning('rf', param_grid_rf, X_train, y_train)
    #print(best_grid_rf)
    print("Random Forest Regressor Results:\n")
    test_pred, train_pred = trainer.RandomForestRegressor(best_grid_rf)
    print('Test set evaluation:\n_____________________________________')
    utils.print_evaluate(y_test, test_pred)
    print('Train set evaluation:\n_____________________________________')
    utils.print_evaluate(y_train, train_pred)
    # results_df = results_df.append(pd.DataFrame(data=[["Random Forest Regressor", *utils.evaluate(y_test, test_pred)]],
    #                                             columns=['Model', 'MAE', 'MSE', 'RMSE', 'R2 Square']), ignore_index=True)


    # best_grid_xgbr = hyperparameters_tuning('xgbr', param_grid_xgbr, X_train, y_train)
    # print(best_grid_xgbr)
    # print("XGBoost Regressor Results:\n")
    # test_pred, train_pred = trainer.XGBoostRegressor(best_grid_xgbr)
    # print('Test set evaluation:\n_____________________________________')
    # utils.print_evaluate(y_test, test_pred)
    # print('Train set evaluation:\n_____________________________________')
    # utils.print_evaluate(y_train, train_pred)
    # results_df = results_df.append(pd.DataFrame(data=[["XGBoost Regressor", *utils.evaluate(y_test, test_pred)]],
    #                                             columns=['Model', 'MAE', 'MSE', 'RMSE', 'R2 Square']), ignore_index=True)

    #
    # best_grid_gbr = hyperparameters_tuning('gbr', param_grid_gbr, X_train, y_train)
    # #print(best_grid_xgbr)
    # print("Gradient Boost Regressor Results:\n")
    # test_pred, train_pred = trainer.GradientBoostRegressor(best_grid_gbr)
    # print('Test set evaluation:\n_____________________________________')
    # utils.print_evaluate(y_test, test_pred)
    # print('Train set evaluation:\n_____________________________________')
    # utils.print_evaluate(y_train, train_pred)
    # results_df = results_df.append(pd.DataFrame(data=[["Gradient Boost Regressor", *utils.evaluate(y_test, test_pred)]],
    #                                             columns=['Model', 'MAE', 'MSE', 'RMSE', 'R2 Square']), ignore_index=True)

    # print("Bayesian Ridge Regressor Results:\n")
    # test_pred, train_pred = trainer.BayesianRidgeRegression()
    # print('Test set evaluation:\n_____________________________________')
    # utils.print_evaluate(y_test, test_pred)
    # print('Train set evaluation:\n_____________________________________')
    # utils.print_evaluate(y_train, train_pred)
    # results_df = results_df.append(pd.DataFrame(data=[["Bayesian Ridge Regressor", *utils.evaluate(y_test, test_pred)]],
    #                             columns=['Model', 'MAE', 'MSE', 'RMSE', 'R2 Square']), ignore_index=True)
    #
    #
    #
    #print(results_df)



if __name__ == "__main__" :
    with open('config.json', 'r') as file:
        f = json.load(file)
    path = Path(os.getcwd()+f['path'])
    param_grid_dtr = f["DecisionTreeRegressor"]
    param_grid_rf = f["RandomForestRegressor"]
    param_grid_xgbr = f["XGBRegressor"]
    param_grid_gbr = f["GradientBoostingRegressor"]
    main()