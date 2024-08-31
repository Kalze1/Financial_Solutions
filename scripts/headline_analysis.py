import matplotlib.pyplot as plt
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment_vader(df, text_column):
    """
    Analyze sentiment using VADER and classify it into positive, negative, and neutral categories.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the text data.
    text_column (str): The name of the column containing the text to analyze.
    
    Returns:
    pd.DataFrame: The original DataFrame with additional columns for sentiment score and classification.
    """
    # Initialize VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Calculate sentiment scores
    df['sentiment_score'] = df[text_column].apply(lambda x: sid.polarity_scores(x)['compound'])

    # Classify sentiment based on score
    def classify_sentiment(score):
        if score > 0.05:
            return 'positive'
        elif score < -0.05:
            return 'negative'
        else:
            return 'neutral'

    df['sentiment'] = df['sentiment_score'].apply(classify_sentiment)

    # Calculate sentiment frequency
    sentiment_counts = df['sentiment'].value_counts()

    return df


