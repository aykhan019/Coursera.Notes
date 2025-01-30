

# Module 5: Clustering
## Clustering: An Introduction
### Overview of Clustering
Clustering is an unsupervised learning technique used to group similar data points into clusters based on their characteristics. This method is commonly applied in various domains to segment data, identify patterns, and make predictions.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9cb01ce9-5e0d-49ef-8f43-c9db38fbc0e0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNV7OBE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCshBA4y1yqQAUcacs68tWDC8Hh8973ApJ6CNboxvkhMAIgcyZf3Rr1GU0cWpx5q6JsvcsVMB2PqjhOiU0wYWO9B30qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWqdf208mkrRzVDxSrcA75oohgCgJkOccgja7RpmoanMXVyfOP58MWtBDwl%2Fv9a5UaQaUYmVy4G4e6o9EgfVMgtP1UXYh4IwoWTkt7ZlACllb9m7BOJtAgBlJrkKaH7CtDmR0Y88EBHfD7us3H6SUPtqt0OUffA8E8kHF5xIBO7gMoiUiZfJdZKAOaoeS86Yf8czDZsRSXSbTH7asHEbfuNC9DZWGH9ieCWsK6wVlHk8wkWMC9tD21M04MOImNXwdufpDsrORYasyxA6zAunwgn%2FYUy4am4exHpo3P2aMp%2FJljxaBOS3aYhDlgLNq1katRQ9%2Fb%2FHLa58%2F4Is2ld9SNslSnFBGm5lYUQF5klYahmnPDDQTRA4bSqlLEpJ0OJJIybaKUYfSY8Vhr9IvIyiQ11S223nZpsFjLYRsQ8E6HYY6J592okenepksJWRrBluKcyjtK%2BseoRWjDf9PAX8DYgRxQPzQKyU31XpQrGM3eca%2BTRSiejMWH1haFSf0tS5LKtG17JYV6GmNkf6zu7rsg%2Bh6hP3RWVhlyvZfULYgb0N%2Bb5jRbyuP9RMYDGjhS9LPuOpVzE4EW1cF%2FUDoNdrEH6YWjkNsipJqhTOJETh9t0MHWuJTuaTzGjhtlIixeE7oNFFmzNoTzTROUBMKbF77wGOqUBfm%2FmB2FeCM9Kz6Zjdgmqszc0JmEEsgv9029CBJuI2nQqCiD54uD3sYyni3z5NATWs1K78wqMutCpjl1KKyETutG%2BnjirrXuIHTOE9%2Fl1RxNoSnExIB0PwYVFrblvqbUVV6T3EOrFvtnaSn9MHmMzU2exN%2B2qCdULagSuB2Udm%2F5BkmNAyzqamcbbrGy9Wp7QBKEzM3hH6NCM%2FTb%2F56EGX2nymnCp&X-Amz-Signature=d6fc4cc51837f1753fe5639efc44984f127fc2b6b9961c02aa8957377122ea99&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ede0dba7-3f63-4051-85fd-51f2f38eeeb5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNV7OBE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCshBA4y1yqQAUcacs68tWDC8Hh8973ApJ6CNboxvkhMAIgcyZf3Rr1GU0cWpx5q6JsvcsVMB2PqjhOiU0wYWO9B30qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWqdf208mkrRzVDxSrcA75oohgCgJkOccgja7RpmoanMXVyfOP58MWtBDwl%2Fv9a5UaQaUYmVy4G4e6o9EgfVMgtP1UXYh4IwoWTkt7ZlACllb9m7BOJtAgBlJrkKaH7CtDmR0Y88EBHfD7us3H6SUPtqt0OUffA8E8kHF5xIBO7gMoiUiZfJdZKAOaoeS86Yf8czDZsRSXSbTH7asHEbfuNC9DZWGH9ieCWsK6wVlHk8wkWMC9tD21M04MOImNXwdufpDsrORYasyxA6zAunwgn%2FYUy4am4exHpo3P2aMp%2FJljxaBOS3aYhDlgLNq1katRQ9%2Fb%2FHLa58%2F4Is2ld9SNslSnFBGm5lYUQF5klYahmnPDDQTRA4bSqlLEpJ0OJJIybaKUYfSY8Vhr9IvIyiQ11S223nZpsFjLYRsQ8E6HYY6J592okenepksJWRrBluKcyjtK%2BseoRWjDf9PAX8DYgRxQPzQKyU31XpQrGM3eca%2BTRSiejMWH1haFSf0tS5LKtG17JYV6GmNkf6zu7rsg%2Bh6hP3RWVhlyvZfULYgb0N%2Bb5jRbyuP9RMYDGjhS9LPuOpVzE4EW1cF%2FUDoNdrEH6YWjkNsipJqhTOJETh9t0MHWuJTuaTzGjhtlIixeE7oNFFmzNoTzTROUBMKbF77wGOqUBfm%2FmB2FeCM9Kz6Zjdgmqszc0JmEEsgv9029CBJuI2nQqCiD54uD3sYyni3z5NATWs1K78wqMutCpjl1KKyETutG%2BnjirrXuIHTOE9%2Fl1RxNoSnExIB0PwYVFrblvqbUVV6T3EOrFvtnaSn9MHmMzU2exN%2B2qCdULagSuB2Udm%2F5BkmNAyzqamcbbrGy9Wp7QBKEzM3hH6NCM%2FTb%2F56EGX2nymnCp&X-Amz-Signature=c785e9a7668470693c34dd974c648a391d9af643f7b681a6811a7d898aefef3b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications of Clustering
1. **Customer Segmentation**:
	- Clustering is widely used for customer segmentation in marketing. It helps businesses to group customers based on demographic or behavioral similarities, allowing for targeted marketing strategies.
	- Example: Segmenting customers into groups such as high-profit low-risk, young educated, and middle-income customers.
2. **Recommendation Systems**:
	- Used to find groups of similar items or users. This information can be used for collaborative filtering to recommend products or content, such as books or movies.
3. **Banking**:
	- Clustering is used to identify normal transaction patterns, detect fraudulent credit card activities, and categorize customers based on loyalty or likelihood to churn.
4. **Insurance**:
	- Helps in fraud detection during claims analysis and evaluating insurance risks for different customer segments.
5. **Publication Media**:
	- Used to auto-categorize and tag news articles for better recommendation systems.
6. **Medicine**:
	- Clustering patients based on similar characteristics to identify effective medical therapies or grouping genes with similar expression patterns.
## Clustering Algorithms
- K-Means
- K-Medians
- Fuzzy c-Means
- Agglomerative
- Divisive
- DBSCAN
### Types of Clustering Algorithms
7. **Partition-based Clustering**:
	- Algorithms such as **K-Means**, **K-Medians**, and **Fuzzy c-Means** produce sphere-like clusters.
	- Efficient for medium to large-sized datasets.
8. **Hierarchical Clustering**:
	- Produces trees of clusters using algorithms like **Agglomerative** and **Divisive**.
	- Best suited for small-sized datasets.
9. **Density-based Clustering**:
	- Creates arbitrary-shaped clusters with algorithms such as **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**.
	- Useful for spatial data or noisy datasets.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23d540d1-3363-46c0-b145-c20928ff781b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNV7OBE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCshBA4y1yqQAUcacs68tWDC8Hh8973ApJ6CNboxvkhMAIgcyZf3Rr1GU0cWpx5q6JsvcsVMB2PqjhOiU0wYWO9B30qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWqdf208mkrRzVDxSrcA75oohgCgJkOccgja7RpmoanMXVyfOP58MWtBDwl%2Fv9a5UaQaUYmVy4G4e6o9EgfVMgtP1UXYh4IwoWTkt7ZlACllb9m7BOJtAgBlJrkKaH7CtDmR0Y88EBHfD7us3H6SUPtqt0OUffA8E8kHF5xIBO7gMoiUiZfJdZKAOaoeS86Yf8czDZsRSXSbTH7asHEbfuNC9DZWGH9ieCWsK6wVlHk8wkWMC9tD21M04MOImNXwdufpDsrORYasyxA6zAunwgn%2FYUy4am4exHpo3P2aMp%2FJljxaBOS3aYhDlgLNq1katRQ9%2Fb%2FHLa58%2F4Is2ld9SNslSnFBGm5lYUQF5klYahmnPDDQTRA4bSqlLEpJ0OJJIybaKUYfSY8Vhr9IvIyiQ11S223nZpsFjLYRsQ8E6HYY6J592okenepksJWRrBluKcyjtK%2BseoRWjDf9PAX8DYgRxQPzQKyU31XpQrGM3eca%2BTRSiejMWH1haFSf0tS5LKtG17JYV6GmNkf6zu7rsg%2Bh6hP3RWVhlyvZfULYgb0N%2Bb5jRbyuP9RMYDGjhS9LPuOpVzE4EW1cF%2FUDoNdrEH6YWjkNsipJqhTOJETh9t0MHWuJTuaTzGjhtlIixeE7oNFFmzNoTzTROUBMKbF77wGOqUBfm%2FmB2FeCM9Kz6Zjdgmqszc0JmEEsgv9029CBJuI2nQqCiD54uD3sYyni3z5NATWs1K78wqMutCpjl1KKyETutG%2BnjirrXuIHTOE9%2Fl1RxNoSnExIB0PwYVFrblvqbUVV6T3EOrFvtnaSn9MHmMzU2exN%2B2qCdULagSuB2Udm%2F5BkmNAyzqamcbbrGy9Wp7QBKEzM3hH6NCM%2FTb%2F56EGX2nymnCp&X-Amz-Signature=0d1ca0d3cd6208b5eeab22b51bfeff3176bbfb122cb66f0d89602745be64e7a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Differences Between Clustering and Classification
- **Clustering**:
	- Unsupervised learning.
	- Groups similar data points into clusters without predefined labels.
- **Classification**:
	- Supervised learning.
	- Predicts categorical labels for data points using labeled training data.
### Purposes of Clustering
10. **Exploratory Data Analysis**: To understand the structure of data.
11. **Summary Generation/Scale Reduction**: To simplify large datasets.
12. **Outlier Detection**: Especially useful for fraud detection or noise removal.
13. **Finding Duplicates**: To identify and remove redundant data points.
14. **Pre-processing**: Used as a preparatory step for other data mining tasks or predictions.
### Conclusion
Clustering is a powerful technique with a wide range of applications across different industries. From customer segmentation to fraud detection, it helps in identifying patterns and making data-driven decisions. Various clustering algorithms can be chosen based on the dataset's characteristics and the specific application in mind.
___
## K-Means Clustering
### Introduction
K-Means Clustering is an unsupervised learning algorithm used for partitioning a dataset into distinct groups or clusters based on similarity. It is widely used for customer segmentation and other applications.
### Key Concepts
- **Customer Segmentation**: Dividing a customer base into groups with similar characteristics.
- **Partitioning Clustering**: K-Means is a type of partitioning clustering that divides data into K non-overlapping clusters.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8af3f76b-b350-4668-99db-ffde6afd7a48/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNV7OBE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCshBA4y1yqQAUcacs68tWDC8Hh8973ApJ6CNboxvkhMAIgcyZf3Rr1GU0cWpx5q6JsvcsVMB2PqjhOiU0wYWO9B30qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWqdf208mkrRzVDxSrcA75oohgCgJkOccgja7RpmoanMXVyfOP58MWtBDwl%2Fv9a5UaQaUYmVy4G4e6o9EgfVMgtP1UXYh4IwoWTkt7ZlACllb9m7BOJtAgBlJrkKaH7CtDmR0Y88EBHfD7us3H6SUPtqt0OUffA8E8kHF5xIBO7gMoiUiZfJdZKAOaoeS86Yf8czDZsRSXSbTH7asHEbfuNC9DZWGH9ieCWsK6wVlHk8wkWMC9tD21M04MOImNXwdufpDsrORYasyxA6zAunwgn%2FYUy4am4exHpo3P2aMp%2FJljxaBOS3aYhDlgLNq1katRQ9%2Fb%2FHLa58%2F4Is2ld9SNslSnFBGm5lYUQF5klYahmnPDDQTRA4bSqlLEpJ0OJJIybaKUYfSY8Vhr9IvIyiQ11S223nZpsFjLYRsQ8E6HYY6J592okenepksJWRrBluKcyjtK%2BseoRWjDf9PAX8DYgRxQPzQKyU31XpQrGM3eca%2BTRSiejMWH1haFSf0tS5LKtG17JYV6GmNkf6zu7rsg%2Bh6hP3RWVhlyvZfULYgb0N%2Bb5jRbyuP9RMYDGjhS9LPuOpVzE4EW1cF%2FUDoNdrEH6YWjkNsipJqhTOJETh9t0MHWuJTuaTzGjhtlIixeE7oNFFmzNoTzTROUBMKbF77wGOqUBfm%2FmB2FeCM9Kz6Zjdgmqszc0JmEEsgv9029CBJuI2nQqCiD54uD3sYyni3z5NATWs1K78wqMutCpjl1KKyETutG%2BnjirrXuIHTOE9%2Fl1RxNoSnExIB0PwYVFrblvqbUVV6T3EOrFvtnaSn9MHmMzU2exN%2B2qCdULagSuB2Udm%2F5BkmNAyzqamcbbrGy9Wp7QBKEzM3hH6NCM%2FTb%2F56EGX2nymnCp&X-Amz-Signature=bf9308b90227fc9512856c8e1750608326b0cfc394c7e5accf1f20987d187e01&X-Amz-SignedHeaders=host&x-id=GetObject)
### Steps in K-Means Clustering
15. **Initialization**
	- Randomly select K initial centroids from the dataset or create K random points as centroids.
16. **Assignment**
	- Assign each data point to the nearest centroid based on a distance metric (e.g., Euclidean distance).
	- Create a distance matrix where each row represents the distance of a data point from each centroid.
17. **Update**
	- Recalculate the centroids by taking the mean of all data points assigned to each centroid.
18. **Iteration**
	- Repeat the assignment and update steps until the centroids no longer move or the changes are minimal.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/16d20e8e-68c0-4ad6-83fa-24ee550846a6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNV7OBE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCshBA4y1yqQAUcacs68tWDC8Hh8973ApJ6CNboxvkhMAIgcyZf3Rr1GU0cWpx5q6JsvcsVMB2PqjhOiU0wYWO9B30qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWqdf208mkrRzVDxSrcA75oohgCgJkOccgja7RpmoanMXVyfOP58MWtBDwl%2Fv9a5UaQaUYmVy4G4e6o9EgfVMgtP1UXYh4IwoWTkt7ZlACllb9m7BOJtAgBlJrkKaH7CtDmR0Y88EBHfD7us3H6SUPtqt0OUffA8E8kHF5xIBO7gMoiUiZfJdZKAOaoeS86Yf8czDZsRSXSbTH7asHEbfuNC9DZWGH9ieCWsK6wVlHk8wkWMC9tD21M04MOImNXwdufpDsrORYasyxA6zAunwgn%2FYUy4am4exHpo3P2aMp%2FJljxaBOS3aYhDlgLNq1katRQ9%2Fb%2FHLa58%2F4Is2ld9SNslSnFBGm5lYUQF5klYahmnPDDQTRA4bSqlLEpJ0OJJIybaKUYfSY8Vhr9IvIyiQ11S223nZpsFjLYRsQ8E6HYY6J592okenepksJWRrBluKcyjtK%2BseoRWjDf9PAX8DYgRxQPzQKyU31XpQrGM3eca%2BTRSiejMWH1haFSf0tS5LKtG17JYV6GmNkf6zu7rsg%2Bh6hP3RWVhlyvZfULYgb0N%2Bb5jRbyuP9RMYDGjhS9LPuOpVzE4EW1cF%2FUDoNdrEH6YWjkNsipJqhTOJETh9t0MHWuJTuaTzGjhtlIixeE7oNFFmzNoTzTROUBMKbF77wGOqUBfm%2FmB2FeCM9Kz6Zjdgmqszc0JmEEsgv9029CBJuI2nQqCiD54uD3sYyni3z5NATWs1K78wqMutCpjl1KKyETutG%2BnjirrXuIHTOE9%2Fl1RxNoSnExIB0PwYVFrblvqbUVV6T3EOrFvtnaSn9MHmMzU2exN%2B2qCdULagSuB2Udm%2F5BkmNAyzqamcbbrGy9Wp7QBKEzM3hH6NCM%2FTb%2F56EGX2nymnCp&X-Amz-Signature=45a326298d4b1e3ab48f25b0cb6fa0842a55c18b136431db2342c0342ab34bfc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Distance Metrics
- **Euclidean Distance**: Commonly used to measure the distance between data points.
- Other metrics: Cosine similarity, Manhattan distance, Minkowski distance, etc., depending on the data type and domain.
### Convergence
- **Heuristic Algorithm**: K-Means converges to a local optimum rather than a global optimum.
- **Multiple Runs**: To avoid local optima, the algorithm is often run multiple times with different initial centroids.
### Applications
- Customer segmentation in marketing.
- Identifying buying patterns in retail.
- Fraud detection in banking.
- Categorizing news articles in media.
- Characterizing patient behavior in medicine.
### Code Example
Here's a basic example of how to implement K-Means Clustering using Python's `scikit-learn` library:
```python
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Sample data
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Income': [40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000]
}
df = pd.DataFrame(data)

# Standardize the data
scaler = StandardScaler()
scaled_df = scaler.fit_transform(df)

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(scaled_df)
df['Cluster'] = kmeans.labels_

# Plotting
plt.scatter(df['Age'], df['Income'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('K-Means Clustering')
plt.show()
```
**Output:**
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/73a2c105-2ca5-46a7-974c-ec918cf62c91/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNV7OBE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCshBA4y1yqQAUcacs68tWDC8Hh8973ApJ6CNboxvkhMAIgcyZf3Rr1GU0cWpx5q6JsvcsVMB2PqjhOiU0wYWO9B30qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWqdf208mkrRzVDxSrcA75oohgCgJkOccgja7RpmoanMXVyfOP58MWtBDwl%2Fv9a5UaQaUYmVy4G4e6o9EgfVMgtP1UXYh4IwoWTkt7ZlACllb9m7BOJtAgBlJrkKaH7CtDmR0Y88EBHfD7us3H6SUPtqt0OUffA8E8kHF5xIBO7gMoiUiZfJdZKAOaoeS86Yf8czDZsRSXSbTH7asHEbfuNC9DZWGH9ieCWsK6wVlHk8wkWMC9tD21M04MOImNXwdufpDsrORYasyxA6zAunwgn%2FYUy4am4exHpo3P2aMp%2FJljxaBOS3aYhDlgLNq1katRQ9%2Fb%2FHLa58%2F4Is2ld9SNslSnFBGm5lYUQF5klYahmnPDDQTRA4bSqlLEpJ0OJJIybaKUYfSY8Vhr9IvIyiQ11S223nZpsFjLYRsQ8E6HYY6J592okenepksJWRrBluKcyjtK%2BseoRWjDf9PAX8DYgRxQPzQKyU31XpQrGM3eca%2BTRSiejMWH1haFSf0tS5LKtG17JYV6GmNkf6zu7rsg%2Bh6hP3RWVhlyvZfULYgb0N%2Bb5jRbyuP9RMYDGjhS9LPuOpVzE4EW1cF%2FUDoNdrEH6YWjkNsipJqhTOJETh9t0MHWuJTuaTzGjhtlIixeE7oNFFmzNoTzTROUBMKbF77wGOqUBfm%2FmB2FeCM9Kz6Zjdgmqszc0JmEEsgv9029CBJuI2nQqCiD54uD3sYyni3z5NATWs1K78wqMutCpjl1KKyETutG%2BnjirrXuIHTOE9%2Fl1RxNoSnExIB0PwYVFrblvqbUVV6T3EOrFvtnaSn9MHmMzU2exN%2B2qCdULagSuB2Udm%2F5BkmNAyzqamcbbrGy9Wp7QBKEzM3hH6NCM%2FTb%2F56EGX2nymnCp&X-Amz-Signature=d20887ed7f859297e3e76f319df8219cda75c753dc61987d01e409294864d827&X-Amz-SignedHeaders=host&x-id=GetObject)
### Explanation
19. **Import Libraries**: Necessary libraries are imported.
20. **Sample Data**: A sample dataset with 'Age' and 'Income' is created.
21. **Standardize Data**: Features are standardized using `StandardScaler`.
22. **Fit K-Means Model**: The K-Means model is created with 3 clusters and fitted to the standardized data.
23. **Plot Results**: A scatter plot visualizes the clustering result.
### Conclusion
K-Means Clustering is a powerful tool for discovering groups within data, but its performance and results can be sensitive to the initial conditions. It is crucial to understand the dataset and choose the right distance metrics for effective clustering.
___
## K-Means Clustering: Characteristics and Accuracy
### Introduction
K-Means clustering is a partition-based clustering algorithm used to partition a dataset into K non-overlapping subsets or clusters. It works in an unsupervised manner, grouping data based on the similarity of samples. K-Means aims to minimize the intra-cluster variance while maximizing the inter-cluster distances.
### Algorithm Overview
24. **Initialization**:
	- Randomly place K centroids, one for each cluster.
25. **Assignment**:
	- Assign each data point to the nearest centroid based on a distance metric (typically Euclidean distance).
26. **Update**:
	- Recalculate the centroids by computing the mean of all points assigned to each cluster.
27. **Repeat**:
	- Repeat the assignment and update steps until the centroids no longer move significantly.
### Evaluating K-Means Clustering
Evaluating K-Means clustering is challenging, especially since it is an unsupervised learning algorithm. Common methods to assess clustering quality include:
- **Within-Cluster Sum of Squares (WCSS)**: Measures the average distance between data points and their cluster centroids. Lower values indicate better clustering.
- **Elbow Method**: Helps determine the optimal number of clusters (K). Plot WCSS against the number of clusters and look for the "elbow" point where the rate of decrease **sharply shifts***.*
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7d3cdfd2-3a59-4bf7-8d34-4b4314e49abd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNV7OBE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCshBA4y1yqQAUcacs68tWDC8Hh8973ApJ6CNboxvkhMAIgcyZf3Rr1GU0cWpx5q6JsvcsVMB2PqjhOiU0wYWO9B30qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWqdf208mkrRzVDxSrcA75oohgCgJkOccgja7RpmoanMXVyfOP58MWtBDwl%2Fv9a5UaQaUYmVy4G4e6o9EgfVMgtP1UXYh4IwoWTkt7ZlACllb9m7BOJtAgBlJrkKaH7CtDmR0Y88EBHfD7us3H6SUPtqt0OUffA8E8kHF5xIBO7gMoiUiZfJdZKAOaoeS86Yf8czDZsRSXSbTH7asHEbfuNC9DZWGH9ieCWsK6wVlHk8wkWMC9tD21M04MOImNXwdufpDsrORYasyxA6zAunwgn%2FYUy4am4exHpo3P2aMp%2FJljxaBOS3aYhDlgLNq1katRQ9%2Fb%2FHLa58%2F4Is2ld9SNslSnFBGm5lYUQF5klYahmnPDDQTRA4bSqlLEpJ0OJJIybaKUYfSY8Vhr9IvIyiQ11S223nZpsFjLYRsQ8E6HYY6J592okenepksJWRrBluKcyjtK%2BseoRWjDf9PAX8DYgRxQPzQKyU31XpQrGM3eca%2BTRSiejMWH1haFSf0tS5LKtG17JYV6GmNkf6zu7rsg%2Bh6hP3RWVhlyvZfULYgb0N%2Bb5jRbyuP9RMYDGjhS9LPuOpVzE4EW1cF%2FUDoNdrEH6YWjkNsipJqhTOJETh9t0MHWuJTuaTzGjhtlIixeE7oNFFmzNoTzTROUBMKbF77wGOqUBfm%2FmB2FeCM9Kz6Zjdgmqszc0JmEEsgv9029CBJuI2nQqCiD54uD3sYyni3z5NATWs1K78wqMutCpjl1KKyETutG%2BnjirrXuIHTOE9%2Fl1RxNoSnExIB0PwYVFrblvqbUVV6T3EOrFvtnaSn9MHmMzU2exN%2B2qCdULagSuB2Udm%2F5BkmNAyzqamcbbrGy9Wp7QBKEzM3hH6NCM%2FTb%2F56EGX2nymnCp&X-Amz-Signature=2304e709f35611a5ed9d82bedf1612f668274deedd2ca30d4ec735865bafef1e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example Code
Below is a code example demonstrating K-Means clustering and the elbow method to find the optimal number of clusters:
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Fit K-Means model
def find_optimal_k(X, max_k=10):
    wcss = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    # Plot the elbow method result
    plt.plot(range(1, max_k + 1), wcss)
    plt.title('Elbow Method for Optimal K')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

find_optimal_k(X)

# Apply K-Means with the optimal number of clusters
optimal_k = 4  # Assume the optimal K is found to be 4 from the elbow plot
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
plt.title('Clusters and Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```
**Outputs:**
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74024f1a-9e67-4a06-856e-ff0920d20ba0/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNV7OBE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCshBA4y1yqQAUcacs68tWDC8Hh8973ApJ6CNboxvkhMAIgcyZf3Rr1GU0cWpx5q6JsvcsVMB2PqjhOiU0wYWO9B30qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWqdf208mkrRzVDxSrcA75oohgCgJkOccgja7RpmoanMXVyfOP58MWtBDwl%2Fv9a5UaQaUYmVy4G4e6o9EgfVMgtP1UXYh4IwoWTkt7ZlACllb9m7BOJtAgBlJrkKaH7CtDmR0Y88EBHfD7us3H6SUPtqt0OUffA8E8kHF5xIBO7gMoiUiZfJdZKAOaoeS86Yf8czDZsRSXSbTH7asHEbfuNC9DZWGH9ieCWsK6wVlHk8wkWMC9tD21M04MOImNXwdufpDsrORYasyxA6zAunwgn%2FYUy4am4exHpo3P2aMp%2FJljxaBOS3aYhDlgLNq1katRQ9%2Fb%2FHLa58%2F4Is2ld9SNslSnFBGm5lYUQF5klYahmnPDDQTRA4bSqlLEpJ0OJJIybaKUYfSY8Vhr9IvIyiQ11S223nZpsFjLYRsQ8E6HYY6J592okenepksJWRrBluKcyjtK%2BseoRWjDf9PAX8DYgRxQPzQKyU31XpQrGM3eca%2BTRSiejMWH1haFSf0tS5LKtG17JYV6GmNkf6zu7rsg%2Bh6hP3RWVhlyvZfULYgb0N%2Bb5jRbyuP9RMYDGjhS9LPuOpVzE4EW1cF%2FUDoNdrEH6YWjkNsipJqhTOJETh9t0MHWuJTuaTzGjhtlIixeE7oNFFmzNoTzTROUBMKbF77wGOqUBfm%2FmB2FeCM9Kz6Zjdgmqszc0JmEEsgv9029CBJuI2nQqCiD54uD3sYyni3z5NATWs1K78wqMutCpjl1KKyETutG%2BnjirrXuIHTOE9%2Fl1RxNoSnExIB0PwYVFrblvqbUVV6T3EOrFvtnaSn9MHmMzU2exN%2B2qCdULagSuB2Udm%2F5BkmNAyzqamcbbrGy9Wp7QBKEzM3hH6NCM%2FTb%2F56EGX2nymnCp&X-Amz-Signature=aee273f164b894cf9f02cb6fe6657e3b1d1146ba12ff055ac57088dd968cb206&X-Amz-SignedHeaders=host&x-id=GetObject)
![Figure2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/14af08ae-a84c-4391-95ac-9cee37c62973/Figure2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFNV7OBE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCshBA4y1yqQAUcacs68tWDC8Hh8973ApJ6CNboxvkhMAIgcyZf3Rr1GU0cWpx5q6JsvcsVMB2PqjhOiU0wYWO9B30qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWqdf208mkrRzVDxSrcA75oohgCgJkOccgja7RpmoanMXVyfOP58MWtBDwl%2Fv9a5UaQaUYmVy4G4e6o9EgfVMgtP1UXYh4IwoWTkt7ZlACllb9m7BOJtAgBlJrkKaH7CtDmR0Y88EBHfD7us3H6SUPtqt0OUffA8E8kHF5xIBO7gMoiUiZfJdZKAOaoeS86Yf8czDZsRSXSbTH7asHEbfuNC9DZWGH9ieCWsK6wVlHk8wkWMC9tD21M04MOImNXwdufpDsrORYasyxA6zAunwgn%2FYUy4am4exHpo3P2aMp%2FJljxaBOS3aYhDlgLNq1katRQ9%2Fb%2FHLa58%2F4Is2ld9SNslSnFBGm5lYUQF5klYahmnPDDQTRA4bSqlLEpJ0OJJIybaKUYfSY8Vhr9IvIyiQ11S223nZpsFjLYRsQ8E6HYY6J592okenepksJWRrBluKcyjtK%2BseoRWjDf9PAX8DYgRxQPzQKyU31XpQrGM3eca%2BTRSiejMWH1haFSf0tS5LKtG17JYV6GmNkf6zu7rsg%2Bh6hP3RWVhlyvZfULYgb0N%2Bb5jRbyuP9RMYDGjhS9LPuOpVzE4EW1cF%2FUDoNdrEH6YWjkNsipJqhTOJETh9t0MHWuJTuaTzGjhtlIixeE7oNFFmzNoTzTROUBMKbF77wGOqUBfm%2FmB2FeCM9Kz6Zjdgmqszc0JmEEsgv9029CBJuI2nQqCiD54uD3sYyni3z5NATWs1K78wqMutCpjl1KKyETutG%2BnjirrXuIHTOE9%2Fl1RxNoSnExIB0PwYVFrblvqbUVV6T3EOrFvtnaSn9MHmMzU2exN%2B2qCdULagSuB2Udm%2F5BkmNAyzqamcbbrGy9Wp7QBKEzM3hH6NCM%2FTb%2F56EGX2nymnCp&X-Amz-Signature=0184525b29687d70bf3178ee938b4df0d07e59680a5a2fcb71726c70a8d4fe3b&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Characteristics of K-Means
- **Partition-Based**: Divides data into K clusters based on similarity.
- **Efficiency**: Relatively efficient on medium and large-sized datasets.
- **Cluster Shape**: Produces spherical clusters as it groups data around centroids.
- **Pre-Specified K**: Requires the number of clusters (K) to be specified beforehand, which can be challenging.
### Conclusion
K-Means clustering is a widely-used algorithm for grouping data into clusters based on feature similarity. The algorithm's effectiveness is often evaluated using metrics such as WCSS and the elbow method to determine the optimal number of clusters.