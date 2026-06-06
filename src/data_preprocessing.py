import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(filepath):
    df = pd.read_csv(filepath)

    encoder = LabelEncoder()
    df['Gender'] = encoder.fit_transform(df['Gender'])

    features = df[['Gender',
                   'Age',
                   'Annual Income (k$)',
                   'Spending Score (1-100)']]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    return df, scaled_features