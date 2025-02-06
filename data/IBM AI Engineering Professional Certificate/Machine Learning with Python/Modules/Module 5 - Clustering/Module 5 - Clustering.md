

# Module 5: Clustering
## Clustering: An Introduction
### Overview of Clustering
Clustering is an unsupervised learning technique used to group similar data points into clusters based on their characteristics. This method is commonly applied in various domains to segment data, identify patterns, and make predictions.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9cb01ce9-5e0d-49ef-8f43-c9db38fbc0e0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXCXCC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIDJyyLiOzrkXHQqtMdibJ94qmYv6aCH6qKl9gTpRHGltAiBGM1MTPa%2BmIwwg1OSndtnIoVQ4kZeTQV7lxAAVbqsgFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMnJGF%2FpdvE3t1KB20KtwDrttyrq3z%2FAUjYh9cpZjgDEwoo4G%2BUp82kQ6OhEnUyNcdixoWp0UvcrchCLTRoXlUgMNsPLlf8DHWE5M0LZL2xS%2BzG1jDjAt6pjXOmGffmk9Nhx86%2Bt%2BYvhKAZFJEaP%2FXre949rFo2%2B1iopcLQkK8gFWYucPLHgNdRyQ%2F1wiibU%2B%2BWzlU1ibY36NS%2FqfEeks9VJBqJBOlWtEPP0gpaI5CA10N1EF3%2FP7aGrjYF9mbl%2FvC0TDPYHorQZkBoQuvzc6362XwtOkMgcMLdH1ZokNGKf3DqOJnIaiYinqauK%2BH97mnVYcpH476rg7cbufEysg%2Bp3guB47C0DLrqDtNxC5gH%2BxFMfd9u4OEvUwDhbMp0PTRDnfhBupfClgskfWL9LRhkC5L5pwvMooyfEVy%2FUw32dVmFCV%2BhbD%2BV4jqvKstLY96cccQqYYkawr24gMZ%2BAqUlyVDA%2FBluR8cl5YMc7xbM3cZPTM1vDkVWgzxjNIRLoco%2FGqAC24nqsavbIt50ORfG9MhUdwtOVRykrtMm8ooo46xIpTY4QXx1nCeQlEFrZocUe%2Fk%2FHyKGuMXeB6qU1mvtYU5LrwLvoPIa9KUq7McrWHwOhEHw8cDj70%2BnlA9W%2BI7vU%2B77tiWBi5N2LYwx5yTvQY6pgGrUGE%2FlWRrxxqXswp15nxUFoYliGN8SarlycBxPam%2BxQtnyS0OSu6ODKQ13eF3FJZ4fIWI9MH819u%2BylqNcsZwZewLXzOXA2BSah%2Ba5YRiAYR3Zo7ye38XYhcBvRul%2Bvg6Lg3dFufsuX%2F5t56oXu6p1Y%2BPx1Qsv0ZbFzNUzDCEzK1uyr97PPdAkGWAGLz3PQ4Uu%2BHP%2Bc8k325bnXBy1DxTbE%2FSPDhF&X-Amz-Signature=16c48b6cf8f302bcca70c36d6db7499f11b05ec59479dcc8535c51547d6c1f60&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ede0dba7-3f63-4051-85fd-51f2f38eeeb5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXCXCC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIDJyyLiOzrkXHQqtMdibJ94qmYv6aCH6qKl9gTpRHGltAiBGM1MTPa%2BmIwwg1OSndtnIoVQ4kZeTQV7lxAAVbqsgFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMnJGF%2FpdvE3t1KB20KtwDrttyrq3z%2FAUjYh9cpZjgDEwoo4G%2BUp82kQ6OhEnUyNcdixoWp0UvcrchCLTRoXlUgMNsPLlf8DHWE5M0LZL2xS%2BzG1jDjAt6pjXOmGffmk9Nhx86%2Bt%2BYvhKAZFJEaP%2FXre949rFo2%2B1iopcLQkK8gFWYucPLHgNdRyQ%2F1wiibU%2B%2BWzlU1ibY36NS%2FqfEeks9VJBqJBOlWtEPP0gpaI5CA10N1EF3%2FP7aGrjYF9mbl%2FvC0TDPYHorQZkBoQuvzc6362XwtOkMgcMLdH1ZokNGKf3DqOJnIaiYinqauK%2BH97mnVYcpH476rg7cbufEysg%2Bp3guB47C0DLrqDtNxC5gH%2BxFMfd9u4OEvUwDhbMp0PTRDnfhBupfClgskfWL9LRhkC5L5pwvMooyfEVy%2FUw32dVmFCV%2BhbD%2BV4jqvKstLY96cccQqYYkawr24gMZ%2BAqUlyVDA%2FBluR8cl5YMc7xbM3cZPTM1vDkVWgzxjNIRLoco%2FGqAC24nqsavbIt50ORfG9MhUdwtOVRykrtMm8ooo46xIpTY4QXx1nCeQlEFrZocUe%2Fk%2FHyKGuMXeB6qU1mvtYU5LrwLvoPIa9KUq7McrWHwOhEHw8cDj70%2BnlA9W%2BI7vU%2B77tiWBi5N2LYwx5yTvQY6pgGrUGE%2FlWRrxxqXswp15nxUFoYliGN8SarlycBxPam%2BxQtnyS0OSu6ODKQ13eF3FJZ4fIWI9MH819u%2BylqNcsZwZewLXzOXA2BSah%2Ba5YRiAYR3Zo7ye38XYhcBvRul%2Bvg6Lg3dFufsuX%2F5t56oXu6p1Y%2BPx1Qsv0ZbFzNUzDCEzK1uyr97PPdAkGWAGLz3PQ4Uu%2BHP%2Bc8k325bnXBy1DxTbE%2FSPDhF&X-Amz-Signature=b5fd50ec044cf6aa0cbacfa69950328463f5178e344cdd241ed131c699f269df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23d540d1-3363-46c0-b145-c20928ff781b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXCXCC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIDJyyLiOzrkXHQqtMdibJ94qmYv6aCH6qKl9gTpRHGltAiBGM1MTPa%2BmIwwg1OSndtnIoVQ4kZeTQV7lxAAVbqsgFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMnJGF%2FpdvE3t1KB20KtwDrttyrq3z%2FAUjYh9cpZjgDEwoo4G%2BUp82kQ6OhEnUyNcdixoWp0UvcrchCLTRoXlUgMNsPLlf8DHWE5M0LZL2xS%2BzG1jDjAt6pjXOmGffmk9Nhx86%2Bt%2BYvhKAZFJEaP%2FXre949rFo2%2B1iopcLQkK8gFWYucPLHgNdRyQ%2F1wiibU%2B%2BWzlU1ibY36NS%2FqfEeks9VJBqJBOlWtEPP0gpaI5CA10N1EF3%2FP7aGrjYF9mbl%2FvC0TDPYHorQZkBoQuvzc6362XwtOkMgcMLdH1ZokNGKf3DqOJnIaiYinqauK%2BH97mnVYcpH476rg7cbufEysg%2Bp3guB47C0DLrqDtNxC5gH%2BxFMfd9u4OEvUwDhbMp0PTRDnfhBupfClgskfWL9LRhkC5L5pwvMooyfEVy%2FUw32dVmFCV%2BhbD%2BV4jqvKstLY96cccQqYYkawr24gMZ%2BAqUlyVDA%2FBluR8cl5YMc7xbM3cZPTM1vDkVWgzxjNIRLoco%2FGqAC24nqsavbIt50ORfG9MhUdwtOVRykrtMm8ooo46xIpTY4QXx1nCeQlEFrZocUe%2Fk%2FHyKGuMXeB6qU1mvtYU5LrwLvoPIa9KUq7McrWHwOhEHw8cDj70%2BnlA9W%2BI7vU%2B77tiWBi5N2LYwx5yTvQY6pgGrUGE%2FlWRrxxqXswp15nxUFoYliGN8SarlycBxPam%2BxQtnyS0OSu6ODKQ13eF3FJZ4fIWI9MH819u%2BylqNcsZwZewLXzOXA2BSah%2Ba5YRiAYR3Zo7ye38XYhcBvRul%2Bvg6Lg3dFufsuX%2F5t56oXu6p1Y%2BPx1Qsv0ZbFzNUzDCEzK1uyr97PPdAkGWAGLz3PQ4Uu%2BHP%2Bc8k325bnXBy1DxTbE%2FSPDhF&X-Amz-Signature=5cef77665174a34a191be5c50c7f1e054e619dca44843550174b60fec0837b53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8af3f76b-b350-4668-99db-ffde6afd7a48/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXCXCC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIDJyyLiOzrkXHQqtMdibJ94qmYv6aCH6qKl9gTpRHGltAiBGM1MTPa%2BmIwwg1OSndtnIoVQ4kZeTQV7lxAAVbqsgFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMnJGF%2FpdvE3t1KB20KtwDrttyrq3z%2FAUjYh9cpZjgDEwoo4G%2BUp82kQ6OhEnUyNcdixoWp0UvcrchCLTRoXlUgMNsPLlf8DHWE5M0LZL2xS%2BzG1jDjAt6pjXOmGffmk9Nhx86%2Bt%2BYvhKAZFJEaP%2FXre949rFo2%2B1iopcLQkK8gFWYucPLHgNdRyQ%2F1wiibU%2B%2BWzlU1ibY36NS%2FqfEeks9VJBqJBOlWtEPP0gpaI5CA10N1EF3%2FP7aGrjYF9mbl%2FvC0TDPYHorQZkBoQuvzc6362XwtOkMgcMLdH1ZokNGKf3DqOJnIaiYinqauK%2BH97mnVYcpH476rg7cbufEysg%2Bp3guB47C0DLrqDtNxC5gH%2BxFMfd9u4OEvUwDhbMp0PTRDnfhBupfClgskfWL9LRhkC5L5pwvMooyfEVy%2FUw32dVmFCV%2BhbD%2BV4jqvKstLY96cccQqYYkawr24gMZ%2BAqUlyVDA%2FBluR8cl5YMc7xbM3cZPTM1vDkVWgzxjNIRLoco%2FGqAC24nqsavbIt50ORfG9MhUdwtOVRykrtMm8ooo46xIpTY4QXx1nCeQlEFrZocUe%2Fk%2FHyKGuMXeB6qU1mvtYU5LrwLvoPIa9KUq7McrWHwOhEHw8cDj70%2BnlA9W%2BI7vU%2B77tiWBi5N2LYwx5yTvQY6pgGrUGE%2FlWRrxxqXswp15nxUFoYliGN8SarlycBxPam%2BxQtnyS0OSu6ODKQ13eF3FJZ4fIWI9MH819u%2BylqNcsZwZewLXzOXA2BSah%2Ba5YRiAYR3Zo7ye38XYhcBvRul%2Bvg6Lg3dFufsuX%2F5t56oXu6p1Y%2BPx1Qsv0ZbFzNUzDCEzK1uyr97PPdAkGWAGLz3PQ4Uu%2BHP%2Bc8k325bnXBy1DxTbE%2FSPDhF&X-Amz-Signature=a1426880beb6eb89ce3ddd4eda4f1f79a12309d028e148c57b91e0012b78a833&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/16d20e8e-68c0-4ad6-83fa-24ee550846a6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXCXCC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIDJyyLiOzrkXHQqtMdibJ94qmYv6aCH6qKl9gTpRHGltAiBGM1MTPa%2BmIwwg1OSndtnIoVQ4kZeTQV7lxAAVbqsgFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMnJGF%2FpdvE3t1KB20KtwDrttyrq3z%2FAUjYh9cpZjgDEwoo4G%2BUp82kQ6OhEnUyNcdixoWp0UvcrchCLTRoXlUgMNsPLlf8DHWE5M0LZL2xS%2BzG1jDjAt6pjXOmGffmk9Nhx86%2Bt%2BYvhKAZFJEaP%2FXre949rFo2%2B1iopcLQkK8gFWYucPLHgNdRyQ%2F1wiibU%2B%2BWzlU1ibY36NS%2FqfEeks9VJBqJBOlWtEPP0gpaI5CA10N1EF3%2FP7aGrjYF9mbl%2FvC0TDPYHorQZkBoQuvzc6362XwtOkMgcMLdH1ZokNGKf3DqOJnIaiYinqauK%2BH97mnVYcpH476rg7cbufEysg%2Bp3guB47C0DLrqDtNxC5gH%2BxFMfd9u4OEvUwDhbMp0PTRDnfhBupfClgskfWL9LRhkC5L5pwvMooyfEVy%2FUw32dVmFCV%2BhbD%2BV4jqvKstLY96cccQqYYkawr24gMZ%2BAqUlyVDA%2FBluR8cl5YMc7xbM3cZPTM1vDkVWgzxjNIRLoco%2FGqAC24nqsavbIt50ORfG9MhUdwtOVRykrtMm8ooo46xIpTY4QXx1nCeQlEFrZocUe%2Fk%2FHyKGuMXeB6qU1mvtYU5LrwLvoPIa9KUq7McrWHwOhEHw8cDj70%2BnlA9W%2BI7vU%2B77tiWBi5N2LYwx5yTvQY6pgGrUGE%2FlWRrxxqXswp15nxUFoYliGN8SarlycBxPam%2BxQtnyS0OSu6ODKQ13eF3FJZ4fIWI9MH819u%2BylqNcsZwZewLXzOXA2BSah%2Ba5YRiAYR3Zo7ye38XYhcBvRul%2Bvg6Lg3dFufsuX%2F5t56oXu6p1Y%2BPx1Qsv0ZbFzNUzDCEzK1uyr97PPdAkGWAGLz3PQ4Uu%2BHP%2Bc8k325bnXBy1DxTbE%2FSPDhF&X-Amz-Signature=835f61bbb6e1c2ae65e382cb2eef79b162252ef832b2606d2e08b29cbc01aa52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/73a2c105-2ca5-46a7-974c-ec918cf62c91/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXCXCC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIDJyyLiOzrkXHQqtMdibJ94qmYv6aCH6qKl9gTpRHGltAiBGM1MTPa%2BmIwwg1OSndtnIoVQ4kZeTQV7lxAAVbqsgFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMnJGF%2FpdvE3t1KB20KtwDrttyrq3z%2FAUjYh9cpZjgDEwoo4G%2BUp82kQ6OhEnUyNcdixoWp0UvcrchCLTRoXlUgMNsPLlf8DHWE5M0LZL2xS%2BzG1jDjAt6pjXOmGffmk9Nhx86%2Bt%2BYvhKAZFJEaP%2FXre949rFo2%2B1iopcLQkK8gFWYucPLHgNdRyQ%2F1wiibU%2B%2BWzlU1ibY36NS%2FqfEeks9VJBqJBOlWtEPP0gpaI5CA10N1EF3%2FP7aGrjYF9mbl%2FvC0TDPYHorQZkBoQuvzc6362XwtOkMgcMLdH1ZokNGKf3DqOJnIaiYinqauK%2BH97mnVYcpH476rg7cbufEysg%2Bp3guB47C0DLrqDtNxC5gH%2BxFMfd9u4OEvUwDhbMp0PTRDnfhBupfClgskfWL9LRhkC5L5pwvMooyfEVy%2FUw32dVmFCV%2BhbD%2BV4jqvKstLY96cccQqYYkawr24gMZ%2BAqUlyVDA%2FBluR8cl5YMc7xbM3cZPTM1vDkVWgzxjNIRLoco%2FGqAC24nqsavbIt50ORfG9MhUdwtOVRykrtMm8ooo46xIpTY4QXx1nCeQlEFrZocUe%2Fk%2FHyKGuMXeB6qU1mvtYU5LrwLvoPIa9KUq7McrWHwOhEHw8cDj70%2BnlA9W%2BI7vU%2B77tiWBi5N2LYwx5yTvQY6pgGrUGE%2FlWRrxxqXswp15nxUFoYliGN8SarlycBxPam%2BxQtnyS0OSu6ODKQ13eF3FJZ4fIWI9MH819u%2BylqNcsZwZewLXzOXA2BSah%2Ba5YRiAYR3Zo7ye38XYhcBvRul%2Bvg6Lg3dFufsuX%2F5t56oXu6p1Y%2BPx1Qsv0ZbFzNUzDCEzK1uyr97PPdAkGWAGLz3PQ4Uu%2BHP%2Bc8k325bnXBy1DxTbE%2FSPDhF&X-Amz-Signature=4aab47110e2da40cae6e77d7b6dfa45d59a9a14bed5d62d504d8ea5784448f3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7d3cdfd2-3a59-4bf7-8d34-4b4314e49abd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXCXCC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIDJyyLiOzrkXHQqtMdibJ94qmYv6aCH6qKl9gTpRHGltAiBGM1MTPa%2BmIwwg1OSndtnIoVQ4kZeTQV7lxAAVbqsgFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMnJGF%2FpdvE3t1KB20KtwDrttyrq3z%2FAUjYh9cpZjgDEwoo4G%2BUp82kQ6OhEnUyNcdixoWp0UvcrchCLTRoXlUgMNsPLlf8DHWE5M0LZL2xS%2BzG1jDjAt6pjXOmGffmk9Nhx86%2Bt%2BYvhKAZFJEaP%2FXre949rFo2%2B1iopcLQkK8gFWYucPLHgNdRyQ%2F1wiibU%2B%2BWzlU1ibY36NS%2FqfEeks9VJBqJBOlWtEPP0gpaI5CA10N1EF3%2FP7aGrjYF9mbl%2FvC0TDPYHorQZkBoQuvzc6362XwtOkMgcMLdH1ZokNGKf3DqOJnIaiYinqauK%2BH97mnVYcpH476rg7cbufEysg%2Bp3guB47C0DLrqDtNxC5gH%2BxFMfd9u4OEvUwDhbMp0PTRDnfhBupfClgskfWL9LRhkC5L5pwvMooyfEVy%2FUw32dVmFCV%2BhbD%2BV4jqvKstLY96cccQqYYkawr24gMZ%2BAqUlyVDA%2FBluR8cl5YMc7xbM3cZPTM1vDkVWgzxjNIRLoco%2FGqAC24nqsavbIt50ORfG9MhUdwtOVRykrtMm8ooo46xIpTY4QXx1nCeQlEFrZocUe%2Fk%2FHyKGuMXeB6qU1mvtYU5LrwLvoPIa9KUq7McrWHwOhEHw8cDj70%2BnlA9W%2BI7vU%2B77tiWBi5N2LYwx5yTvQY6pgGrUGE%2FlWRrxxqXswp15nxUFoYliGN8SarlycBxPam%2BxQtnyS0OSu6ODKQ13eF3FJZ4fIWI9MH819u%2BylqNcsZwZewLXzOXA2BSah%2Ba5YRiAYR3Zo7ye38XYhcBvRul%2Bvg6Lg3dFufsuX%2F5t56oXu6p1Y%2BPx1Qsv0ZbFzNUzDCEzK1uyr97PPdAkGWAGLz3PQ4Uu%2BHP%2Bc8k325bnXBy1DxTbE%2FSPDhF&X-Amz-Signature=6526044b7670c16022671bc2cdc90185bf74f9d478ec068304955d8b8b29b29e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74024f1a-9e67-4a06-856e-ff0920d20ba0/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXCXCC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIDJyyLiOzrkXHQqtMdibJ94qmYv6aCH6qKl9gTpRHGltAiBGM1MTPa%2BmIwwg1OSndtnIoVQ4kZeTQV7lxAAVbqsgFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMnJGF%2FpdvE3t1KB20KtwDrttyrq3z%2FAUjYh9cpZjgDEwoo4G%2BUp82kQ6OhEnUyNcdixoWp0UvcrchCLTRoXlUgMNsPLlf8DHWE5M0LZL2xS%2BzG1jDjAt6pjXOmGffmk9Nhx86%2Bt%2BYvhKAZFJEaP%2FXre949rFo2%2B1iopcLQkK8gFWYucPLHgNdRyQ%2F1wiibU%2B%2BWzlU1ibY36NS%2FqfEeks9VJBqJBOlWtEPP0gpaI5CA10N1EF3%2FP7aGrjYF9mbl%2FvC0TDPYHorQZkBoQuvzc6362XwtOkMgcMLdH1ZokNGKf3DqOJnIaiYinqauK%2BH97mnVYcpH476rg7cbufEysg%2Bp3guB47C0DLrqDtNxC5gH%2BxFMfd9u4OEvUwDhbMp0PTRDnfhBupfClgskfWL9LRhkC5L5pwvMooyfEVy%2FUw32dVmFCV%2BhbD%2BV4jqvKstLY96cccQqYYkawr24gMZ%2BAqUlyVDA%2FBluR8cl5YMc7xbM3cZPTM1vDkVWgzxjNIRLoco%2FGqAC24nqsavbIt50ORfG9MhUdwtOVRykrtMm8ooo46xIpTY4QXx1nCeQlEFrZocUe%2Fk%2FHyKGuMXeB6qU1mvtYU5LrwLvoPIa9KUq7McrWHwOhEHw8cDj70%2BnlA9W%2BI7vU%2B77tiWBi5N2LYwx5yTvQY6pgGrUGE%2FlWRrxxqXswp15nxUFoYliGN8SarlycBxPam%2BxQtnyS0OSu6ODKQ13eF3FJZ4fIWI9MH819u%2BylqNcsZwZewLXzOXA2BSah%2Ba5YRiAYR3Zo7ye38XYhcBvRul%2Bvg6Lg3dFufsuX%2F5t56oXu6p1Y%2BPx1Qsv0ZbFzNUzDCEzK1uyr97PPdAkGWAGLz3PQ4Uu%2BHP%2Bc8k325bnXBy1DxTbE%2FSPDhF&X-Amz-Signature=76a88b88d8169ae6c48a34f615ed7f3f5519c76f894039ee87227549925b1209&X-Amz-SignedHeaders=host&x-id=GetObject)
![Figure2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/14af08ae-a84c-4391-95ac-9cee37c62973/Figure2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAXCXCC6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIDJyyLiOzrkXHQqtMdibJ94qmYv6aCH6qKl9gTpRHGltAiBGM1MTPa%2BmIwwg1OSndtnIoVQ4kZeTQV7lxAAVbqsgFCr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMnJGF%2FpdvE3t1KB20KtwDrttyrq3z%2FAUjYh9cpZjgDEwoo4G%2BUp82kQ6OhEnUyNcdixoWp0UvcrchCLTRoXlUgMNsPLlf8DHWE5M0LZL2xS%2BzG1jDjAt6pjXOmGffmk9Nhx86%2Bt%2BYvhKAZFJEaP%2FXre949rFo2%2B1iopcLQkK8gFWYucPLHgNdRyQ%2F1wiibU%2B%2BWzlU1ibY36NS%2FqfEeks9VJBqJBOlWtEPP0gpaI5CA10N1EF3%2FP7aGrjYF9mbl%2FvC0TDPYHorQZkBoQuvzc6362XwtOkMgcMLdH1ZokNGKf3DqOJnIaiYinqauK%2BH97mnVYcpH476rg7cbufEysg%2Bp3guB47C0DLrqDtNxC5gH%2BxFMfd9u4OEvUwDhbMp0PTRDnfhBupfClgskfWL9LRhkC5L5pwvMooyfEVy%2FUw32dVmFCV%2BhbD%2BV4jqvKstLY96cccQqYYkawr24gMZ%2BAqUlyVDA%2FBluR8cl5YMc7xbM3cZPTM1vDkVWgzxjNIRLoco%2FGqAC24nqsavbIt50ORfG9MhUdwtOVRykrtMm8ooo46xIpTY4QXx1nCeQlEFrZocUe%2Fk%2FHyKGuMXeB6qU1mvtYU5LrwLvoPIa9KUq7McrWHwOhEHw8cDj70%2BnlA9W%2BI7vU%2B77tiWBi5N2LYwx5yTvQY6pgGrUGE%2FlWRrxxqXswp15nxUFoYliGN8SarlycBxPam%2BxQtnyS0OSu6ODKQ13eF3FJZ4fIWI9MH819u%2BylqNcsZwZewLXzOXA2BSah%2Ba5YRiAYR3Zo7ye38XYhcBvRul%2Bvg6Lg3dFufsuX%2F5t56oXu6p1Y%2BPx1Qsv0ZbFzNUzDCEzK1uyr97PPdAkGWAGLz3PQ4Uu%2BHP%2Bc8k325bnXBy1DxTbE%2FSPDhF&X-Amz-Signature=6d4ac18f8f80720a0e42a5ab51b3d0b4ae552bae1c037a8453d1ac4c8175d4cb&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Characteristics of K-Means
- **Partition-Based**: Divides data into K clusters based on similarity.
- **Efficiency**: Relatively efficient on medium and large-sized datasets.
- **Cluster Shape**: Produces spherical clusters as it groups data around centroids.
- **Pre-Specified K**: Requires the number of clusters (K) to be specified beforehand, which can be challenging.
### Conclusion
K-Means clustering is a widely-used algorithm for grouping data into clusters based on feature similarity. The algorithm's effectiveness is often evaluated using metrics such as WCSS and the elbow method to determine the optimal number of clusters.