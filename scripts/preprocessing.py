from matplotlib.pylab import f


with open("Data/stopwords.txt", "r") as f:
    stopwords_list = f.read()
    # print(stopwords_list)
# stopwords_list = f.read("Data/stopwords.txt").splitlines()




def preprocess_text(text, stopwords_list):
   
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords_list]
    preprocessed_text = ' '.join(filtered_words)

    return preprocessed_text

def preprocess(df, column):
    n_column = "preprocessed_" + column
    df[n_column] = df[column].apply(lambda x: preprocess_text(x, stopwords_list) )

    return df 