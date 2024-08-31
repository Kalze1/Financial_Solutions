import pandas as pd



def file_path(name):
    #select path for the file to load
    if name == "AAPL":
        return "Data/yfinance_data/AAPL_historical_data.csv"
    elif name == "AMZN":
        return "Data/yfinance_data/AMZN_historical_data.csv"
    elif name == "GOOG":
        return "Data/yfinance_data/GOOG_historical_data.csv"
    elif name == "META":
        return "Data/yfinance_data/META_historical_data.csv"
    elif name == "MSFT":
        return "Data/yfinance_data/MSFT_historical_data.csv"
    elif name == "NVDA":
        return "Data/yfinance_data/NVDA_historical_data.csv"
    elif name == "TSLA":
        return "Data/yfinance_data/TSLA_historical_data.csv"
    elif name == "News":
        return "Data/raw_analyst_ratings.csv"
    else :
         return -1 
    
    

def load_data(name):
    path = file_path(name)
    df = pd.read_csv(path, parse_dates=['date'])
    
    return df
    
    
def format_date(df, format):
    df['date'] = pd.to_datetime(df['date'].str.split().str[0])  
    df['date'] = df['date'].dt.strftime(format)

    return df 