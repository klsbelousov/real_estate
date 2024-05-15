import pandas as pd


def data_to_processed() -> None:
    X_train = pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/X/X_train.csv')
    X_test = pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/X/X_test.csv')
    y_train = pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/Y/y_train.csv')
    y_test = pd.read_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/interim/Y/y_test.csv')
    dataframes = [X_train, X_test, y_train, y_test]
    for df in dataframes:
        for column in df.columns:
            if 'Unnamed' in column:
                df.drop(column, axis=1, inplace=True)
    X_train.to_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/X_train.csv', index=False)
    X_test.to_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/X_test.csv', index=False)
    y_train.to_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_train.csv', index=False)
    y_test.to_csv('/Users/klimbelousov/Documents/Projects/real_estate/data/processed/y_test.csv', index=False)


if __name__ == '__main__':
    data_to_processed()