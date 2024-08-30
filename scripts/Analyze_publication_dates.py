import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_publication_dates(df):
    """
    Analyze publication dates to identify trends over time, such as increased news frequency on particular days.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the dataset with a 'date' column.
    
    Returns:
    pd.Series: Daily counts of articles published.
    """
    try:
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'], format="ISO8601")

        # Extract date components
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day
        df['hour'] = df['date'].dt.hour

        # Count articles per day
        daily_counts = df['date'].dt.date.value_counts().sort_index()
        monthly_counts = df['date'].dt.to_period('M').value_counts().sort_index()

        # Print basic statistics
        print("Daily Publication Counts:")
        print(daily_counts.head(10))
        
        # Visualization: Daily articles count
        plt.figure(figsize=(12, 6))
        daily_counts.plot(kind='line', marker='o', color='skyblue')
        plt.title("Daily Publication Counts Over Time")
        plt.xlabel("Date")
        plt.ylabel("Number of Articles")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Visualization: Monthly articles count
        plt.figure(figsize=(12, 6))
        monthly_counts.plot(kind='bar', color='lightgreen')
        plt.title("Monthly Publication Counts")
        plt.xlabel("Month")
        plt.ylabel("Number of Articles")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return daily_counts

    except Exception as e:
        print(f"Error analyzing publication dates: {e}")
        return None
