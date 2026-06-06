import pandas as pd

def create_rfm(df):

    rfm = pd.DataFrame()

    rfm['CustomerID'] = df['CustomerID']

    rfm['Recency'] = 100 - df['Spending Score (1-100)']

    rfm['Frequency'] = df['Spending Score (1-100)']

    rfm['Monetary'] = df['Annual Income (k$)']

    return rfm