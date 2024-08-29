import pandas as pd
import numpy as np
import re
from string import punctuation


class DataPreprocessor:
    def __init__(self, stopwords_file_path):
        # Load stopwords from the text file into a set
        with open(stopwords_file_path, 'r') as file:
            self.stop_words = set(line.strip() for line in file)
        
    def preprocess(self, df):
        # Handle missing values with forward fill
        df.ffill(inplace=True)

        # Convert data types
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce')

        # Text preprocessing
        def preprocess_text(text):
            # Convert to lowercase and tokenize
            tokens = re.findall(r'\b\w+\b', text.lower())
            
            # Remove stopwords
            tokens = [word for word in tokens if word not in self.stop_words]
            
            # Perform stemming 
            stemmer = lambda w: w[:-1] if len(w) > 4 else w 
            tokens = [stemmer(word) for word in tokens]
            
            return tokens

        df['preprocessed_headline'] = df['headline'].apply(preprocess_text)

        return df



