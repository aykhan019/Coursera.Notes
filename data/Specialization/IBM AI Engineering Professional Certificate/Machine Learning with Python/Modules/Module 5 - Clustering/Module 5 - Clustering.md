

# Module 5: Clustering
## Clustering: An Introduction
### Overview of Clustering
Clustering is an unsupervised learning technique used to group similar data points into clusters based on their characteristics. This method is commonly applied in various domains to segment data, identify patterns, and make predictions.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9cb01ce9-5e0d-49ef-8f43-c9db38fbc0e0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCEWIAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLhhzuWR9d828OV9gELkmAHm8Gz2Rcq%2B%2Fe1f6GRTEZQAiBmexuxOL3kRJvZPkuQ6oY3%2F4HnUESfh4J%2BDdH3amgqQiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYC%2BoVTmShRWgEtx%2FKtwDIGjuV9JTNXkoUgENRlRRjMDU4cGv27ShlOOl6qPGkk46l08oRLVw0yHl%2F9%2Fz6eHWT7V03phBc9vTZdFc5%2B%2FI7Cr4Er2cQ1EfVkv3iREybvTKOhqQmd610ja7XObjYUps9Gu%2FmYAcwXG76PJTobUfI0wcdlehnBvoGZftw0YlEjYpv8Yyy7GQrmp7qSl8YbeAdpJUco278YX2dRzgguCjTCejZAL1kbNxa2X7byO6YWzpNupYzTY6NWiJsAfYbJxck0U4Wne1S8wqENX6RcgkxD16FYVZDC6zH4zScSqOGcl1BO%2BGi6j2%2B5tWJRWlq2u6xMkbi3cdJ6A%2FDDKwX%2FZXfVYbQyKHhjKol6u9O4Jl8k5JXM8ysGpWsMHxIUCWD%2F5HdG%2FVj1VD03luVrii6OOptJqKiUyrrTngi6gwhp7WLIr2Jc4Ic6NtMoL0OuYj66SnGgkeMNhnN4VvZ6ef0NJpiuHE8FszMs0CMFcRgpxQ1I0k0kCw3LjYgEh2gi%2FY%2B%2BNmf%2F3rBi68nbaAp4Hf%2FiFJHQDanhrNR7P9s%2FYEYgZBWN3Zow3B6imKPNyCPPkVlXmmcztr65VfDWpQvmmNouo0b9mgIp%2B%2FByGZfUTuGG9fc0HxnLFFWop5v4DGyREw%2BdbyvAY6pgFlDSdNC%2FDFu7e9nBd5vNt99zzmOhES6hW2GlA%2FWEhmC5ngwGjp0L%2BSEvjpkmk%2FU2LBfAajVaoe3c3EuuaZa0r7f5D4jJq34d72FFhx%2BjHc3fimbB0CkMi8ba3IyaCAdFhZ0WGGBlOTizK6ihAqyJx5t04524CwzeKTySReLbDe%2FRfvKq79aAFERlUwMxT5fMvG9guxdHZ%2B6SgC7zvQfOjpDjB3FyWo&X-Amz-Signature=0ac6b3135b245b1999ad708cb0712025861630d3dd87c9231d2a63c0e3de2427&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ede0dba7-3f63-4051-85fd-51f2f38eeeb5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCEWIAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLhhzuWR9d828OV9gELkmAHm8Gz2Rcq%2B%2Fe1f6GRTEZQAiBmexuxOL3kRJvZPkuQ6oY3%2F4HnUESfh4J%2BDdH3amgqQiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYC%2BoVTmShRWgEtx%2FKtwDIGjuV9JTNXkoUgENRlRRjMDU4cGv27ShlOOl6qPGkk46l08oRLVw0yHl%2F9%2Fz6eHWT7V03phBc9vTZdFc5%2B%2FI7Cr4Er2cQ1EfVkv3iREybvTKOhqQmd610ja7XObjYUps9Gu%2FmYAcwXG76PJTobUfI0wcdlehnBvoGZftw0YlEjYpv8Yyy7GQrmp7qSl8YbeAdpJUco278YX2dRzgguCjTCejZAL1kbNxa2X7byO6YWzpNupYzTY6NWiJsAfYbJxck0U4Wne1S8wqENX6RcgkxD16FYVZDC6zH4zScSqOGcl1BO%2BGi6j2%2B5tWJRWlq2u6xMkbi3cdJ6A%2FDDKwX%2FZXfVYbQyKHhjKol6u9O4Jl8k5JXM8ysGpWsMHxIUCWD%2F5HdG%2FVj1VD03luVrii6OOptJqKiUyrrTngi6gwhp7WLIr2Jc4Ic6NtMoL0OuYj66SnGgkeMNhnN4VvZ6ef0NJpiuHE8FszMs0CMFcRgpxQ1I0k0kCw3LjYgEh2gi%2FY%2B%2BNmf%2F3rBi68nbaAp4Hf%2FiFJHQDanhrNR7P9s%2FYEYgZBWN3Zow3B6imKPNyCPPkVlXmmcztr65VfDWpQvmmNouo0b9mgIp%2B%2FByGZfUTuGG9fc0HxnLFFWop5v4DGyREw%2BdbyvAY6pgFlDSdNC%2FDFu7e9nBd5vNt99zzmOhES6hW2GlA%2FWEhmC5ngwGjp0L%2BSEvjpkmk%2FU2LBfAajVaoe3c3EuuaZa0r7f5D4jJq34d72FFhx%2BjHc3fimbB0CkMi8ba3IyaCAdFhZ0WGGBlOTizK6ihAqyJx5t04524CwzeKTySReLbDe%2FRfvKq79aAFERlUwMxT5fMvG9guxdHZ%2B6SgC7zvQfOjpDjB3FyWo&X-Amz-Signature=d1f6c106f67f681c44a193be84ab7e8e6cd2d1893bb9cc8f8cdb1df8d83aac46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23d540d1-3363-46c0-b145-c20928ff781b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCEWIAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLhhzuWR9d828OV9gELkmAHm8Gz2Rcq%2B%2Fe1f6GRTEZQAiBmexuxOL3kRJvZPkuQ6oY3%2F4HnUESfh4J%2BDdH3amgqQiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYC%2BoVTmShRWgEtx%2FKtwDIGjuV9JTNXkoUgENRlRRjMDU4cGv27ShlOOl6qPGkk46l08oRLVw0yHl%2F9%2Fz6eHWT7V03phBc9vTZdFc5%2B%2FI7Cr4Er2cQ1EfVkv3iREybvTKOhqQmd610ja7XObjYUps9Gu%2FmYAcwXG76PJTobUfI0wcdlehnBvoGZftw0YlEjYpv8Yyy7GQrmp7qSl8YbeAdpJUco278YX2dRzgguCjTCejZAL1kbNxa2X7byO6YWzpNupYzTY6NWiJsAfYbJxck0U4Wne1S8wqENX6RcgkxD16FYVZDC6zH4zScSqOGcl1BO%2BGi6j2%2B5tWJRWlq2u6xMkbi3cdJ6A%2FDDKwX%2FZXfVYbQyKHhjKol6u9O4Jl8k5JXM8ysGpWsMHxIUCWD%2F5HdG%2FVj1VD03luVrii6OOptJqKiUyrrTngi6gwhp7WLIr2Jc4Ic6NtMoL0OuYj66SnGgkeMNhnN4VvZ6ef0NJpiuHE8FszMs0CMFcRgpxQ1I0k0kCw3LjYgEh2gi%2FY%2B%2BNmf%2F3rBi68nbaAp4Hf%2FiFJHQDanhrNR7P9s%2FYEYgZBWN3Zow3B6imKPNyCPPkVlXmmcztr65VfDWpQvmmNouo0b9mgIp%2B%2FByGZfUTuGG9fc0HxnLFFWop5v4DGyREw%2BdbyvAY6pgFlDSdNC%2FDFu7e9nBd5vNt99zzmOhES6hW2GlA%2FWEhmC5ngwGjp0L%2BSEvjpkmk%2FU2LBfAajVaoe3c3EuuaZa0r7f5D4jJq34d72FFhx%2BjHc3fimbB0CkMi8ba3IyaCAdFhZ0WGGBlOTizK6ihAqyJx5t04524CwzeKTySReLbDe%2FRfvKq79aAFERlUwMxT5fMvG9guxdHZ%2B6SgC7zvQfOjpDjB3FyWo&X-Amz-Signature=4a30dc16534cf6023c8567881640d30ddc76db937858e8926495b86dbf1adec6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8af3f76b-b350-4668-99db-ffde6afd7a48/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCEWIAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLhhzuWR9d828OV9gELkmAHm8Gz2Rcq%2B%2Fe1f6GRTEZQAiBmexuxOL3kRJvZPkuQ6oY3%2F4HnUESfh4J%2BDdH3amgqQiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYC%2BoVTmShRWgEtx%2FKtwDIGjuV9JTNXkoUgENRlRRjMDU4cGv27ShlOOl6qPGkk46l08oRLVw0yHl%2F9%2Fz6eHWT7V03phBc9vTZdFc5%2B%2FI7Cr4Er2cQ1EfVkv3iREybvTKOhqQmd610ja7XObjYUps9Gu%2FmYAcwXG76PJTobUfI0wcdlehnBvoGZftw0YlEjYpv8Yyy7GQrmp7qSl8YbeAdpJUco278YX2dRzgguCjTCejZAL1kbNxa2X7byO6YWzpNupYzTY6NWiJsAfYbJxck0U4Wne1S8wqENX6RcgkxD16FYVZDC6zH4zScSqOGcl1BO%2BGi6j2%2B5tWJRWlq2u6xMkbi3cdJ6A%2FDDKwX%2FZXfVYbQyKHhjKol6u9O4Jl8k5JXM8ysGpWsMHxIUCWD%2F5HdG%2FVj1VD03luVrii6OOptJqKiUyrrTngi6gwhp7WLIr2Jc4Ic6NtMoL0OuYj66SnGgkeMNhnN4VvZ6ef0NJpiuHE8FszMs0CMFcRgpxQ1I0k0kCw3LjYgEh2gi%2FY%2B%2BNmf%2F3rBi68nbaAp4Hf%2FiFJHQDanhrNR7P9s%2FYEYgZBWN3Zow3B6imKPNyCPPkVlXmmcztr65VfDWpQvmmNouo0b9mgIp%2B%2FByGZfUTuGG9fc0HxnLFFWop5v4DGyREw%2BdbyvAY6pgFlDSdNC%2FDFu7e9nBd5vNt99zzmOhES6hW2GlA%2FWEhmC5ngwGjp0L%2BSEvjpkmk%2FU2LBfAajVaoe3c3EuuaZa0r7f5D4jJq34d72FFhx%2BjHc3fimbB0CkMi8ba3IyaCAdFhZ0WGGBlOTizK6ihAqyJx5t04524CwzeKTySReLbDe%2FRfvKq79aAFERlUwMxT5fMvG9guxdHZ%2B6SgC7zvQfOjpDjB3FyWo&X-Amz-Signature=f7e11faeb6d34813573d95a08a91e3628a041449c7c178288d0e3b50bc3bd2a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/16d20e8e-68c0-4ad6-83fa-24ee550846a6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCEWIAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLhhzuWR9d828OV9gELkmAHm8Gz2Rcq%2B%2Fe1f6GRTEZQAiBmexuxOL3kRJvZPkuQ6oY3%2F4HnUESfh4J%2BDdH3amgqQiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYC%2BoVTmShRWgEtx%2FKtwDIGjuV9JTNXkoUgENRlRRjMDU4cGv27ShlOOl6qPGkk46l08oRLVw0yHl%2F9%2Fz6eHWT7V03phBc9vTZdFc5%2B%2FI7Cr4Er2cQ1EfVkv3iREybvTKOhqQmd610ja7XObjYUps9Gu%2FmYAcwXG76PJTobUfI0wcdlehnBvoGZftw0YlEjYpv8Yyy7GQrmp7qSl8YbeAdpJUco278YX2dRzgguCjTCejZAL1kbNxa2X7byO6YWzpNupYzTY6NWiJsAfYbJxck0U4Wne1S8wqENX6RcgkxD16FYVZDC6zH4zScSqOGcl1BO%2BGi6j2%2B5tWJRWlq2u6xMkbi3cdJ6A%2FDDKwX%2FZXfVYbQyKHhjKol6u9O4Jl8k5JXM8ysGpWsMHxIUCWD%2F5HdG%2FVj1VD03luVrii6OOptJqKiUyrrTngi6gwhp7WLIr2Jc4Ic6NtMoL0OuYj66SnGgkeMNhnN4VvZ6ef0NJpiuHE8FszMs0CMFcRgpxQ1I0k0kCw3LjYgEh2gi%2FY%2B%2BNmf%2F3rBi68nbaAp4Hf%2FiFJHQDanhrNR7P9s%2FYEYgZBWN3Zow3B6imKPNyCPPkVlXmmcztr65VfDWpQvmmNouo0b9mgIp%2B%2FByGZfUTuGG9fc0HxnLFFWop5v4DGyREw%2BdbyvAY6pgFlDSdNC%2FDFu7e9nBd5vNt99zzmOhES6hW2GlA%2FWEhmC5ngwGjp0L%2BSEvjpkmk%2FU2LBfAajVaoe3c3EuuaZa0r7f5D4jJq34d72FFhx%2BjHc3fimbB0CkMi8ba3IyaCAdFhZ0WGGBlOTizK6ihAqyJx5t04524CwzeKTySReLbDe%2FRfvKq79aAFERlUwMxT5fMvG9guxdHZ%2B6SgC7zvQfOjpDjB3FyWo&X-Amz-Signature=8cd049b93dde4af37dd6237d375d9d66e2f30fedcbc6993fa8bffe1c99e23e99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/73a2c105-2ca5-46a7-974c-ec918cf62c91/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCEWIAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLhhzuWR9d828OV9gELkmAHm8Gz2Rcq%2B%2Fe1f6GRTEZQAiBmexuxOL3kRJvZPkuQ6oY3%2F4HnUESfh4J%2BDdH3amgqQiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYC%2BoVTmShRWgEtx%2FKtwDIGjuV9JTNXkoUgENRlRRjMDU4cGv27ShlOOl6qPGkk46l08oRLVw0yHl%2F9%2Fz6eHWT7V03phBc9vTZdFc5%2B%2FI7Cr4Er2cQ1EfVkv3iREybvTKOhqQmd610ja7XObjYUps9Gu%2FmYAcwXG76PJTobUfI0wcdlehnBvoGZftw0YlEjYpv8Yyy7GQrmp7qSl8YbeAdpJUco278YX2dRzgguCjTCejZAL1kbNxa2X7byO6YWzpNupYzTY6NWiJsAfYbJxck0U4Wne1S8wqENX6RcgkxD16FYVZDC6zH4zScSqOGcl1BO%2BGi6j2%2B5tWJRWlq2u6xMkbi3cdJ6A%2FDDKwX%2FZXfVYbQyKHhjKol6u9O4Jl8k5JXM8ysGpWsMHxIUCWD%2F5HdG%2FVj1VD03luVrii6OOptJqKiUyrrTngi6gwhp7WLIr2Jc4Ic6NtMoL0OuYj66SnGgkeMNhnN4VvZ6ef0NJpiuHE8FszMs0CMFcRgpxQ1I0k0kCw3LjYgEh2gi%2FY%2B%2BNmf%2F3rBi68nbaAp4Hf%2FiFJHQDanhrNR7P9s%2FYEYgZBWN3Zow3B6imKPNyCPPkVlXmmcztr65VfDWpQvmmNouo0b9mgIp%2B%2FByGZfUTuGG9fc0HxnLFFWop5v4DGyREw%2BdbyvAY6pgFlDSdNC%2FDFu7e9nBd5vNt99zzmOhES6hW2GlA%2FWEhmC5ngwGjp0L%2BSEvjpkmk%2FU2LBfAajVaoe3c3EuuaZa0r7f5D4jJq34d72FFhx%2BjHc3fimbB0CkMi8ba3IyaCAdFhZ0WGGBlOTizK6ihAqyJx5t04524CwzeKTySReLbDe%2FRfvKq79aAFERlUwMxT5fMvG9guxdHZ%2B6SgC7zvQfOjpDjB3FyWo&X-Amz-Signature=0f3989ce79461047962446eeae263b1df12b0dd84cb4150521add47482736728&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7d3cdfd2-3a59-4bf7-8d34-4b4314e49abd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCEWIAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLhhzuWR9d828OV9gELkmAHm8Gz2Rcq%2B%2Fe1f6GRTEZQAiBmexuxOL3kRJvZPkuQ6oY3%2F4HnUESfh4J%2BDdH3amgqQiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYC%2BoVTmShRWgEtx%2FKtwDIGjuV9JTNXkoUgENRlRRjMDU4cGv27ShlOOl6qPGkk46l08oRLVw0yHl%2F9%2Fz6eHWT7V03phBc9vTZdFc5%2B%2FI7Cr4Er2cQ1EfVkv3iREybvTKOhqQmd610ja7XObjYUps9Gu%2FmYAcwXG76PJTobUfI0wcdlehnBvoGZftw0YlEjYpv8Yyy7GQrmp7qSl8YbeAdpJUco278YX2dRzgguCjTCejZAL1kbNxa2X7byO6YWzpNupYzTY6NWiJsAfYbJxck0U4Wne1S8wqENX6RcgkxD16FYVZDC6zH4zScSqOGcl1BO%2BGi6j2%2B5tWJRWlq2u6xMkbi3cdJ6A%2FDDKwX%2FZXfVYbQyKHhjKol6u9O4Jl8k5JXM8ysGpWsMHxIUCWD%2F5HdG%2FVj1VD03luVrii6OOptJqKiUyrrTngi6gwhp7WLIr2Jc4Ic6NtMoL0OuYj66SnGgkeMNhnN4VvZ6ef0NJpiuHE8FszMs0CMFcRgpxQ1I0k0kCw3LjYgEh2gi%2FY%2B%2BNmf%2F3rBi68nbaAp4Hf%2FiFJHQDanhrNR7P9s%2FYEYgZBWN3Zow3B6imKPNyCPPkVlXmmcztr65VfDWpQvmmNouo0b9mgIp%2B%2FByGZfUTuGG9fc0HxnLFFWop5v4DGyREw%2BdbyvAY6pgFlDSdNC%2FDFu7e9nBd5vNt99zzmOhES6hW2GlA%2FWEhmC5ngwGjp0L%2BSEvjpkmk%2FU2LBfAajVaoe3c3EuuaZa0r7f5D4jJq34d72FFhx%2BjHc3fimbB0CkMi8ba3IyaCAdFhZ0WGGBlOTizK6ihAqyJx5t04524CwzeKTySReLbDe%2FRfvKq79aAFERlUwMxT5fMvG9guxdHZ%2B6SgC7zvQfOjpDjB3FyWo&X-Amz-Signature=a73723e92331e8a402aa97d1a05b7eab70627032e1186a97143cdefacfdd0747&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74024f1a-9e67-4a06-856e-ff0920d20ba0/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCEWIAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLhhzuWR9d828OV9gELkmAHm8Gz2Rcq%2B%2Fe1f6GRTEZQAiBmexuxOL3kRJvZPkuQ6oY3%2F4HnUESfh4J%2BDdH3amgqQiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYC%2BoVTmShRWgEtx%2FKtwDIGjuV9JTNXkoUgENRlRRjMDU4cGv27ShlOOl6qPGkk46l08oRLVw0yHl%2F9%2Fz6eHWT7V03phBc9vTZdFc5%2B%2FI7Cr4Er2cQ1EfVkv3iREybvTKOhqQmd610ja7XObjYUps9Gu%2FmYAcwXG76PJTobUfI0wcdlehnBvoGZftw0YlEjYpv8Yyy7GQrmp7qSl8YbeAdpJUco278YX2dRzgguCjTCejZAL1kbNxa2X7byO6YWzpNupYzTY6NWiJsAfYbJxck0U4Wne1S8wqENX6RcgkxD16FYVZDC6zH4zScSqOGcl1BO%2BGi6j2%2B5tWJRWlq2u6xMkbi3cdJ6A%2FDDKwX%2FZXfVYbQyKHhjKol6u9O4Jl8k5JXM8ysGpWsMHxIUCWD%2F5HdG%2FVj1VD03luVrii6OOptJqKiUyrrTngi6gwhp7WLIr2Jc4Ic6NtMoL0OuYj66SnGgkeMNhnN4VvZ6ef0NJpiuHE8FszMs0CMFcRgpxQ1I0k0kCw3LjYgEh2gi%2FY%2B%2BNmf%2F3rBi68nbaAp4Hf%2FiFJHQDanhrNR7P9s%2FYEYgZBWN3Zow3B6imKPNyCPPkVlXmmcztr65VfDWpQvmmNouo0b9mgIp%2B%2FByGZfUTuGG9fc0HxnLFFWop5v4DGyREw%2BdbyvAY6pgFlDSdNC%2FDFu7e9nBd5vNt99zzmOhES6hW2GlA%2FWEhmC5ngwGjp0L%2BSEvjpkmk%2FU2LBfAajVaoe3c3EuuaZa0r7f5D4jJq34d72FFhx%2BjHc3fimbB0CkMi8ba3IyaCAdFhZ0WGGBlOTizK6ihAqyJx5t04524CwzeKTySReLbDe%2FRfvKq79aAFERlUwMxT5fMvG9guxdHZ%2B6SgC7zvQfOjpDjB3FyWo&X-Amz-Signature=f87f1c4dd766a4e7f7af5333a387bfe25946be8475ba62db662bc36b369afe9d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Figure2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/14af08ae-a84c-4391-95ac-9cee37c62973/Figure2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCEWIAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBLhhzuWR9d828OV9gELkmAHm8Gz2Rcq%2B%2Fe1f6GRTEZQAiBmexuxOL3kRJvZPkuQ6oY3%2F4HnUESfh4J%2BDdH3amgqQiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYC%2BoVTmShRWgEtx%2FKtwDIGjuV9JTNXkoUgENRlRRjMDU4cGv27ShlOOl6qPGkk46l08oRLVw0yHl%2F9%2Fz6eHWT7V03phBc9vTZdFc5%2B%2FI7Cr4Er2cQ1EfVkv3iREybvTKOhqQmd610ja7XObjYUps9Gu%2FmYAcwXG76PJTobUfI0wcdlehnBvoGZftw0YlEjYpv8Yyy7GQrmp7qSl8YbeAdpJUco278YX2dRzgguCjTCejZAL1kbNxa2X7byO6YWzpNupYzTY6NWiJsAfYbJxck0U4Wne1S8wqENX6RcgkxD16FYVZDC6zH4zScSqOGcl1BO%2BGi6j2%2B5tWJRWlq2u6xMkbi3cdJ6A%2FDDKwX%2FZXfVYbQyKHhjKol6u9O4Jl8k5JXM8ysGpWsMHxIUCWD%2F5HdG%2FVj1VD03luVrii6OOptJqKiUyrrTngi6gwhp7WLIr2Jc4Ic6NtMoL0OuYj66SnGgkeMNhnN4VvZ6ef0NJpiuHE8FszMs0CMFcRgpxQ1I0k0kCw3LjYgEh2gi%2FY%2B%2BNmf%2F3rBi68nbaAp4Hf%2FiFJHQDanhrNR7P9s%2FYEYgZBWN3Zow3B6imKPNyCPPkVlXmmcztr65VfDWpQvmmNouo0b9mgIp%2B%2FByGZfUTuGG9fc0HxnLFFWop5v4DGyREw%2BdbyvAY6pgFlDSdNC%2FDFu7e9nBd5vNt99zzmOhES6hW2GlA%2FWEhmC5ngwGjp0L%2BSEvjpkmk%2FU2LBfAajVaoe3c3EuuaZa0r7f5D4jJq34d72FFhx%2BjHc3fimbB0CkMi8ba3IyaCAdFhZ0WGGBlOTizK6ihAqyJx5t04524CwzeKTySReLbDe%2FRfvKq79aAFERlUwMxT5fMvG9guxdHZ%2B6SgC7zvQfOjpDjB3FyWo&X-Amz-Signature=441b83adb5b77088f8ac5e749b6e8d3a581f75da39bbf1673419a70acb36ced3&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Characteristics of K-Means
- **Partition-Based**: Divides data into K clusters based on similarity.
- **Efficiency**: Relatively efficient on medium and large-sized datasets.
- **Cluster Shape**: Produces spherical clusters as it groups data around centroids.
- **Pre-Specified K**: Requires the number of clusters (K) to be specified beforehand, which can be challenging.
### Conclusion
K-Means clustering is a widely-used algorithm for grouping data into clusters based on feature similarity. The algorithm's effectiveness is often evaluated using metrics such as WCSS and the elbow method to determine the optimal number of clusters.