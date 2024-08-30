import pandas as pd
import matplotlib.pyplot as plt

def analyze_headline_lengths(df):
   
    # Calculate headline lengths
    df['headline_length'] = df['headline'].apply(len)
    
    # Calculate basic statistics
    stats = df['headline_length'].describe()
    print("Headline Length Statistics:")
    print(stats)
    
    # Visualize the data
    plt.figure(figsize=(10, 6))

    # Histogram of headline lengths
    plt.subplot(1, 2, 1)
    plt.hist(df['headline_length'], bins=20, color='blue', edgecolor='black')
    plt.title('Distribution of Headline Lengths')
    plt.xlabel('Headline Length')
    plt.ylabel('Frequency')

    # Boxplot of headline lengths
    plt.subplot(1, 2, 2)
    plt.boxplot(df['headline_length'], vert=False)
    plt.title('Boxplot of Headline Lengths')
    plt.xlabel('Headline Length')

    plt.tight_layout()
    plt.show()

    return stats
