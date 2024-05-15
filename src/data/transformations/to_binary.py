import pandas as pd

def to_binary(dataframe: pd.DataFrame, 
              columns: list[str],
              name: str) -> pd.DataFrame:
    """
    Fill the missing values with the most frequent value and transform them to binary format
    
    :dataframes: 
        – original pd.DataFrame(s)
        
    :columns: 
        – list of columns to fill
        
    :return:
        – return modified pd.DataFrame
    """
    binaries = {'t': 1, 'f': 0}

    for column in columns:
        dataframe[column] = dataframe[column].fillna(dataframe[column].mode()[0])
        dataframe[column] = dataframe[column].replace(binaries).astype(int)
    dataframe.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/binary_form/binary_format_{name}.csv')


if __name__ == '__main__':
    to_binary(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/filled_by_0/filled_by_0_train.csv'), 
        columns=['is_apartments'],
        name='train'
    )

    to_binary(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/filled_by_0/filled_by_0_test.csv'), 
        columns=['is_apartments'],
        name='test'
    )