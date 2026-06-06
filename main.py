from src.data_preprocessing import preprocess_data
from src.rfm_analysis import create_rfm
from src.pca_analysis import apply_pca
from src.clustering import find_clusters
from src.visualization import elbow_method, customer_clusters, pca_clusters

def main():

    print("=" * 50)

    file_path = "dataset/Mall_Customers.csv"

    df, scaled_data = preprocess_data(file_path)

    print("\nDataset Loaded Successfully")
    print(df.head())

    rfm = create_rfm(df)
    print("\nRFM Analysis Completed")

    pca_data = apply_pca(scaled_data)
    print("\nPCA Applied Successfully")

    elbow_method(scaled_data)
    print("\nElbow Method Graph Saved")

    labels, model = find_clusters(scaled_data, k=5)
    print("\nK-Means Clustering Completed")

    df['Cluster'] = labels

    customer_clusters(df)
    pca_clusters(pca_data, labels)

    report = df.groupby('Cluster').mean(numeric_only=True)

    report.to_csv("outputs/cluster_report.csv")

    print("\nCluster Report Generated")

    print("\nGraphs Generated Successfully")

    print("\nCluster Report:")
    print(report)

    print("\nProject Executed Successfully")

if __name__ == "__main__":
    main()