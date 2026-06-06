import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def elbow_method(data):

    wcss = []

    for i in range(1,11):
        model = KMeans(
            n_clusters=i,
            random_state=42,
            n_init=10
        )

        model.fit(data)

        wcss.append(model.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11), wcss, marker='o')
    plt.title("Elbow Method")
    plt.xlabel("Clusters")
    plt.ylabel("WCSS")

    plt.savefig("outputs/elbow_method.png")
    plt.close()


def customer_clusters(df):

    plt.figure(figsize=(8,6))

    plt.scatter(
        df['Annual Income (k$)'],
        df['Spending Score (1-100)'],
        c=df['Cluster']
    )

    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segments")

    plt.savefig("outputs/customer_clusters.png")
    plt.close()


def pca_clusters(pca_data, labels):

    plt.figure(figsize=(8,6))

    plt.scatter(
        pca_data[:,0],
        pca_data[:,1],
        c=labels
    )

    plt.xlabel("PCA1")
    plt.ylabel("PCA2")
    plt.title("PCA Cluster Visualization")

    plt.savefig("outputs/pca_clusters.png")
    plt.close()