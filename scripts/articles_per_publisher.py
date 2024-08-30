import pandas as pd
import matplotlib.pyplot as plt

def count_articles_per_publisher(df):
   
    # Count articles per publisher
    publisher_counts = df['publisher'].value_counts()

    # Identify top publishers
    print("Top Publishers:")
    print(publisher_counts.head(10))

    # Visualize top publishers
    top_publishers = publisher_counts.head(10)
    top_publishers.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title("Top 10 Publishers by Article Count")
    plt.xlabel("Publisher")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return publisher_counts
