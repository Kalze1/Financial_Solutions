import numpy as np
import pandas as pd


class DataPreprocessor:
    def __init__(self):
        pass

    def preprocess(self, df):
        # Handle missing values
        df.fillna(method='ffill', inplace=True)

        # Convert data types
        # df['date'] = df['date'].str.split().str[0]  
        # df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')


        # Normalize numerical features
        df['normalized_Open'] = (df['Open'] - df['Open'].min()) / (df['Open'].max() - df['Open'].min())
        df['normalized_High'] = (df['High'] - df['High'].min()) / (df['High'].max() - df['High'].min())
        df['normalized_Low'] = (df['Low'] - df['Low'].min()) / (df['Low'].max() - df['Low'].min())
        df['normalized_close'] = (df['Close'] - df['Close'].min()) / (df['Close'].max() - df['Close'].min())
        df['normalized_Adj Close'] = (df['Adj Close'] - df['Adj Close'].min()) / (df['Adj Close'].max() - df['Adj Close'].min())
        df['normalized_Volume'] = (df['Volume'] - df['Volume'].min()) / (df['Volume'].max() - df['Volume'].min())





        # Handle outliers using IQR
        def handle_outliers_iqr(col):
            q1, q3 = np.quantile(col, [0.25, 0.75])
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            return col.clip(lower_bound, upper_bound)

        df['Open'] = handle_outliers_iqr(df['Open'])
        df['High'] = handle_outliers_iqr(df['High'])
        df['Low'] = handle_outliers_iqr(df['Low'])
        df['Close'] = handle_outliers_iqr(df['Close'])
        df['Adj Close'] = handle_outliers_iqr(df['Adj Close'])
        df['Volume'] = handle_outliers_iqr(df['Volume'])



        

        return df