import pandas as pd

def split_district(dataframe: pd.DataFrame, 
                   name: str,
                   pattern: str,
                   column='district') -> None:
    """
    Split district column
    """
    dataframe[['district', 'district_naming']] = dataframe[column].str.split(pattern, expand=True)
    dataframe.drop('district_naming', axis=1, inplace=True)
    dataframe.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/splitted_district/splitted_district_{name}.csv')

if __name__ == '__main__':
    split_district(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/binary_form/binary_format_train.csv'), 
        name='train',
        pattern=' ',
    )

    split_district(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/binary_form/binary_format_train.csv'), 
        name='test',
        pattern=' ',
    )