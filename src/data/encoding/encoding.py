import pandas as pd

def encoding(df: pd.DataFrame,
             name: str) -> pd.DataFrame:
    """
    Function perfroms one-hot-encoding for categorical features and writes it to .csv file

    :input:
        – original pd.DataFrame

    :name:
        - naming of output .csv file

    :return:
        - modified pd.DataFrame 
    """
    
    binaries = {True: 1, False: 0}
    df = pd.get_dummies(data=df, drop_first=True)
    df.replace(binaries, inplace=True)
    df.to_csv(f'/Users/klimbelousov/Documents/Projects/real_estate/data/interim/encoding/encoding_{name}.csv')

if __name__ == '__main__':
    encoding(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/cleaned_outliers/cleaned_outliers_train.csv'),
        'train'
    )

    encoding(
        pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/cleaned_outliers/cleaned_outliers_test.csv'),
        'test'
    )