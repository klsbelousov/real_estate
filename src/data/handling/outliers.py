import pandas as pd

def clean_outliers(dataframe: pd.DataFrame,
                   name: str) -> None:
    """
    Delete rows in which the value of any of the features exceeds and writes it to .csv file
    
    :dataframes:
        - original pd.DataFrame

    :return:
        - modified pd.DataFrame
    """
    dataframe = dataframe[dataframe['total_area'] < dataframe['total_area'].quantile(.8)]
    dataframe = dataframe[dataframe['total_area'] > 15]
    dataframe.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/cleaned_outliers/cleaned_outliers_{name}.csv')


if __name__ == '__main__':
    clean_outliers(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/splitted_district/splitted_district_train.csv'),
        'train'
    )

    clean_outliers(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/splitted_district/splitted_district_test.csv'),
        'test'
    )