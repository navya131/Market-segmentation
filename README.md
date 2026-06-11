# Market & Customer Segmentation Using Machine Learning

## Project Overview

Market & Customer Segmentation is a Machine Learning project that helps businesses identify different groups of customers based on their purchasing behavior and demographic information. By segmenting customers into meaningful clusters, organizations can design targeted marketing strategies, improve customer engagement, and increase business revenue.

This project uses the Mall Customers Dataset and applies data preprocessing, RFM (Recency, Frequency, Monetary) analysis, Principal Component Analysis (PCA), and K-Means Clustering to discover customer segments.

---

## Objectives

* Analyze customer purchasing behavior.
* Perform customer segmentation using Machine Learning.
* Apply RFM-based customer profiling.
* Reduce feature dimensions using PCA.
* Visualize customer clusters.
* Generate cluster-wise business insights.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

---

## Dataset Information

The dataset contains customer demographic and spending information.

### Features

| Feature                | Description                                  |
| ---------------------- | -------------------------------------------- |
| CustomerID             | Unique customer identifier                   |
| Gender                 | Customer gender                              |
| Age                    | Customer age                                 |
| Annual Income (k$)     | Annual income in thousands of dollars        |
| Spending Score (1-100) | Spending behavior score assigned by the mall |

---

## Project Workflow

### 1. Data Preprocessing

* Load dataset
* Handle categorical features
* Encode gender values
* Standardize numerical features

### 2. RFM Analysis

* Recency
* Frequency
* Monetary Value

### 3. Principal Component Analysis (PCA)

* Reduce dimensions
* Improve visualization
* Retain important information

### 4. K-Means Clustering

* Determine optimal number of clusters
* Group customers with similar characteristics

### 5. Visualization

* Elbow Method Graph
* Customer Cluster Plot
* PCA Cluster Visualization

### 6. Cluster Profiling

* Generate cluster-wise statistical report
* Understand customer behavior patterns

---

## Project Structure

```text
Market_Customer_Segmentation/
│
├── dataset/
│   └── Mall_Customers.csv
│
├── outputs/
│   ├── elbow_method.png
│   ├── customer_clusters.png
│   ├── pca_clusters.png
│   └── cluster_report.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── rfm_analysis.py
│   ├── pca_analysis.py
│   ├── clustering.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Market_Customer_Segmentation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Execute the following command:

```bash
python main.py
```

---

## Generated Outputs

After successful execution, the following files are generated inside the outputs folder:

### 1. Elbow Method Graph

Used to determine the optimal number of clusters.

### 2. Customer Clusters Visualization

Shows customer segments based on spending score and annual income.

### 3. PCA Cluster Visualization

Displays clusters in a reduced two-dimensional space.

### 4. Cluster Report

Contains statistical information for each customer segment.

---

## Sample Console Output

```text
==================================================

Dataset Loaded Successfully

RFM Analysis Completed

PCA Applied Successfully

Elbow Method Graph Saved

K-Means Clustering Completed

Cluster Report Generated

Graphs Generated Successfully

Project Executed Successfully
```

---

## Applications

* Customer Behavior Analysis
* Targeted Marketing Campaigns
* Customer Retention Strategies
* Personalized Recommendations
* Business Intelligence
* Retail Analytics

---

## Future Enhancements

* Interactive Dashboard using Streamlit
* Real-Time Customer Segmentation
* Advanced Clustering Algorithms
* Customer Lifetime Value Prediction
* Marketing Recommendation System

---

## Conclusion

This project demonstrates how Machine Learning techniques such as PCA and K-Means Clustering can be used to segment customers effectively. The generated customer groups help businesses understand customer behavior and make data-driven marketing decisions.
