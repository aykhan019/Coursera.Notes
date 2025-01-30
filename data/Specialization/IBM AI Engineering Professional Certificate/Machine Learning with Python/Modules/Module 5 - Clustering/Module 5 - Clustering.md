

# Module 5: Clustering
## Clustering: An Introduction
### Overview of Clustering
Clustering is an unsupervised learning technique used to group similar data points into clusters based on their characteristics. This method is commonly applied in various domains to segment data, identify patterns, and make predictions.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9cb01ce9-5e0d-49ef-8f43-c9db38fbc0e0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7OSVVZV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpPCIZl1eAy3zu6cJwIG%2BDF3q6Loq%2B5pf%2FM9EQc5hVxAiAg38c2%2F%2Bxa2WqritV0%2FNSr5ZmDimh3cL63RgMInBiUgyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMViqzS7zJ9dtA0pm4KtwDsJIhaHX56I78IrsjNIt2PpZ9G8pmKXBorpV2r4rtdjRfEf2If7Srwg8X2roLTObak%2FGsfKe%2F6duQiPO8UNz3ZbnqDEufjHvAEpQBMtp1cwrsB4Smt8ZMiBKwKbOzDJevQYy1mkZCNT7fY0njeJrKDRudmW4hgNdehd9fEkrxJ2z0EEN9pjsxzZqT7Fc8vHYp8UVrlb%2BfhwCnbcwv0ehzXWmR%2By7LONfVmYS1T7p2KQO8jNzUAfdR91H%2FSY4P%2BfFJzqhgonoY54xMRwZAiEdEZbE5cg4jCNCvC0uVNdxzt0DXEA1HwPJdpXphpbMN9NqG1RrMacyb2Xv4W044kxmqxHPGH9vBf6VsN5%2ByoZZ%2FTiBxg3IEqX4gdDQA8S7vB5qS6zlEctcPPLaBbs%2BXWgPxF0%2FkRraFA7ogPPLbbNa1gMp5QkAKhWglqw4h%2F9VP8%2BVXVkNC56YHKgb4AF1DKme9wYyOCgvKhAKEGjdNFGfj9OOoW7MqXlYoikp64ObAfT80bQS23mQ1Kdr%2BEM%2FIlslsKTnArKm6Wn02I4sq14A%2BEg8%2BMkqObWWRyC4aTHcv1XLV%2F7%2BaNProLNPYAOdYyd42nLnYm0am9XD8PgSbFbNt%2BCbGY7tK9Haf2TSq3mQwhpjuvAY6pgG4EUxJyn4yjdsK%2BbxN2hhxEFUQMtoFNGTEEjPNHR95Kfqu10nqntTWc%2Bx%2FRvOiVdRxi3Ws8PXBqWJoVf0XQmyoCQYxDf88Jx91JvsZiLaUOeZwOuB8QBvvr6GchqqiPE%2BOAZAMKeienmbe2bSY%2FHb8kedMs2kAjqus6Z7IbnB2J8x7KdNMMisSFQoAUJ9xHlIAbH%2FzJiU%2FsGstlrD%2FGyZFKnD5y4wE&X-Amz-Signature=f30351db92f579e865857cc0e0f35576f49b9c923d6c2856fac6c377f2ed0671&X-Amz-SignedHeaders=host&x-id=GetObject)
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ede0dba7-3f63-4051-85fd-51f2f38eeeb5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7OSVVZV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpPCIZl1eAy3zu6cJwIG%2BDF3q6Loq%2B5pf%2FM9EQc5hVxAiAg38c2%2F%2Bxa2WqritV0%2FNSr5ZmDimh3cL63RgMInBiUgyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMViqzS7zJ9dtA0pm4KtwDsJIhaHX56I78IrsjNIt2PpZ9G8pmKXBorpV2r4rtdjRfEf2If7Srwg8X2roLTObak%2FGsfKe%2F6duQiPO8UNz3ZbnqDEufjHvAEpQBMtp1cwrsB4Smt8ZMiBKwKbOzDJevQYy1mkZCNT7fY0njeJrKDRudmW4hgNdehd9fEkrxJ2z0EEN9pjsxzZqT7Fc8vHYp8UVrlb%2BfhwCnbcwv0ehzXWmR%2By7LONfVmYS1T7p2KQO8jNzUAfdR91H%2FSY4P%2BfFJzqhgonoY54xMRwZAiEdEZbE5cg4jCNCvC0uVNdxzt0DXEA1HwPJdpXphpbMN9NqG1RrMacyb2Xv4W044kxmqxHPGH9vBf6VsN5%2ByoZZ%2FTiBxg3IEqX4gdDQA8S7vB5qS6zlEctcPPLaBbs%2BXWgPxF0%2FkRraFA7ogPPLbbNa1gMp5QkAKhWglqw4h%2F9VP8%2BVXVkNC56YHKgb4AF1DKme9wYyOCgvKhAKEGjdNFGfj9OOoW7MqXlYoikp64ObAfT80bQS23mQ1Kdr%2BEM%2FIlslsKTnArKm6Wn02I4sq14A%2BEg8%2BMkqObWWRyC4aTHcv1XLV%2F7%2BaNProLNPYAOdYyd42nLnYm0am9XD8PgSbFbNt%2BCbGY7tK9Haf2TSq3mQwhpjuvAY6pgG4EUxJyn4yjdsK%2BbxN2hhxEFUQMtoFNGTEEjPNHR95Kfqu10nqntTWc%2Bx%2FRvOiVdRxi3Ws8PXBqWJoVf0XQmyoCQYxDf88Jx91JvsZiLaUOeZwOuB8QBvvr6GchqqiPE%2BOAZAMKeienmbe2bSY%2FHb8kedMs2kAjqus6Z7IbnB2J8x7KdNMMisSFQoAUJ9xHlIAbH%2FzJiU%2FsGstlrD%2FGyZFKnD5y4wE&X-Amz-Signature=4f86d38fdd5ba4c6a2c14cc8a148e3550c770b06c90a921279dd3a7bbf903cf4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23d540d1-3363-46c0-b145-c20928ff781b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7OSVVZV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpPCIZl1eAy3zu6cJwIG%2BDF3q6Loq%2B5pf%2FM9EQc5hVxAiAg38c2%2F%2Bxa2WqritV0%2FNSr5ZmDimh3cL63RgMInBiUgyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMViqzS7zJ9dtA0pm4KtwDsJIhaHX56I78IrsjNIt2PpZ9G8pmKXBorpV2r4rtdjRfEf2If7Srwg8X2roLTObak%2FGsfKe%2F6duQiPO8UNz3ZbnqDEufjHvAEpQBMtp1cwrsB4Smt8ZMiBKwKbOzDJevQYy1mkZCNT7fY0njeJrKDRudmW4hgNdehd9fEkrxJ2z0EEN9pjsxzZqT7Fc8vHYp8UVrlb%2BfhwCnbcwv0ehzXWmR%2By7LONfVmYS1T7p2KQO8jNzUAfdR91H%2FSY4P%2BfFJzqhgonoY54xMRwZAiEdEZbE5cg4jCNCvC0uVNdxzt0DXEA1HwPJdpXphpbMN9NqG1RrMacyb2Xv4W044kxmqxHPGH9vBf6VsN5%2ByoZZ%2FTiBxg3IEqX4gdDQA8S7vB5qS6zlEctcPPLaBbs%2BXWgPxF0%2FkRraFA7ogPPLbbNa1gMp5QkAKhWglqw4h%2F9VP8%2BVXVkNC56YHKgb4AF1DKme9wYyOCgvKhAKEGjdNFGfj9OOoW7MqXlYoikp64ObAfT80bQS23mQ1Kdr%2BEM%2FIlslsKTnArKm6Wn02I4sq14A%2BEg8%2BMkqObWWRyC4aTHcv1XLV%2F7%2BaNProLNPYAOdYyd42nLnYm0am9XD8PgSbFbNt%2BCbGY7tK9Haf2TSq3mQwhpjuvAY6pgG4EUxJyn4yjdsK%2BbxN2hhxEFUQMtoFNGTEEjPNHR95Kfqu10nqntTWc%2Bx%2FRvOiVdRxi3Ws8PXBqWJoVf0XQmyoCQYxDf88Jx91JvsZiLaUOeZwOuB8QBvvr6GchqqiPE%2BOAZAMKeienmbe2bSY%2FHb8kedMs2kAjqus6Z7IbnB2J8x7KdNMMisSFQoAUJ9xHlIAbH%2FzJiU%2FsGstlrD%2FGyZFKnD5y4wE&X-Amz-Signature=4ae344442c5613a67d859d3851864034d0c9e8a374f60c35b159f11722c9deb0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8af3f76b-b350-4668-99db-ffde6afd7a48/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7OSVVZV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpPCIZl1eAy3zu6cJwIG%2BDF3q6Loq%2B5pf%2FM9EQc5hVxAiAg38c2%2F%2Bxa2WqritV0%2FNSr5ZmDimh3cL63RgMInBiUgyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMViqzS7zJ9dtA0pm4KtwDsJIhaHX56I78IrsjNIt2PpZ9G8pmKXBorpV2r4rtdjRfEf2If7Srwg8X2roLTObak%2FGsfKe%2F6duQiPO8UNz3ZbnqDEufjHvAEpQBMtp1cwrsB4Smt8ZMiBKwKbOzDJevQYy1mkZCNT7fY0njeJrKDRudmW4hgNdehd9fEkrxJ2z0EEN9pjsxzZqT7Fc8vHYp8UVrlb%2BfhwCnbcwv0ehzXWmR%2By7LONfVmYS1T7p2KQO8jNzUAfdR91H%2FSY4P%2BfFJzqhgonoY54xMRwZAiEdEZbE5cg4jCNCvC0uVNdxzt0DXEA1HwPJdpXphpbMN9NqG1RrMacyb2Xv4W044kxmqxHPGH9vBf6VsN5%2ByoZZ%2FTiBxg3IEqX4gdDQA8S7vB5qS6zlEctcPPLaBbs%2BXWgPxF0%2FkRraFA7ogPPLbbNa1gMp5QkAKhWglqw4h%2F9VP8%2BVXVkNC56YHKgb4AF1DKme9wYyOCgvKhAKEGjdNFGfj9OOoW7MqXlYoikp64ObAfT80bQS23mQ1Kdr%2BEM%2FIlslsKTnArKm6Wn02I4sq14A%2BEg8%2BMkqObWWRyC4aTHcv1XLV%2F7%2BaNProLNPYAOdYyd42nLnYm0am9XD8PgSbFbNt%2BCbGY7tK9Haf2TSq3mQwhpjuvAY6pgG4EUxJyn4yjdsK%2BbxN2hhxEFUQMtoFNGTEEjPNHR95Kfqu10nqntTWc%2Bx%2FRvOiVdRxi3Ws8PXBqWJoVf0XQmyoCQYxDf88Jx91JvsZiLaUOeZwOuB8QBvvr6GchqqiPE%2BOAZAMKeienmbe2bSY%2FHb8kedMs2kAjqus6Z7IbnB2J8x7KdNMMisSFQoAUJ9xHlIAbH%2FzJiU%2FsGstlrD%2FGyZFKnD5y4wE&X-Amz-Signature=dc29d35ef9a44d5f517c1354acb3c153e0a649d00923e04e949067b76c3f59c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/16d20e8e-68c0-4ad6-83fa-24ee550846a6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7OSVVZV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpPCIZl1eAy3zu6cJwIG%2BDF3q6Loq%2B5pf%2FM9EQc5hVxAiAg38c2%2F%2Bxa2WqritV0%2FNSr5ZmDimh3cL63RgMInBiUgyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMViqzS7zJ9dtA0pm4KtwDsJIhaHX56I78IrsjNIt2PpZ9G8pmKXBorpV2r4rtdjRfEf2If7Srwg8X2roLTObak%2FGsfKe%2F6duQiPO8UNz3ZbnqDEufjHvAEpQBMtp1cwrsB4Smt8ZMiBKwKbOzDJevQYy1mkZCNT7fY0njeJrKDRudmW4hgNdehd9fEkrxJ2z0EEN9pjsxzZqT7Fc8vHYp8UVrlb%2BfhwCnbcwv0ehzXWmR%2By7LONfVmYS1T7p2KQO8jNzUAfdR91H%2FSY4P%2BfFJzqhgonoY54xMRwZAiEdEZbE5cg4jCNCvC0uVNdxzt0DXEA1HwPJdpXphpbMN9NqG1RrMacyb2Xv4W044kxmqxHPGH9vBf6VsN5%2ByoZZ%2FTiBxg3IEqX4gdDQA8S7vB5qS6zlEctcPPLaBbs%2BXWgPxF0%2FkRraFA7ogPPLbbNa1gMp5QkAKhWglqw4h%2F9VP8%2BVXVkNC56YHKgb4AF1DKme9wYyOCgvKhAKEGjdNFGfj9OOoW7MqXlYoikp64ObAfT80bQS23mQ1Kdr%2BEM%2FIlslsKTnArKm6Wn02I4sq14A%2BEg8%2BMkqObWWRyC4aTHcv1XLV%2F7%2BaNProLNPYAOdYyd42nLnYm0am9XD8PgSbFbNt%2BCbGY7tK9Haf2TSq3mQwhpjuvAY6pgG4EUxJyn4yjdsK%2BbxN2hhxEFUQMtoFNGTEEjPNHR95Kfqu10nqntTWc%2Bx%2FRvOiVdRxi3Ws8PXBqWJoVf0XQmyoCQYxDf88Jx91JvsZiLaUOeZwOuB8QBvvr6GchqqiPE%2BOAZAMKeienmbe2bSY%2FHb8kedMs2kAjqus6Z7IbnB2J8x7KdNMMisSFQoAUJ9xHlIAbH%2FzJiU%2FsGstlrD%2FGyZFKnD5y4wE&X-Amz-Signature=2696fa3ebb1e30bd98c99dc7d7fd30dd205981e0bea99823953f59e70b03a5d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/73a2c105-2ca5-46a7-974c-ec918cf62c91/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7OSVVZV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpPCIZl1eAy3zu6cJwIG%2BDF3q6Loq%2B5pf%2FM9EQc5hVxAiAg38c2%2F%2Bxa2WqritV0%2FNSr5ZmDimh3cL63RgMInBiUgyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMViqzS7zJ9dtA0pm4KtwDsJIhaHX56I78IrsjNIt2PpZ9G8pmKXBorpV2r4rtdjRfEf2If7Srwg8X2roLTObak%2FGsfKe%2F6duQiPO8UNz3ZbnqDEufjHvAEpQBMtp1cwrsB4Smt8ZMiBKwKbOzDJevQYy1mkZCNT7fY0njeJrKDRudmW4hgNdehd9fEkrxJ2z0EEN9pjsxzZqT7Fc8vHYp8UVrlb%2BfhwCnbcwv0ehzXWmR%2By7LONfVmYS1T7p2KQO8jNzUAfdR91H%2FSY4P%2BfFJzqhgonoY54xMRwZAiEdEZbE5cg4jCNCvC0uVNdxzt0DXEA1HwPJdpXphpbMN9NqG1RrMacyb2Xv4W044kxmqxHPGH9vBf6VsN5%2ByoZZ%2FTiBxg3IEqX4gdDQA8S7vB5qS6zlEctcPPLaBbs%2BXWgPxF0%2FkRraFA7ogPPLbbNa1gMp5QkAKhWglqw4h%2F9VP8%2BVXVkNC56YHKgb4AF1DKme9wYyOCgvKhAKEGjdNFGfj9OOoW7MqXlYoikp64ObAfT80bQS23mQ1Kdr%2BEM%2FIlslsKTnArKm6Wn02I4sq14A%2BEg8%2BMkqObWWRyC4aTHcv1XLV%2F7%2BaNProLNPYAOdYyd42nLnYm0am9XD8PgSbFbNt%2BCbGY7tK9Haf2TSq3mQwhpjuvAY6pgG4EUxJyn4yjdsK%2BbxN2hhxEFUQMtoFNGTEEjPNHR95Kfqu10nqntTWc%2Bx%2FRvOiVdRxi3Ws8PXBqWJoVf0XQmyoCQYxDf88Jx91JvsZiLaUOeZwOuB8QBvvr6GchqqiPE%2BOAZAMKeienmbe2bSY%2FHb8kedMs2kAjqus6Z7IbnB2J8x7KdNMMisSFQoAUJ9xHlIAbH%2FzJiU%2FsGstlrD%2FGyZFKnD5y4wE&X-Amz-Signature=44a656c2c4c31951dab61d0d552becefd986c825e682f45742083c3de02e5b2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7d3cdfd2-3a59-4bf7-8d34-4b4314e49abd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7OSVVZV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpPCIZl1eAy3zu6cJwIG%2BDF3q6Loq%2B5pf%2FM9EQc5hVxAiAg38c2%2F%2Bxa2WqritV0%2FNSr5ZmDimh3cL63RgMInBiUgyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMViqzS7zJ9dtA0pm4KtwDsJIhaHX56I78IrsjNIt2PpZ9G8pmKXBorpV2r4rtdjRfEf2If7Srwg8X2roLTObak%2FGsfKe%2F6duQiPO8UNz3ZbnqDEufjHvAEpQBMtp1cwrsB4Smt8ZMiBKwKbOzDJevQYy1mkZCNT7fY0njeJrKDRudmW4hgNdehd9fEkrxJ2z0EEN9pjsxzZqT7Fc8vHYp8UVrlb%2BfhwCnbcwv0ehzXWmR%2By7LONfVmYS1T7p2KQO8jNzUAfdR91H%2FSY4P%2BfFJzqhgonoY54xMRwZAiEdEZbE5cg4jCNCvC0uVNdxzt0DXEA1HwPJdpXphpbMN9NqG1RrMacyb2Xv4W044kxmqxHPGH9vBf6VsN5%2ByoZZ%2FTiBxg3IEqX4gdDQA8S7vB5qS6zlEctcPPLaBbs%2BXWgPxF0%2FkRraFA7ogPPLbbNa1gMp5QkAKhWglqw4h%2F9VP8%2BVXVkNC56YHKgb4AF1DKme9wYyOCgvKhAKEGjdNFGfj9OOoW7MqXlYoikp64ObAfT80bQS23mQ1Kdr%2BEM%2FIlslsKTnArKm6Wn02I4sq14A%2BEg8%2BMkqObWWRyC4aTHcv1XLV%2F7%2BaNProLNPYAOdYyd42nLnYm0am9XD8PgSbFbNt%2BCbGY7tK9Haf2TSq3mQwhpjuvAY6pgG4EUxJyn4yjdsK%2BbxN2hhxEFUQMtoFNGTEEjPNHR95Kfqu10nqntTWc%2Bx%2FRvOiVdRxi3Ws8PXBqWJoVf0XQmyoCQYxDf88Jx91JvsZiLaUOeZwOuB8QBvvr6GchqqiPE%2BOAZAMKeienmbe2bSY%2FHb8kedMs2kAjqus6Z7IbnB2J8x7KdNMMisSFQoAUJ9xHlIAbH%2FzJiU%2FsGstlrD%2FGyZFKnD5y4wE&X-Amz-Signature=2a2c8383fcf46871ec1c7569c3c077110478292cf31321e8b089d8848788675f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Figure_1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74024f1a-9e67-4a06-856e-ff0920d20ba0/Figure_1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7OSVVZV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpPCIZl1eAy3zu6cJwIG%2BDF3q6Loq%2B5pf%2FM9EQc5hVxAiAg38c2%2F%2Bxa2WqritV0%2FNSr5ZmDimh3cL63RgMInBiUgyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMViqzS7zJ9dtA0pm4KtwDsJIhaHX56I78IrsjNIt2PpZ9G8pmKXBorpV2r4rtdjRfEf2If7Srwg8X2roLTObak%2FGsfKe%2F6duQiPO8UNz3ZbnqDEufjHvAEpQBMtp1cwrsB4Smt8ZMiBKwKbOzDJevQYy1mkZCNT7fY0njeJrKDRudmW4hgNdehd9fEkrxJ2z0EEN9pjsxzZqT7Fc8vHYp8UVrlb%2BfhwCnbcwv0ehzXWmR%2By7LONfVmYS1T7p2KQO8jNzUAfdR91H%2FSY4P%2BfFJzqhgonoY54xMRwZAiEdEZbE5cg4jCNCvC0uVNdxzt0DXEA1HwPJdpXphpbMN9NqG1RrMacyb2Xv4W044kxmqxHPGH9vBf6VsN5%2ByoZZ%2FTiBxg3IEqX4gdDQA8S7vB5qS6zlEctcPPLaBbs%2BXWgPxF0%2FkRraFA7ogPPLbbNa1gMp5QkAKhWglqw4h%2F9VP8%2BVXVkNC56YHKgb4AF1DKme9wYyOCgvKhAKEGjdNFGfj9OOoW7MqXlYoikp64ObAfT80bQS23mQ1Kdr%2BEM%2FIlslsKTnArKm6Wn02I4sq14A%2BEg8%2BMkqObWWRyC4aTHcv1XLV%2F7%2BaNProLNPYAOdYyd42nLnYm0am9XD8PgSbFbNt%2BCbGY7tK9Haf2TSq3mQwhpjuvAY6pgG4EUxJyn4yjdsK%2BbxN2hhxEFUQMtoFNGTEEjPNHR95Kfqu10nqntTWc%2Bx%2FRvOiVdRxi3Ws8PXBqWJoVf0XQmyoCQYxDf88Jx91JvsZiLaUOeZwOuB8QBvvr6GchqqiPE%2BOAZAMKeienmbe2bSY%2FHb8kedMs2kAjqus6Z7IbnB2J8x7KdNMMisSFQoAUJ9xHlIAbH%2FzJiU%2FsGstlrD%2FGyZFKnD5y4wE&X-Amz-Signature=249d79bc9de019a5eaec9fe5727dfb51b5f59798081e5a28ddb18172f39ebe4c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Figure2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/14af08ae-a84c-4391-95ac-9cee37c62973/Figure2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7OSVVZV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpPCIZl1eAy3zu6cJwIG%2BDF3q6Loq%2B5pf%2FM9EQc5hVxAiAg38c2%2F%2Bxa2WqritV0%2FNSr5ZmDimh3cL63RgMInBiUgyqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMViqzS7zJ9dtA0pm4KtwDsJIhaHX56I78IrsjNIt2PpZ9G8pmKXBorpV2r4rtdjRfEf2If7Srwg8X2roLTObak%2FGsfKe%2F6duQiPO8UNz3ZbnqDEufjHvAEpQBMtp1cwrsB4Smt8ZMiBKwKbOzDJevQYy1mkZCNT7fY0njeJrKDRudmW4hgNdehd9fEkrxJ2z0EEN9pjsxzZqT7Fc8vHYp8UVrlb%2BfhwCnbcwv0ehzXWmR%2By7LONfVmYS1T7p2KQO8jNzUAfdR91H%2FSY4P%2BfFJzqhgonoY54xMRwZAiEdEZbE5cg4jCNCvC0uVNdxzt0DXEA1HwPJdpXphpbMN9NqG1RrMacyb2Xv4W044kxmqxHPGH9vBf6VsN5%2ByoZZ%2FTiBxg3IEqX4gdDQA8S7vB5qS6zlEctcPPLaBbs%2BXWgPxF0%2FkRraFA7ogPPLbbNa1gMp5QkAKhWglqw4h%2F9VP8%2BVXVkNC56YHKgb4AF1DKme9wYyOCgvKhAKEGjdNFGfj9OOoW7MqXlYoikp64ObAfT80bQS23mQ1Kdr%2BEM%2FIlslsKTnArKm6Wn02I4sq14A%2BEg8%2BMkqObWWRyC4aTHcv1XLV%2F7%2BaNProLNPYAOdYyd42nLnYm0am9XD8PgSbFbNt%2BCbGY7tK9Haf2TSq3mQwhpjuvAY6pgG4EUxJyn4yjdsK%2BbxN2hhxEFUQMtoFNGTEEjPNHR95Kfqu10nqntTWc%2Bx%2FRvOiVdRxi3Ws8PXBqWJoVf0XQmyoCQYxDf88Jx91JvsZiLaUOeZwOuB8QBvvr6GchqqiPE%2BOAZAMKeienmbe2bSY%2FHb8kedMs2kAjqus6Z7IbnB2J8x7KdNMMisSFQoAUJ9xHlIAbH%2FzJiU%2FsGstlrD%2FGyZFKnD5y4wE&X-Amz-Signature=23b710d9770aced49cc9ad1962a3e3ba94d5e6e86a41a19e0d544615867e0b8c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Key Characteristics of K-Means
- **Partition-Based**: Divides data into K clusters based on similarity.
- **Efficiency**: Relatively efficient on medium and large-sized datasets.
- **Cluster Shape**: Produces spherical clusters as it groups data around centroids.
- **Pre-Specified K**: Requires the number of clusters (K) to be specified beforehand, which can be challenging.
### Conclusion
K-Means clustering is a widely-used algorithm for grouping data into clusters based on feature similarity. The algorithm's effectiveness is often evaluated using metrics such as WCSS and the elbow method to determine the optimal number of clusters.