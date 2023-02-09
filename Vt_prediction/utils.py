#Importing the basic librarires

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error ,mean_squared_error, r2_score
import numpy as np


from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import BayesianRidge


def clean_dataset(df):
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

def data_processing(data):
    le = LabelEncoder()
    object_columns = data.iloc[:, :].select_dtypes(include=['object']).columns
    for col in object_columns:
        data[col]= le.fit_transform(data[col].astype(str))
    clean_dataset(data)
    data = data[data['Vt'] < 30.0]
    X = data.drop(columns="Vt")
    y = data["Vt"]
    return X, y

def split_data(X, y):
    # split the data train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
    return  X_train, X_test, y_train, y_test

def print_evaluate(true, predicted):
    mae = mean_absolute_error(true, predicted)
    mse = mean_squared_error(true, predicted)
    rmse = np.sqrt(mean_squared_error(true, predicted))
    r2_square = r2_score(true, predicted)
    print('MAE:', mae)
    print('MSE:', mse)
    print('RMSE:', rmse)
    print('R2 Square', r2_square)
    print('__________________________________')

def evaluate(true, predicted):
    mae = mean_absolute_error(true, predicted)
    mse = mean_squared_error(true, predicted)
    rmse = np.sqrt(mean_squared_error(true, predicted))
    r2_square = r2_score(true, predicted)
    return mae, mse, rmse, r2_square

class MyModels(object):
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test

    def DecisionTreeRegressor(self, max_depth, min_samples_leaf, random_state):
        dt_reg = DecisionTreeRegressor(max_depth=max_depth, min_samples_leaf=min_samples_leaf, random_state=random_state)
        dt_reg.fit(self.X_train, self.y_train)
        test_pred = dt_reg.predict(self.X_test)
        train_pred = dt_reg.predict(self.X_train)
        return (test_pred, train_pred )

    def RandomForestRegressor(self, best_params):
        rf_reg = RandomForestRegressor(max_depth=best_params["max_depth"], max_features=best_params["max_features"], min_samples_leaf=best_params["min_samples_leaf"], min_samples_split=best_params["min_samples_split"], n_estimators=best_params["n_estimators"])
        rf_reg.fit(self.X_train, self.y_train)
        test_pred = rf_reg.predict(self.X_test)
        train_pred = rf_reg.predict(self.X_train)
        return (test_pred, train_pred )

    def XGBoostRegressor(self):
        xgb_reg = XGBRegressor()
        xgb_reg.fit(self.X_train, self.y_train)
        test_pred = xgb_reg.predict(self.X_test)
        train_pred = xgb_reg.predict(self.X_train)
        return (test_pred, train_pred)

    def GradientBoostRegressor(self):
        gb_reg = GradientBoostingRegressor()
        gb_reg.fit(self.X_train, self.y_train)
        test_pred = gb_reg.predict(self.X_test)
        train_pred = gb_reg.predict(self.X_train)
        return (test_pred, train_pred)

    def BayesianRidgeRegression(self):
        br_reg = BayesianRidge()
        br_reg.fit(self.X_train, self.y_train)
        test_pred = br_reg.predict(self.X_test)
        train_pred = br_reg.predict(self.X_train)
        return (test_pred, train_pred)

