import optuna
import mlflow
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

def objective(trial):
    mlflow.set_experiment('testing_optuna')
    with mlflow.start_run(nested=True):
        # Define hyperparameters
        params = {
            "criterion": "squared_error",
            "n_estimators": trial.suggest_int("n_estimators", 200, 500),
            "max_depth": trial.suggest_int("max_depth", 20, 70),
            "min_samples_leaf": 2,
            "min_samples_split": 2,
            "random_state": 52,
            'n_jobs': -1,
        }

        # Train XGBoost model
        rf = RandomForestRegressor(**params)
        rf.fit(
            X=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/X_train.csv'),
            y=np.array(pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_train.csv')).reshape(-1)
        )
        y_pred = rf.predict(
            X=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/X_test.csv')
        )
        error = mean_absolute_percentage_error(
            y_true=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_test.csv'),
            y_pred=y_pred
        )


        # Log to MLflow
        mlflow.log_params(params)
        mlflow.log_metric("mape", error)

    

    return error
study = optuna.create_study(direction="minimize")
# Execute the hyperparameter optimization trials.
# Note the addition of the `champion_callback` inclusion to control our logging
study.optimize(objective, n_trials=30)
print(study.best_params)