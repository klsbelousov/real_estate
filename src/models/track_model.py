import pickle
import pandas as pd
import numpy as np
import mlflow
from sklearn.ensemble import RandomForestRegressor


def train_baseline() -> None:
    """
    Function saving .pkl file with fitted baseline RandomForestRegressor model 
    """
    rf = RandomForestRegressor(n_estimators=481, max_depth=35, min_samples_leaf=2, min_samples_split=2, n_jobs=-1)

    rf.fit(
        X=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/X_train.csv'),
        y=np.array(pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_train.csv')).reshape(-1)
    )

    filename = 'src/models/baseline_model.pkl'
    pickle.dump(rf, open(filename, 'wb'))

if __name__ == '__main__':
    mlflow.set_experiment('sklearn_rf_3')
    mlflow.sklearn.autolog()
    with mlflow.start_run():
        train_baseline()
