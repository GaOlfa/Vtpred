from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import BayesianRidge

def hyperparameters_tuning(estimator, parameters, X_train, y_train):
    # Create a base model
    if estimator == "dtr":
        dtr = DecisionTreeRegressor(random_state=10)
        grid_search = GridSearchCV(estimator=dtr, param_grid=parameters, scoring='neg_mean_squared_error',
                                   cv=3, n_jobs=-1, verbose=3, return_train_score=True)

    elif estimator == "rf":
        rf = RandomForestRegressor(random_state=42)
        # Instantiate the grid search model
        grid_search = GridSearchCV(estimator=rf, param_grid=parameters,
                                   cv=3, n_jobs=-1, verbose=2, return_train_score=True)

    elif estimator == "xgbr":
        xgbr = XGBRegressor(seed=20)
        grid_search = GridSearchCV(estimator=xgbr, param_grid=parameters,
                                   verbose=2, scoring='neg_mean_squared_error')

    elif estimator =="gbr":
        gbr = GradientBoostingRegressor(random_state=42)
        grid_search = GridSearchCV(estimator=gbr, param_grid=parameters,
                                   cv=3, n_jobs=-1, verbose=2)

    # elif estimator =="brr":
    #     brr = BayesianRidge(random_state=42)
    #     # Instantiate the grid search model
    #     grid_search = GridSearchCV(estimator=brr, param_grid=parameters,
    #                                cv=3, n_jobs=-1, verbose=2)



    # Fit the grid search to the data
    grid_search.fit(X_train, y_train)
    return(grid_search.best_params_)