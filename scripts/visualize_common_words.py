import pandas as pd
import re
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk import bigrams
from nltk.tokenize import word_tokenize

# Function to preprocess the text
def preprocess_text(text):
    """
    Preprocesses the input text by converting to lowercase, removing special characters,
    tokenizing, and removing stopwords.
    
    Args:
    text (str): The text to preprocess.
    
    Returns:
    list: A list of tokens after preprocessing.
    """
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords
    tokens = [word for word in tokens if word not in ENGLISH_STOP_WORDS]
    return tokens

# Function to extract most common words
def extract_common_words(tokens_list, n=20):
    """
    Extracts the most common words from a list of tokens.
    
    Args:
    tokens_list (list of list): List of tokenized text.
    n (int): Number of most common words to return.
    
    Returns:
    list: A list of tuples containing the most common words and their counts.
    """
    all_tokens = [token for tokens in tokens_list for token in tokens]
    word_freq = Counter(all_tokens)
    return word_freq.most_common(n)

# Function to extract most common bigrams
def extract_common_bigrams(tokens_list, n=20):
    """
    Extracts the most common bigrams from a list of tokens.
    
    Args:
    tokens_list (list of list): List of tokenized text.
    n (int): Number of most common bigrams to return.
    
    Returns:
    list: A list of tuples containing the most common bigrams and their counts.
    """
    all_bigrams = [bigram for tokens in tokens_list for bigram in bigrams(tokens)]
    bigram_freq = Counter(all_bigrams)
    return bigram_freq.most_common(n)

# Function to visualize most common words
def visualize_common_words(common_words):
    """
    Visualizes the most common words using a bar plot.
    
    Args:
    common_words (list): A list of tuples containing words and their counts.
    """
    words, counts = zip(*common_words)
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.title('Top 20 Most Common Words in Headlines')
    plt.xticks(rotation=45)
    plt.show()

# Function to generate a word cloud
def generate_word_cloud(word_freq):
    """
    Generates and displays a word cloud from word frequencies.
    
    Args:
    word_freq (Counter): A Counter object containing word frequencies.
    """
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Common Keywords in Headlines')
    plt.show()

# Function to visualize most common bigrams
def visualize_common_bigrams(common_bigrams):
    """
    Visualizes the most common bigrams using a bar plot.
    
    Args:
    common_bigrams (list): A list of tuples containing bigrams and their counts.
    """
    bigrams_words, bigrams_counts = zip(*common_bigrams)
    bigrams_labels = [' '.join(bigram) for bigram in bigrams_words]
    plt.figure(figsize=(10, 6))
    plt.bar(bigrams_labels, bigrams_counts)
    plt.title('Top 20 Most Common Bigrams in Headlines')
    plt.xticks(rotation=45)
    plt.show()

# Main function to process the DataFrame and perform analysis
def analyze_headlines(df):
    """
    Preprocesses the headlines, extracts and visualizes common words and bigrams.
    
    Args:
    df (pd.DataFrame): The DataFrame containing headlines.
    
    Returns:
    None
    """
    # Preprocess the headlines
    df['tokens'] = df['headline'].apply(preprocess_text)
    
    # Extract common words
    common_words = extract_common_words(df['tokens'])
    print("Most Common Words:")
    print(common_words)
    
    # Visualize common words
    visualize_common_words(common_words)
    
    # Generate word cloud
    all_tokens = [token for tokens in df['tokens'] for token in tokens]
    word_freq = Counter(all_tokens)
    generate_word_cloud(word_freq)
    
    # Extract common bigrams
    common_bigrams = extract_common_bigrams(df['tokens'])
    print("Most Common Bigrams:")
    print(common_bigrams)
    
    # Visualize common bigrams
    visualize_common_bigrams(common_bigrams)

