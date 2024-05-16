import pickle
import pandas as pd
import numpy as np
import mlflow
from sklearn.ensemble import RandomForestRegressor


def train_baseline() -> None:
    """
    Function saving .pkl file with fitted baseline RandomForestRegressor model 
    """
    rf = RandomForestRegressor(n_estimators=200, min_samples_leaf=3, min_samples_split=3, n_jobs=-1)

    rf.fit(
        X=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/X_train.csv'),
        y=np.array(pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_train.csv')).reshape(-1)
    )

if __name__ == '__main__':
    mlflow.set_tracking_uri("http://localhost:8080")
    mlflow.set_experiment('sklearn2')
    mlflow.sklearn.autolog()
    with mlflow.start_run():
        train_baseline()
