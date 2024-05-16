import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


rf = RandomForestRegressor(n_estimators=350, min_samples_leaf=3, min_samples_split=3, n_jobs=-1)

rf.fit(
    X=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/X_train.csv'),
    y=pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_train.csv')
)

filename = '/Users/klimbelousov/Documents/Projects/real_estate/models/baseline_model.pkl'
pickle.dump(rf, open(filename, 'wb'))