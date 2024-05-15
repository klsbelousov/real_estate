import pandas as pd

def predictors_n_target(dataframe: pd.DataFrame,
                        name: str) -> (pd.DataFrame | pd.Series):
    """
    Splitting data into predictors and target variables
    """
    X = dataframe.drop('price', axis=1)
    y = dataframe['price']
    X.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/X/{name}_X.csv')
    y.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/Y/{name}_y.csv')

if __name__ == '__main__':
    predictors_n_target(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/encoding/encoding_train.csv'),
        'train'
    )

    predictors_n_target(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/encoding/encoding_test.csv'),
        'test'
    )