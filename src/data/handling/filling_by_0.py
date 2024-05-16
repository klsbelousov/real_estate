import pandas as pd


def filling_by_0(dataframe: pd.DataFrame,
                 columns: list[str],
                 name: str) -> None:
    """
    Filling missing values by 0
    
    :dataframes: 
        – original pd.DataFrame
        
    :columns: 
        – list of columns to fill
        
    :return: 
        – return modified pd.DataFrame
    
    """
    for column in columns:
        dataframe[column] = dataframe[column].fillna(0)
    dataframe.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/filled_by_0/filled_by_0_{name}.csv')

if __name__ == '__main__':
    
    filling_by_0(pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/dropped_vals/dropped_values_train.csv'), 
                 columns=['rooms_count', 'kitchen_area','living_area'], 
                 name='train')
    
    filling_by_0(pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/dropped_vals/dropped_values_test.csv'), 
                 columns=['rooms_count', 'kitchen_area','living_area'], 
                 name='test')