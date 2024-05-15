import pandas as pd

def drop_nan_columns(dataframe: pd.DataFrame,
                     columns: list[str],
                     name: str) -> pd.DataFrame:
    """
    Drop columns with multiple NAN values
    
    :dataframe: 
        – original pd.DaaFrame(s)
    :columns: 
        – list of columns to cl
    :return: 
        – return modified pd.DataFrame
    
    """

    for column in columns:
        dataframe.drop(column, axis=1, inplace=True)
    dataframe.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/dropped_vals/dropped_values_{name}.csv')

if __name__=='__main__':
    drop_nan_columns(pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/raw/real_estate_train.csv'), 
                     columns=['Unnamed: 0', 'bedrooms_count', 'balcony', 'year_built'], 
                     name='train')

    drop_nan_columns(pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/raw/real_estate_test.csv'), 
                     columns=['Unnamed: 0', 'bedrooms_count', 'balcony', 'year_built'], 
                     name='test')