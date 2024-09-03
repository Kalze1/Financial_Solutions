import pandas as pd
from scripts.headline_analysis import analyze_sentiment_vader


def calculate_correlation(df_news, df_stock, column):
    
    df_stock['stock_price_change'] = df_stock[column].pct_change()

    daily_sentiment= df_news.groupby('date')['sentiment_score'].mean()
    daily_sentiment_df = daily_sentiment.reset_index()
    daily_sentiment_df.columns = ['date', 'mean_sentiment_score']


    combined_data = pd.DataFrame({'date': [], 'stock_price_change': []})
    combined_data['date'] = df_stock['date']
    combined_data['stock_price_change'] = df_stock['stock_price_change']
    combined_data['date'] = pd.to_datetime(combined_data['date'])
    daily_sentiment_df['date'] = pd.to_datetime(daily_sentiment_df['date'])
    combined_data = pd.merge(combined_data, daily_sentiment_df[['date', 'mean_sentiment_score']], on='date', how='left')
    combined_data = combined_data.dropna(how="any")
    correlation = combined_data[['mean_sentiment_score', 'stock_price_change']].corr()
    

    return correlation



