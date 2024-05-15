import pandas as pd
from sklearn.model_selection import train_test_split


def validation_sampling(X: pd.DataFrame, 
                        y: pd.Series,
                        test_size: float,
                        seed: int) -> pd.DataFrame:
    """
    Splitting data into holdout sample
    
    :X: 
        - predictor variables presented as pd.DataFrame
        
    :y: 
        - target variable as pd.Series
        
    :test_size: 
        - size of sample
        
    :seed: 
        - randomness variable
    """
    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=test_size, random_state=seed)
    X_train.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/X/X_train.csv')
    X_test.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/X/X_test.csv')
    y_train.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/Y/y_train.csv')
    y_test.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/Y/y_test.csv')


if __name__ == '__main__':
    validation_sampling(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/X/train_X_scaled.csv'), 
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/Y/train_y.csv'), 
        test_size=0.2, 
        seed=52
    )
    