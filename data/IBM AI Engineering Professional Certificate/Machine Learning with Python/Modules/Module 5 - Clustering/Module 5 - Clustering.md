

# Module 5: Clustering
## Clustering: An Introduction
### Overview of Clustering
Clustering is an unsupervised learning technique used to group similar data points into clusters based on their characteristics. This method is commonly applied in various domains to segment data, identify patterns, and make predictions.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9cb01ce9-5e0d-49ef-8f43-c9db38fbc0e0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=9c362b004d0c4a7befdf43d2f3a7d670404ee7ce56c45807f6f8abf1bdece84b&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ede0dba7-3f63-4051-85fd-51f2f38eeeb5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=95fd0cf72fd0e8ad5e89125cbd4e9dd07e118c76113b07152d2e6a8abaa8c47d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23d540d1-3363-46c0-b145-c20928ff781b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=dc62196fea9c09a88c551c4a722d2498cfe2bb1f228503c53f35b92ad77d6c85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8af3f76b-b350-4668-99db-ffde6afd7a48/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=b8ef9813ad76b9a97d485b64ea45eb25fc69d47075a1d76ec92bdfb02caf53fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/16d20e8e-68c0-4ad6-83fa-24ee550846a6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=74bee8d80d700271ed3689da7f781440ba443f3dee6c3162228f9d35a9cbc3f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/73a2c105-2ca5-46a7-974c-ec918cf62c91/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=9fb35a2bf5f1f62cd023a3a709c1ff3a597c172ceb48ab49588f146917faa167&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7d3cdfd2-3a59-4bf7-8d34-4b4314e49abd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=b0cb7e0a242fd07a8a85b2920255ceaa49c67af9401e0c4964d90c4c0bd8828d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74024f1a-9e67-4a06-856e-ff0920d20ba0/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=5c392d0d98eed7b63e873c770da0d20600ee4e4766a04a45f02c2378f7e4773d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Figure2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/14af08ae-a84c-4391-95ac-9cee37c62973/Figure2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE4RD6XG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBCeYorktqU92ABtLi8hnC3Fy8iP3ZzlJBdb2APEXzP9AiEAsqpUfL7omv6v6b4xjFScePE6s44HcwoDCuKpUWdz%2FQEq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFJJRnnPDCe0nXHGjSrcA%2FRlNgw%2BzQWWAEE5NjjaHiCEAg1YCN47GesbS3Ymd0UYsSrpH2aam96blliIFbXjiMB7e2aMOXuxxb21F0FdiDU4B%2FmazkpqL5uyivA7xHXJlnhfD%2F2gWkZG2Ukv5%2BvD12y4TMlBK9sNy03oEw6qeRP5SRkEJ%2BzhFBCj8a1DuobtcQSkZsOwnpfJj9xSFXnCPbDn5AqV%2BIpZJN2oMgVqlc0Wl2yIUkA7pa0sd9JMjRzwEOBycXf6%2BPx7IorANbYZsUIWebZ8Q6KDGrOYD2xvL9SjnRnpXnrUmRvXV7qELWrCBPRgLDKc1VXZyvq5TBOaGhFbh%2FrM%2BE1eh6Ou9MBfMspIV9Bf8fm67fP51%2BdK6wgd%2Bb0KKTThgHkdmYoBoexYKp5tc3qYvhtwb8rzxoiuo4uQ8wypMrCgt33977YHMjCJhhySYxh8pbNrAnxP1bSry39YGS9szHOlg8Z8oSaV0tkt2b3tVZTXjO5Bo2pY7POybjae01DpyxL%2FbcW1mMINldXcyr3oWuakJ1KvZYHrC6rMW3wdvFvX0KwSg8gNTDb6LYY%2Fnmetn62qtayA0BqeysZ%2BixtIXZAvbUu00HBCLpQn%2F0E%2BzKW%2FOQMiRTCAr9Fzrg0gSZX82YigplDOMJ%2F5i70GOqUBhEQN4a%2BhM2yxIQr%2Bg29laFSuWvCMyKK3tSo4gy0cPaqaPDsacHUUe52jhuBEL8Bx671VyrFg9RCZif%2B%2FjOUfvomAEDXiCstIXn10VFy%2BSl5h0Y97d9%2Fya6B5ISksI7BO96OLI5tcaONOn69nMzsE0dmvi0hXZx4Jcd%2B0U9oAp0MwWbnQoVSlmxNip4ecZRMa38D0FW4ouc3Lv%2FeRqiRYUNRdVU3M&X-Amz-Signature=f08e8a18750e97d138437d810e071d4c76c04afb850c86908194e4fdc20173f8&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Characteristics of K-Means
- **Partition-Based**: Divides data into K clusters based on similarity.
- **Efficiency**: Relatively efficient on medium and large-sized datasets.
- **Cluster Shape**: Produces spherical clusters as it groups data around centroids.
- **Pre-Specified K**: Requires the number of clusters (K) to be specified beforehand, which can be challenging.
### Conclusion
K-Means clustering is a widely-used algorithm for grouping data into clusters based on feature similarity. The algorithm's effectiveness is often evaluated using metrics such as WCSS and the elbow method to determine the optimal number of clusters.