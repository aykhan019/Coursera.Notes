

# Module 5: Clustering
## Clustering: An Introduction
### Overview of Clustering
Clustering is an unsupervised learning technique used to group similar data points into clusters based on their characteristics. This method is commonly applied in various domains to segment data, identify patterns, and make predictions.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9cb01ce9-5e0d-49ef-8f43-c9db38fbc0e0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWLA3BV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIF0mpRs4gnuD1BaMu84MAFazYU2auuxrZBidqWd32OO%2FAiEA4Y85fND80kU081B4TVXJx9QWPo36idxfYXqnBcU%2BHMgq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFSYPoDLwDPuFyKjGyrcA8%2FbwQzGqeq7aO%2BRqvJtqAkUgbtRvf9wyajBE5yxJYalzD6i8U9ARuneeTOp%2FfX0p0%2BU3Qv0Qx%2BtyoUEM2P3Es%2BF1cexFZHRff%2FGbFH8p4xipWHnw0QqnAxeROYjoo2tF9E4Zt98qq3TZQ18BS%2BXVHo9sKAkm6sXgEo%2B6CPakDB%2FlwAd6D0wxo5SsoBT7Ykz0h5hxWvc7Ko6VrWXvy5t67f53ZX04EZepY%2BiXtwSM4Fxz7njIyShlnxwWWjfMSLKmSpo2YAeJfhaPphER05U%2FWIOcT3pHXYNWd3C1eImvxvkkfD%2B9DBsOwclGr8cvGVwsiRP4y63Pxms9%2Ffv1SLtstTNaZGvxxe5%2FEp0EfwfYvz578xW6dFkJD%2FNZ8ZbXcFrrONWnw%2FNQdSmDtQWPomPSvV3cqcXeKVOAwkwLCWvppA0l%2F%2BFD2jsvshm2oR5e1Xrg43F%2FpF9drZzRXQKeNBToFw2rVMXKY660y613LhLDhR7ocvVrLnYADHnKqmAAgQ5FNk9p1jjszRl3RNv7V81XpkKMBchwLWRvhYhGvLVWgtyI9iV1q2K1kxkXTrdamLTMXN8Es5Tk26dEUNOOVJ0uAcXVE%2FitAevgbzCZZi3fMoOSwwQmnQ5%2BaZUnTBqMNL9lL0GOqUBjWJ6VFfTvm2GXVRMUMOY65Fs97Fql4iS89PIQ7ebrkWLGZdgmvXNVGBUhe5oF3DgNNL%2F7QnxGxLe7HOkYiaZPmWG19qbZ44hpQI4XglaWwbxK23O9sy7eV58JQkYkSfjuVWHhOBN2UZwjZoLuUiiVUk5FvceleILFHoQ7PA%2FZAK24e2P1Y9OE4a7mhQ%2F6FrPfZFRVwDieh51Q%2Fus%2FxtK1ErYIMIl&X-Amz-Signature=84a43d7a53e151b30ad2f18e111ce46c1f877c84ed2a058ee3a27561f65d9dc2&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ede0dba7-3f63-4051-85fd-51f2f38eeeb5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWLA3BV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIF0mpRs4gnuD1BaMu84MAFazYU2auuxrZBidqWd32OO%2FAiEA4Y85fND80kU081B4TVXJx9QWPo36idxfYXqnBcU%2BHMgq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFSYPoDLwDPuFyKjGyrcA8%2FbwQzGqeq7aO%2BRqvJtqAkUgbtRvf9wyajBE5yxJYalzD6i8U9ARuneeTOp%2FfX0p0%2BU3Qv0Qx%2BtyoUEM2P3Es%2BF1cexFZHRff%2FGbFH8p4xipWHnw0QqnAxeROYjoo2tF9E4Zt98qq3TZQ18BS%2BXVHo9sKAkm6sXgEo%2B6CPakDB%2FlwAd6D0wxo5SsoBT7Ykz0h5hxWvc7Ko6VrWXvy5t67f53ZX04EZepY%2BiXtwSM4Fxz7njIyShlnxwWWjfMSLKmSpo2YAeJfhaPphER05U%2FWIOcT3pHXYNWd3C1eImvxvkkfD%2B9DBsOwclGr8cvGVwsiRP4y63Pxms9%2Ffv1SLtstTNaZGvxxe5%2FEp0EfwfYvz578xW6dFkJD%2FNZ8ZbXcFrrONWnw%2FNQdSmDtQWPomPSvV3cqcXeKVOAwkwLCWvppA0l%2F%2BFD2jsvshm2oR5e1Xrg43F%2FpF9drZzRXQKeNBToFw2rVMXKY660y613LhLDhR7ocvVrLnYADHnKqmAAgQ5FNk9p1jjszRl3RNv7V81XpkKMBchwLWRvhYhGvLVWgtyI9iV1q2K1kxkXTrdamLTMXN8Es5Tk26dEUNOOVJ0uAcXVE%2FitAevgbzCZZi3fMoOSwwQmnQ5%2BaZUnTBqMNL9lL0GOqUBjWJ6VFfTvm2GXVRMUMOY65Fs97Fql4iS89PIQ7ebrkWLGZdgmvXNVGBUhe5oF3DgNNL%2F7QnxGxLe7HOkYiaZPmWG19qbZ44hpQI4XglaWwbxK23O9sy7eV58JQkYkSfjuVWHhOBN2UZwjZoLuUiiVUk5FvceleILFHoQ7PA%2FZAK24e2P1Y9OE4a7mhQ%2F6FrPfZFRVwDieh51Q%2Fus%2FxtK1ErYIMIl&X-Amz-Signature=7ef86f334da4d3e723ac2c5422eeff39b0d1cc43192e4034cd68ac0ecfc88452&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23d540d1-3363-46c0-b145-c20928ff781b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWLA3BV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIF0mpRs4gnuD1BaMu84MAFazYU2auuxrZBidqWd32OO%2FAiEA4Y85fND80kU081B4TVXJx9QWPo36idxfYXqnBcU%2BHMgq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFSYPoDLwDPuFyKjGyrcA8%2FbwQzGqeq7aO%2BRqvJtqAkUgbtRvf9wyajBE5yxJYalzD6i8U9ARuneeTOp%2FfX0p0%2BU3Qv0Qx%2BtyoUEM2P3Es%2BF1cexFZHRff%2FGbFH8p4xipWHnw0QqnAxeROYjoo2tF9E4Zt98qq3TZQ18BS%2BXVHo9sKAkm6sXgEo%2B6CPakDB%2FlwAd6D0wxo5SsoBT7Ykz0h5hxWvc7Ko6VrWXvy5t67f53ZX04EZepY%2BiXtwSM4Fxz7njIyShlnxwWWjfMSLKmSpo2YAeJfhaPphER05U%2FWIOcT3pHXYNWd3C1eImvxvkkfD%2B9DBsOwclGr8cvGVwsiRP4y63Pxms9%2Ffv1SLtstTNaZGvxxe5%2FEp0EfwfYvz578xW6dFkJD%2FNZ8ZbXcFrrONWnw%2FNQdSmDtQWPomPSvV3cqcXeKVOAwkwLCWvppA0l%2F%2BFD2jsvshm2oR5e1Xrg43F%2FpF9drZzRXQKeNBToFw2rVMXKY660y613LhLDhR7ocvVrLnYADHnKqmAAgQ5FNk9p1jjszRl3RNv7V81XpkKMBchwLWRvhYhGvLVWgtyI9iV1q2K1kxkXTrdamLTMXN8Es5Tk26dEUNOOVJ0uAcXVE%2FitAevgbzCZZi3fMoOSwwQmnQ5%2BaZUnTBqMNL9lL0GOqUBjWJ6VFfTvm2GXVRMUMOY65Fs97Fql4iS89PIQ7ebrkWLGZdgmvXNVGBUhe5oF3DgNNL%2F7QnxGxLe7HOkYiaZPmWG19qbZ44hpQI4XglaWwbxK23O9sy7eV58JQkYkSfjuVWHhOBN2UZwjZoLuUiiVUk5FvceleILFHoQ7PA%2FZAK24e2P1Y9OE4a7mhQ%2F6FrPfZFRVwDieh51Q%2Fus%2FxtK1ErYIMIl&X-Amz-Signature=b88c4b48fcc2d8cf6bdc793f1cb9a600b4c30f9241d94430fecbec32ccfefda2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8af3f76b-b350-4668-99db-ffde6afd7a48/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWLA3BV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIF0mpRs4gnuD1BaMu84MAFazYU2auuxrZBidqWd32OO%2FAiEA4Y85fND80kU081B4TVXJx9QWPo36idxfYXqnBcU%2BHMgq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFSYPoDLwDPuFyKjGyrcA8%2FbwQzGqeq7aO%2BRqvJtqAkUgbtRvf9wyajBE5yxJYalzD6i8U9ARuneeTOp%2FfX0p0%2BU3Qv0Qx%2BtyoUEM2P3Es%2BF1cexFZHRff%2FGbFH8p4xipWHnw0QqnAxeROYjoo2tF9E4Zt98qq3TZQ18BS%2BXVHo9sKAkm6sXgEo%2B6CPakDB%2FlwAd6D0wxo5SsoBT7Ykz0h5hxWvc7Ko6VrWXvy5t67f53ZX04EZepY%2BiXtwSM4Fxz7njIyShlnxwWWjfMSLKmSpo2YAeJfhaPphER05U%2FWIOcT3pHXYNWd3C1eImvxvkkfD%2B9DBsOwclGr8cvGVwsiRP4y63Pxms9%2Ffv1SLtstTNaZGvxxe5%2FEp0EfwfYvz578xW6dFkJD%2FNZ8ZbXcFrrONWnw%2FNQdSmDtQWPomPSvV3cqcXeKVOAwkwLCWvppA0l%2F%2BFD2jsvshm2oR5e1Xrg43F%2FpF9drZzRXQKeNBToFw2rVMXKY660y613LhLDhR7ocvVrLnYADHnKqmAAgQ5FNk9p1jjszRl3RNv7V81XpkKMBchwLWRvhYhGvLVWgtyI9iV1q2K1kxkXTrdamLTMXN8Es5Tk26dEUNOOVJ0uAcXVE%2FitAevgbzCZZi3fMoOSwwQmnQ5%2BaZUnTBqMNL9lL0GOqUBjWJ6VFfTvm2GXVRMUMOY65Fs97Fql4iS89PIQ7ebrkWLGZdgmvXNVGBUhe5oF3DgNNL%2F7QnxGxLe7HOkYiaZPmWG19qbZ44hpQI4XglaWwbxK23O9sy7eV58JQkYkSfjuVWHhOBN2UZwjZoLuUiiVUk5FvceleILFHoQ7PA%2FZAK24e2P1Y9OE4a7mhQ%2F6FrPfZFRVwDieh51Q%2Fus%2FxtK1ErYIMIl&X-Amz-Signature=ceb4602cc35693819cf9166e62dbc35a1c2e2f5c6c92f48c8b75bcb2b915df91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/16d20e8e-68c0-4ad6-83fa-24ee550846a6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWLA3BV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIF0mpRs4gnuD1BaMu84MAFazYU2auuxrZBidqWd32OO%2FAiEA4Y85fND80kU081B4TVXJx9QWPo36idxfYXqnBcU%2BHMgq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFSYPoDLwDPuFyKjGyrcA8%2FbwQzGqeq7aO%2BRqvJtqAkUgbtRvf9wyajBE5yxJYalzD6i8U9ARuneeTOp%2FfX0p0%2BU3Qv0Qx%2BtyoUEM2P3Es%2BF1cexFZHRff%2FGbFH8p4xipWHnw0QqnAxeROYjoo2tF9E4Zt98qq3TZQ18BS%2BXVHo9sKAkm6sXgEo%2B6CPakDB%2FlwAd6D0wxo5SsoBT7Ykz0h5hxWvc7Ko6VrWXvy5t67f53ZX04EZepY%2BiXtwSM4Fxz7njIyShlnxwWWjfMSLKmSpo2YAeJfhaPphER05U%2FWIOcT3pHXYNWd3C1eImvxvkkfD%2B9DBsOwclGr8cvGVwsiRP4y63Pxms9%2Ffv1SLtstTNaZGvxxe5%2FEp0EfwfYvz578xW6dFkJD%2FNZ8ZbXcFrrONWnw%2FNQdSmDtQWPomPSvV3cqcXeKVOAwkwLCWvppA0l%2F%2BFD2jsvshm2oR5e1Xrg43F%2FpF9drZzRXQKeNBToFw2rVMXKY660y613LhLDhR7ocvVrLnYADHnKqmAAgQ5FNk9p1jjszRl3RNv7V81XpkKMBchwLWRvhYhGvLVWgtyI9iV1q2K1kxkXTrdamLTMXN8Es5Tk26dEUNOOVJ0uAcXVE%2FitAevgbzCZZi3fMoOSwwQmnQ5%2BaZUnTBqMNL9lL0GOqUBjWJ6VFfTvm2GXVRMUMOY65Fs97Fql4iS89PIQ7ebrkWLGZdgmvXNVGBUhe5oF3DgNNL%2F7QnxGxLe7HOkYiaZPmWG19qbZ44hpQI4XglaWwbxK23O9sy7eV58JQkYkSfjuVWHhOBN2UZwjZoLuUiiVUk5FvceleILFHoQ7PA%2FZAK24e2P1Y9OE4a7mhQ%2F6FrPfZFRVwDieh51Q%2Fus%2FxtK1ErYIMIl&X-Amz-Signature=95b1b3abfdbd491f848df8179844b5ae678d15fd88672869f56da2528b047df5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/73a2c105-2ca5-46a7-974c-ec918cf62c91/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWLA3BV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIF0mpRs4gnuD1BaMu84MAFazYU2auuxrZBidqWd32OO%2FAiEA4Y85fND80kU081B4TVXJx9QWPo36idxfYXqnBcU%2BHMgq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFSYPoDLwDPuFyKjGyrcA8%2FbwQzGqeq7aO%2BRqvJtqAkUgbtRvf9wyajBE5yxJYalzD6i8U9ARuneeTOp%2FfX0p0%2BU3Qv0Qx%2BtyoUEM2P3Es%2BF1cexFZHRff%2FGbFH8p4xipWHnw0QqnAxeROYjoo2tF9E4Zt98qq3TZQ18BS%2BXVHo9sKAkm6sXgEo%2B6CPakDB%2FlwAd6D0wxo5SsoBT7Ykz0h5hxWvc7Ko6VrWXvy5t67f53ZX04EZepY%2BiXtwSM4Fxz7njIyShlnxwWWjfMSLKmSpo2YAeJfhaPphER05U%2FWIOcT3pHXYNWd3C1eImvxvkkfD%2B9DBsOwclGr8cvGVwsiRP4y63Pxms9%2Ffv1SLtstTNaZGvxxe5%2FEp0EfwfYvz578xW6dFkJD%2FNZ8ZbXcFrrONWnw%2FNQdSmDtQWPomPSvV3cqcXeKVOAwkwLCWvppA0l%2F%2BFD2jsvshm2oR5e1Xrg43F%2FpF9drZzRXQKeNBToFw2rVMXKY660y613LhLDhR7ocvVrLnYADHnKqmAAgQ5FNk9p1jjszRl3RNv7V81XpkKMBchwLWRvhYhGvLVWgtyI9iV1q2K1kxkXTrdamLTMXN8Es5Tk26dEUNOOVJ0uAcXVE%2FitAevgbzCZZi3fMoOSwwQmnQ5%2BaZUnTBqMNL9lL0GOqUBjWJ6VFfTvm2GXVRMUMOY65Fs97Fql4iS89PIQ7ebrkWLGZdgmvXNVGBUhe5oF3DgNNL%2F7QnxGxLe7HOkYiaZPmWG19qbZ44hpQI4XglaWwbxK23O9sy7eV58JQkYkSfjuVWHhOBN2UZwjZoLuUiiVUk5FvceleILFHoQ7PA%2FZAK24e2P1Y9OE4a7mhQ%2F6FrPfZFRVwDieh51Q%2Fus%2FxtK1ErYIMIl&X-Amz-Signature=5b4bbcedacbb59b0a738eab245ce36ce686c34efc5bc64c0d984898cfe050204&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7d3cdfd2-3a59-4bf7-8d34-4b4314e49abd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWLA3BV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIF0mpRs4gnuD1BaMu84MAFazYU2auuxrZBidqWd32OO%2FAiEA4Y85fND80kU081B4TVXJx9QWPo36idxfYXqnBcU%2BHMgq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFSYPoDLwDPuFyKjGyrcA8%2FbwQzGqeq7aO%2BRqvJtqAkUgbtRvf9wyajBE5yxJYalzD6i8U9ARuneeTOp%2FfX0p0%2BU3Qv0Qx%2BtyoUEM2P3Es%2BF1cexFZHRff%2FGbFH8p4xipWHnw0QqnAxeROYjoo2tF9E4Zt98qq3TZQ18BS%2BXVHo9sKAkm6sXgEo%2B6CPakDB%2FlwAd6D0wxo5SsoBT7Ykz0h5hxWvc7Ko6VrWXvy5t67f53ZX04EZepY%2BiXtwSM4Fxz7njIyShlnxwWWjfMSLKmSpo2YAeJfhaPphER05U%2FWIOcT3pHXYNWd3C1eImvxvkkfD%2B9DBsOwclGr8cvGVwsiRP4y63Pxms9%2Ffv1SLtstTNaZGvxxe5%2FEp0EfwfYvz578xW6dFkJD%2FNZ8ZbXcFrrONWnw%2FNQdSmDtQWPomPSvV3cqcXeKVOAwkwLCWvppA0l%2F%2BFD2jsvshm2oR5e1Xrg43F%2FpF9drZzRXQKeNBToFw2rVMXKY660y613LhLDhR7ocvVrLnYADHnKqmAAgQ5FNk9p1jjszRl3RNv7V81XpkKMBchwLWRvhYhGvLVWgtyI9iV1q2K1kxkXTrdamLTMXN8Es5Tk26dEUNOOVJ0uAcXVE%2FitAevgbzCZZi3fMoOSwwQmnQ5%2BaZUnTBqMNL9lL0GOqUBjWJ6VFfTvm2GXVRMUMOY65Fs97Fql4iS89PIQ7ebrkWLGZdgmvXNVGBUhe5oF3DgNNL%2F7QnxGxLe7HOkYiaZPmWG19qbZ44hpQI4XglaWwbxK23O9sy7eV58JQkYkSfjuVWHhOBN2UZwjZoLuUiiVUk5FvceleILFHoQ7PA%2FZAK24e2P1Y9OE4a7mhQ%2F6FrPfZFRVwDieh51Q%2Fus%2FxtK1ErYIMIl&X-Amz-Signature=d9dfb3e742f5d4855de802fd41095d6f669a8cd9c3fdfd9371f28a97ba53a701&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74024f1a-9e67-4a06-856e-ff0920d20ba0/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWLA3BV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIF0mpRs4gnuD1BaMu84MAFazYU2auuxrZBidqWd32OO%2FAiEA4Y85fND80kU081B4TVXJx9QWPo36idxfYXqnBcU%2BHMgq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFSYPoDLwDPuFyKjGyrcA8%2FbwQzGqeq7aO%2BRqvJtqAkUgbtRvf9wyajBE5yxJYalzD6i8U9ARuneeTOp%2FfX0p0%2BU3Qv0Qx%2BtyoUEM2P3Es%2BF1cexFZHRff%2FGbFH8p4xipWHnw0QqnAxeROYjoo2tF9E4Zt98qq3TZQ18BS%2BXVHo9sKAkm6sXgEo%2B6CPakDB%2FlwAd6D0wxo5SsoBT7Ykz0h5hxWvc7Ko6VrWXvy5t67f53ZX04EZepY%2BiXtwSM4Fxz7njIyShlnxwWWjfMSLKmSpo2YAeJfhaPphER05U%2FWIOcT3pHXYNWd3C1eImvxvkkfD%2B9DBsOwclGr8cvGVwsiRP4y63Pxms9%2Ffv1SLtstTNaZGvxxe5%2FEp0EfwfYvz578xW6dFkJD%2FNZ8ZbXcFrrONWnw%2FNQdSmDtQWPomPSvV3cqcXeKVOAwkwLCWvppA0l%2F%2BFD2jsvshm2oR5e1Xrg43F%2FpF9drZzRXQKeNBToFw2rVMXKY660y613LhLDhR7ocvVrLnYADHnKqmAAgQ5FNk9p1jjszRl3RNv7V81XpkKMBchwLWRvhYhGvLVWgtyI9iV1q2K1kxkXTrdamLTMXN8Es5Tk26dEUNOOVJ0uAcXVE%2FitAevgbzCZZi3fMoOSwwQmnQ5%2BaZUnTBqMNL9lL0GOqUBjWJ6VFfTvm2GXVRMUMOY65Fs97Fql4iS89PIQ7ebrkWLGZdgmvXNVGBUhe5oF3DgNNL%2F7QnxGxLe7HOkYiaZPmWG19qbZ44hpQI4XglaWwbxK23O9sy7eV58JQkYkSfjuVWHhOBN2UZwjZoLuUiiVUk5FvceleILFHoQ7PA%2FZAK24e2P1Y9OE4a7mhQ%2F6FrPfZFRVwDieh51Q%2Fus%2FxtK1ErYIMIl&X-Amz-Signature=abdd4ebdc9271d1a131493b9e0d7bd9d4e7293a4006c79a2619ad4604a034769&X-Amz-SignedHeaders=host&x-id=GetObject)
![Figure2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/14af08ae-a84c-4391-95ac-9cee37c62973/Figure2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWLA3BV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIF0mpRs4gnuD1BaMu84MAFazYU2auuxrZBidqWd32OO%2FAiEA4Y85fND80kU081B4TVXJx9QWPo36idxfYXqnBcU%2BHMgq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDFSYPoDLwDPuFyKjGyrcA8%2FbwQzGqeq7aO%2BRqvJtqAkUgbtRvf9wyajBE5yxJYalzD6i8U9ARuneeTOp%2FfX0p0%2BU3Qv0Qx%2BtyoUEM2P3Es%2BF1cexFZHRff%2FGbFH8p4xipWHnw0QqnAxeROYjoo2tF9E4Zt98qq3TZQ18BS%2BXVHo9sKAkm6sXgEo%2B6CPakDB%2FlwAd6D0wxo5SsoBT7Ykz0h5hxWvc7Ko6VrWXvy5t67f53ZX04EZepY%2BiXtwSM4Fxz7njIyShlnxwWWjfMSLKmSpo2YAeJfhaPphER05U%2FWIOcT3pHXYNWd3C1eImvxvkkfD%2B9DBsOwclGr8cvGVwsiRP4y63Pxms9%2Ffv1SLtstTNaZGvxxe5%2FEp0EfwfYvz578xW6dFkJD%2FNZ8ZbXcFrrONWnw%2FNQdSmDtQWPomPSvV3cqcXeKVOAwkwLCWvppA0l%2F%2BFD2jsvshm2oR5e1Xrg43F%2FpF9drZzRXQKeNBToFw2rVMXKY660y613LhLDhR7ocvVrLnYADHnKqmAAgQ5FNk9p1jjszRl3RNv7V81XpkKMBchwLWRvhYhGvLVWgtyI9iV1q2K1kxkXTrdamLTMXN8Es5Tk26dEUNOOVJ0uAcXVE%2FitAevgbzCZZi3fMoOSwwQmnQ5%2BaZUnTBqMNL9lL0GOqUBjWJ6VFfTvm2GXVRMUMOY65Fs97Fql4iS89PIQ7ebrkWLGZdgmvXNVGBUhe5oF3DgNNL%2F7QnxGxLe7HOkYiaZPmWG19qbZ44hpQI4XglaWwbxK23O9sy7eV58JQkYkSfjuVWHhOBN2UZwjZoLuUiiVUk5FvceleILFHoQ7PA%2FZAK24e2P1Y9OE4a7mhQ%2F6FrPfZFRVwDieh51Q%2Fus%2FxtK1ErYIMIl&X-Amz-Signature=fda0148bbd73f9f2c0a05188e1aad8ced6ade710cc2a055b8ae21ead57ddb2ff&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Characteristics of K-Means
- **Partition-Based**: Divides data into K clusters based on similarity.
- **Efficiency**: Relatively efficient on medium and large-sized datasets.
- **Cluster Shape**: Produces spherical clusters as it groups data around centroids.
- **Pre-Specified K**: Requires the number of clusters (K) to be specified beforehand, which can be challenging.
### Conclusion
K-Means clustering is a widely-used algorithm for grouping data into clusters based on feature similarity. The algorithm's effectiveness is often evaluated using metrics such as WCSS and the elbow method to determine the optimal number of clusters.