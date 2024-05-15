import pandas as pd

def drop_nan_columns(dataframe: pd.DataFrame,
                     columns: list[str],
                     name: str) -> pd.DataFrame:
    """
    Drop columns with multiple NAN values
    
    :dataframe: 
        – original pd.DataFrame(s)
    :columns: 
        – list of columns to cl
    :return: 
        – return modified pd.DataFrame
    
    """

    for column in columns:
        dataframe.drop(column, axis=1, inplace=True)
    dataframe.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/dropped_vals/dropped_values_{name}.csv')

if __name__=='__main__':
    drop_nan_columns()