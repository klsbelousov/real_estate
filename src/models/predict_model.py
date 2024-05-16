import os

import pickle
import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error, mean_absolute_error, mean_squared_error


def baseline_prediction(model: os.path):

    baseline_rf = pickle.load(open(model, 'rb'))

    y_pred = baseline_rf.predict(
        X=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/X_test.csv')
    )

    mae = mean_absolute_error(
        y_true=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_test.csv'),
        y_pred=y_pred
    )
    mse = mean_squared_error(
        y_true=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_test.csv'),
        y_pred=y_pred
    )
    mape = mean_absolute_percentage_error(
        y_true=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_test.csv'),
        y_pred=y_pred
    )

    print(y_pred)
    print(mae, mse, mape)

    return y_pred, mae, mse, mape

if __name__ == '__main__':
    baseline_prediction('/Users/klimbelousov/Documents/Projects/real_estate/models/baseline_model.pkl')