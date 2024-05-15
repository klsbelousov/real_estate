import pandas as pd
from sklearn.preprocessing import PowerTransformer

def transform(dataframe: pd.DataFrame,
              name: str) -> pd.DataFrame:
    """
    Function performs Yeo-Jonhson transformation
    """
    pt = PowerTransformer()
    X_scaled = pt.fit_transform(dataframe)
    X_scaled = pd.DataFrame(X_scaled, columns=[i for i in dataframe.columns if i != 'price'])
    X_scaled.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/X/{name}_X_scaled.csv')


if __name__ == '__main__':
    transform(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/X/train_X.csv'), 
        'train'
    )
    
    transform(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/X/test_X.csv'), 
        'test'
    )
