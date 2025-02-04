

# Module 1: Introduction to Machine Learning
### What is Machine Learning?
Machine Learning is a subfield of computer science that gives computers the ability to learn from data without being explicitly programmed. It involves the development of algorithms that can recognize patterns, make decisions, and improve themselves over time.
### How Does Machine Learning Work?
Machine Learning algorithms, inspired by the human learning process, iteratively learn from data. These algorithms allow computers to discover hidden insights and patterns within large datasets. The models created through Machine Learning can assist in a variety of tasks, such as object recognition, text summarization, recommendation systems, and more.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f70e0ef3-5da8-43ee-97c7-307c710790ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWXXK3CV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIAz1TZ0t1nHranaNO2ujy7L3t3KGOePUKlWBbypa2IvEAiA8lzp33u2J4c4pYM9YN5tBL9K2kzqvyV%2F4esPSs02sFCr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMZIMvRrQTO8%2B2%2FB1EKtwDa8YiJEc5FOovWOEbTwZ%2Bg0KutoS14N1z259RPy53zvT49Sb9AEJ%2Bj53OfvfIUjYfYffzYqygVWqf7AA%2BrNu2zshPDILAQY7gZla15OBuhv6mbokvE3Te%2BoDtcysxBeup887ZRS%2BjGWxoqYGczL2d7XB6LjlOzJNd4pfiIARdRHDSRYDd%2BeGerGhfrtZdS0fRg%2B37NupXA4zOs%2BU86Cpb4gIuobaX7rADfqrNhlXEretyVvX1a2lMbFmO9NkrOpSuDQ36%2Bd4ozJwA1T6o6wVFqY%2FtxS%2BVTPba7F4kvcNnqxgh5SoZGq7DPrltmjTHGdou5NxgY2hTTMyjWAEw1TE1oa2uIb70c3XUZQg%2F4LedqObEc4FV8fG%2FeUAvxC15Xh8w0dR7Q43KKK00se2Je740%2F0nqiT0vxmXniiVYQzf3lsTZod2%2FozBl75J3DwBdFCH1dP6hxpdWuKJiIISwFaghZJsI9vaSSL6DjKVGGT4inwfv8T9BAc7ba3jlXLCxOr5NeLq5PnGsialawE6T5rrl6%2Fxm7VXtWVsLJtOeHRRo7g3LtE3cezq0Q3aasd5e4cy%2FXoOLewvUbTTfAUO9LR%2FMQQcz7AOfEX7JkqyVFg2070O%2Bk8f3km%2FG8JPIOQcwna6HvQY6pgH%2BABFL8PT%2BZxzebEy6MRWSkb5gs4mznd5R%2Bh27FLA9gUO7rn8yIiPNcvUtqGbRIMkNp8Zgsl1Ok8mkAqDU%2BOAhjAZWe3JOeM7fGVC7CsIJadThAUp48ztH9bHTsJ8FCnO9%2BZvUGV%2BuswlfTu8mmjAhMLfg7yeNYuUQ%2FNlcFwhgzHH1BzwwQ0q%2FXP27a2gQsD9BiiaTBM2YGu9ao3INvnFJIx2SEuyJ&X-Amz-Signature=e2a7bdc0756cba5272cda7ba4fb7e5087297b9306cf0fdb2f69a43d31d420312&X-Amz-SignedHeaders=host&x-id=GetObject)

### Major Machine Learning Techniques
___
**Regression**
- **Definition**: A method used to predict continuous values (e.g., prices, temperatures) based on input features.
	- **Scenario**: House Price Prediction
	- **Description**: A real estate company wants to predict house prices based on features like size, number of bedrooms, and location. They use a linear regression model.
	- **Data**:
		- Size (square feet)
		- Number of bedrooms
		- Location (neighborhood)
		- Age of the house
		- Historical sale prices
	- **Outcome**: The model predicts the price of a house given its features.
	- **Benefit**: Helps the company set competitive prices and assists buyers in making informed decisions.
___
**Classification**
- **Definition**: A method used to predict categories or labels (e.g., spam or not spam) based on input features.
	- **Scenario**: Email Spam Detection
	- **Description**: An email service provider wants to filter out spam emails. They use a logistic regression or decision tree classifier.
	- **Data**:
		- Email content (text)
		- Metadata (sender address, frequency of keywords)
		- Label (spam or not spam)
	- **Outcome**: The model classifies emails as either spam or not spam.
	- **Benefit**: Reduces the number of spam emails reaching users' inboxes, improving user experience.
___
**Clustering**
- **Definition**: A method used to group similar data points together without predefined categories.
	- **Scenario**: Customer Segmentation
	- **Description**: An e-commerce company segments its customers based on purchasing behavior using the K-means clustering algorithm.
	- **Data**:
		- Customer Age
		- Annual Income
		- Spending Score
	- **Outcome**: Customers are grouped into clusters with similar behaviors.
	- **Benefit**: Allows for targeted marketing strategies.
___
**Association Rule Learning**
- **Definition**: A method used to find relationships between items in large datasets.
	- **Scenario**: Market Basket Analysis
	- **Description**: A grocery store identifies items frequently bought together using the Apriori algorithm.
	- **Data**:
		- Transaction ID
		- List of items purchased
	- **Outcome**: Rules like {Bread, Butter} → {Milk} are discovered.
	- **Benefit**: Optimizes product placement and promotions.
___
**Anomaly Detection**
- **Definition**: A method used to identify unusual patterns that do not conform to expected behavior.
	- **Scenario**: Fraud Detection
	- **Description**: A bank wants to detect fraudulent transactions. They use anomaly detection techniques.
	- **Data**:
		- Transaction amount
		- Transaction location
		- Time of transaction
		- Historical transaction data
	- **Outcome**: The model flags suspicious transactions.
	- **Benefit**: Helps prevent fraud and protects customers.
___
**Sequence Mining**
- **Definition**: A method used to discover patterns in sequential data.
	- **Scenario**: Customer Purchase Patterns
	- **Description**: An online retailer wants to find patterns in the sequence of items customers purchase. They use sequence mining techniques.
	- **Data**:
		- Transaction sequences
		- Items purchased in order
	- **Outcome**: Patterns like customers often buying a phone case after purchasing a phone are discovered.
	- **Benefit**: Helps in creating better marketing strategies.
___
**Dimensionality Reduction**
- **Definition**: A method used to reduce the number of input variables in a dataset.
	- **Scenario**: Data Visualization
	- **Description**: A data scientist wants to visualize high-dimensional data. They use Principal Component Analysis (PCA).
	- **Data**:
		- Multidimensional data points
	- **Outcome**: The data is reduced to two or three principal components for visualization.
	- **Benefit**: Helps in understanding data structure and identifying patterns.
___
**Recommendation Systems**
- **Definition**: A method used to suggest items to users based on various factors.
	- **Scenario**: Movie Recommendations
	- **Description**: A streaming service wants to recommend movies to its users. They use a recommendation system.
	- **Data**:
		- User viewing history
		- Movie ratings
		- Genre preferences
	- **Outcome**: The system suggests movies that users are likely to enjoy.
	- **Benefit**: Enhances user experience and increases engagement.
___
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f3682ae8-1011-4662-9f34-0e5b8ac9951f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWXXK3CV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIAz1TZ0t1nHranaNO2ujy7L3t3KGOePUKlWBbypa2IvEAiA8lzp33u2J4c4pYM9YN5tBL9K2kzqvyV%2F4esPSs02sFCr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMZIMvRrQTO8%2B2%2FB1EKtwDa8YiJEc5FOovWOEbTwZ%2Bg0KutoS14N1z259RPy53zvT49Sb9AEJ%2Bj53OfvfIUjYfYffzYqygVWqf7AA%2BrNu2zshPDILAQY7gZla15OBuhv6mbokvE3Te%2BoDtcysxBeup887ZRS%2BjGWxoqYGczL2d7XB6LjlOzJNd4pfiIARdRHDSRYDd%2BeGerGhfrtZdS0fRg%2B37NupXA4zOs%2BU86Cpb4gIuobaX7rADfqrNhlXEretyVvX1a2lMbFmO9NkrOpSuDQ36%2Bd4ozJwA1T6o6wVFqY%2FtxS%2BVTPba7F4kvcNnqxgh5SoZGq7DPrltmjTHGdou5NxgY2hTTMyjWAEw1TE1oa2uIb70c3XUZQg%2F4LedqObEc4FV8fG%2FeUAvxC15Xh8w0dR7Q43KKK00se2Je740%2F0nqiT0vxmXniiVYQzf3lsTZod2%2FozBl75J3DwBdFCH1dP6hxpdWuKJiIISwFaghZJsI9vaSSL6DjKVGGT4inwfv8T9BAc7ba3jlXLCxOr5NeLq5PnGsialawE6T5rrl6%2Fxm7VXtWVsLJtOeHRRo7g3LtE3cezq0Q3aasd5e4cy%2FXoOLewvUbTTfAUO9LR%2FMQQcz7AOfEX7JkqyVFg2070O%2Bk8f3km%2FG8JPIOQcwna6HvQY6pgH%2BABFL8PT%2BZxzebEy6MRWSkb5gs4mznd5R%2Bh27FLA9gUO7rn8yIiPNcvUtqGbRIMkNp8Zgsl1Ok8mkAqDU%2BOAhjAZWe3JOeM7fGVC7CsIJadThAUp48ztH9bHTsJ8FCnO9%2BZvUGV%2BuswlfTu8mmjAhMLfg7yeNYuUQ%2FNlcFwhgzHH1BzwwQ0q%2FXP27a2gQsD9BiiaTBM2YGu9ao3INvnFJIx2SEuyJ&X-Amz-Signature=ec1726da72dfd03b7eb7ce3df387ee49962db7d760985703a42048ad539aa9e7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Note
Sequence mining identifies patterns based on the order of events, while association rule learning focuses on identifying co-occurrence patterns without considering the order of items.

___
### Understanding Artificial Intelligence, Machine Learning, and Deep Learning
Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) are often used interchangeably but refer to distinct concepts in the realm of computer science:
- **Artificial Intelligence (AI)** encompasses the broad goal of simulating human intelligence in machines. It includes fields like computer vision, natural language processing, creativity, and summarization.
- **Machine Learning (ML)** is a subset of AI that focuses on algorithms and statistical models that enable computers to perform tasks without explicit programming. ML involves learning from data and examples to improve performance on specific tasks.
- **Deep Learning (DL)** represents a specialized area within ML that involves algorithms inspired by the structure and function of the human brain's neural networks. DL enables computers to learn from large amounts of data and make decisions autonomously.
In summary:
- **AI** aims to make machines intelligent across various domains.
- **ML** provides the statistical tools for machines to learn from data and improve over time.
- **DL** utilizes deep neural networks to achieve high levels of automation and performance in tasks like image and speech recognition.

___
### Introduction to Python for Machine Learning
Python is a popular and powerful general-purpose programming language that has emerged as the preferred language among data scientists. Writing machine learning algorithms using Python is highly effective, especially with numerous pre-implemented modules and libraries available.
#### Key Python Packages for Machine Learning
1. **NumPy**: A math library for working with N-dimensional arrays. It enables efficient computation and is superior for tasks involving arrays, dictionaries, functions, datatypes, and image processing.
2. **SciPy**: A collection of numerical algorithms and domain-specific toolboxes, including signal processing, optimization, and statistics. Ideal for scientific and high-performance computation.
3. **Matplotlib**: A popular plotting package providing both 2D and 3D plotting capabilities. Essential for visualizing data in real-world problem-solving.
4. **Pandas**: A high-level library offering high-performance, easy-to-use data structures and functions for data importing, manipulation, and analysis, particularly for numerical tables and time series.
5. **SciKit Learn**: A comprehensive library of machine learning algorithms and tools. It integrates well with NumPy and SciPy and simplifies the implementation of machine learning models.
#### **SciKit Learn** 
SciKit Learn is a comprehensive machine learning library that integrates seamlessly with NumPy and SciPy. It simplifies the implementation of machine learning models through several streamlined steps:
- **Pre-processing**: Standardizing datasets to handle outliers and varying scales, transforming raw feature vectors into suitable forms for modeling.
- **Train-Test Split**: Dividing datasets into training and testing subsets to validate model performance.
- **Building and Training Models**: Initializing and configuring algorithms, such as support vector classification, and fitting them to training data.
- **Making Predictions**: Using the test data to evaluate the model’s performance.
- **Evaluation**: Assessing accuracy with metrics like a confusion matrix, visualizing model performance.
- **Model Exporting**: Saving trained models for future use, enabling easy deployment.
A typical workflow with SciKit Learn involves pre-processing the data, splitting it into training and testing sets, building and training a classifier, making predictions, evaluating the model, and saving it for future use.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b437e049-e272-41b4-bb95-e2807ba514ca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWXXK3CV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIAz1TZ0t1nHranaNO2ujy7L3t3KGOePUKlWBbypa2IvEAiA8lzp33u2J4c4pYM9YN5tBL9K2kzqvyV%2F4esPSs02sFCr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMZIMvRrQTO8%2B2%2FB1EKtwDa8YiJEc5FOovWOEbTwZ%2Bg0KutoS14N1z259RPy53zvT49Sb9AEJ%2Bj53OfvfIUjYfYffzYqygVWqf7AA%2BrNu2zshPDILAQY7gZla15OBuhv6mbokvE3Te%2BoDtcysxBeup887ZRS%2BjGWxoqYGczL2d7XB6LjlOzJNd4pfiIARdRHDSRYDd%2BeGerGhfrtZdS0fRg%2B37NupXA4zOs%2BU86Cpb4gIuobaX7rADfqrNhlXEretyVvX1a2lMbFmO9NkrOpSuDQ36%2Bd4ozJwA1T6o6wVFqY%2FtxS%2BVTPba7F4kvcNnqxgh5SoZGq7DPrltmjTHGdou5NxgY2hTTMyjWAEw1TE1oa2uIb70c3XUZQg%2F4LedqObEc4FV8fG%2FeUAvxC15Xh8w0dR7Q43KKK00se2Je740%2F0nqiT0vxmXniiVYQzf3lsTZod2%2FozBl75J3DwBdFCH1dP6hxpdWuKJiIISwFaghZJsI9vaSSL6DjKVGGT4inwfv8T9BAc7ba3jlXLCxOr5NeLq5PnGsialawE6T5rrl6%2Fxm7VXtWVsLJtOeHRRo7g3LtE3cezq0Q3aasd5e4cy%2FXoOLewvUbTTfAUO9LR%2FMQQcz7AOfEX7JkqyVFg2070O%2Bk8f3km%2FG8JPIOQcwna6HvQY6pgH%2BABFL8PT%2BZxzebEy6MRWSkb5gs4mznd5R%2Bh27FLA9gUO7rn8yIiPNcvUtqGbRIMkNp8Zgsl1Ok8mkAqDU%2BOAhjAZWe3JOeM7fGVC7CsIJadThAUp48ztH9bHTsJ8FCnO9%2BZvUGV%2BuswlfTu8mmjAhMLfg7yeNYuUQ%2FNlcFwhgzHH1BzwwQ0q%2FXP27a2gQsD9BiiaTBM2YGu9ao3INvnFJIx2SEuyJ&X-Amz-Signature=1a7d82872e4236550049d6eef761203a0b7a84bbcb64e3d8b5949c0c6217f8fb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cea31c5d-b49d-4d39-8566-ec7e66e033b4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWXXK3CV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIAz1TZ0t1nHranaNO2ujy7L3t3KGOePUKlWBbypa2IvEAiA8lzp33u2J4c4pYM9YN5tBL9K2kzqvyV%2F4esPSs02sFCr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMZIMvRrQTO8%2B2%2FB1EKtwDa8YiJEc5FOovWOEbTwZ%2Bg0KutoS14N1z259RPy53zvT49Sb9AEJ%2Bj53OfvfIUjYfYffzYqygVWqf7AA%2BrNu2zshPDILAQY7gZla15OBuhv6mbokvE3Te%2BoDtcysxBeup887ZRS%2BjGWxoqYGczL2d7XB6LjlOzJNd4pfiIARdRHDSRYDd%2BeGerGhfrtZdS0fRg%2B37NupXA4zOs%2BU86Cpb4gIuobaX7rADfqrNhlXEretyVvX1a2lMbFmO9NkrOpSuDQ36%2Bd4ozJwA1T6o6wVFqY%2FtxS%2BVTPba7F4kvcNnqxgh5SoZGq7DPrltmjTHGdou5NxgY2hTTMyjWAEw1TE1oa2uIb70c3XUZQg%2F4LedqObEc4FV8fG%2FeUAvxC15Xh8w0dR7Q43KKK00se2Je740%2F0nqiT0vxmXniiVYQzf3lsTZod2%2FozBl75J3DwBdFCH1dP6hxpdWuKJiIISwFaghZJsI9vaSSL6DjKVGGT4inwfv8T9BAc7ba3jlXLCxOr5NeLq5PnGsialawE6T5rrl6%2Fxm7VXtWVsLJtOeHRRo7g3LtE3cezq0Q3aasd5e4cy%2FXoOLewvUbTTfAUO9LR%2FMQQcz7AOfEX7JkqyVFg2070O%2Bk8f3km%2FG8JPIOQcwna6HvQY6pgH%2BABFL8PT%2BZxzebEy6MRWSkb5gs4mznd5R%2Bh27FLA9gUO7rn8yIiPNcvUtqGbRIMkNp8Zgsl1Ok8mkAqDU%2BOAhjAZWe3JOeM7fGVC7CsIJadThAUp48ztH9bHTsJ8FCnO9%2BZvUGV%2BuswlfTu8mmjAhMLfg7yeNYuUQ%2FNlcFwhgzHH1BzwwQ0q%2FXP27a2gQsD9BiiaTBM2YGu9ao3INvnFJIx2SEuyJ&X-Amz-Signature=a3f57f3d3618e44bdaf3a8208ad9cc47dff4bfc263b02e9cb9e003e1fe3a3005&X-Amz-SignedHeaders=host&x-id=GetObject)
___
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a7c7fcb1-e868-4073-9392-bd1424f11933/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWXXK3CV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIAz1TZ0t1nHranaNO2ujy7L3t3KGOePUKlWBbypa2IvEAiA8lzp33u2J4c4pYM9YN5tBL9K2kzqvyV%2F4esPSs02sFCr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMZIMvRrQTO8%2B2%2FB1EKtwDa8YiJEc5FOovWOEbTwZ%2Bg0KutoS14N1z259RPy53zvT49Sb9AEJ%2Bj53OfvfIUjYfYffzYqygVWqf7AA%2BrNu2zshPDILAQY7gZla15OBuhv6mbokvE3Te%2BoDtcysxBeup887ZRS%2BjGWxoqYGczL2d7XB6LjlOzJNd4pfiIARdRHDSRYDd%2BeGerGhfrtZdS0fRg%2B37NupXA4zOs%2BU86Cpb4gIuobaX7rADfqrNhlXEretyVvX1a2lMbFmO9NkrOpSuDQ36%2Bd4ozJwA1T6o6wVFqY%2FtxS%2BVTPba7F4kvcNnqxgh5SoZGq7DPrltmjTHGdou5NxgY2hTTMyjWAEw1TE1oa2uIb70c3XUZQg%2F4LedqObEc4FV8fG%2FeUAvxC15Xh8w0dR7Q43KKK00se2Je740%2F0nqiT0vxmXniiVYQzf3lsTZod2%2FozBl75J3DwBdFCH1dP6hxpdWuKJiIISwFaghZJsI9vaSSL6DjKVGGT4inwfv8T9BAc7ba3jlXLCxOr5NeLq5PnGsialawE6T5rrl6%2Fxm7VXtWVsLJtOeHRRo7g3LtE3cezq0Q3aasd5e4cy%2FXoOLewvUbTTfAUO9LR%2FMQQcz7AOfEX7JkqyVFg2070O%2Bk8f3km%2FG8JPIOQcwna6HvQY6pgH%2BABFL8PT%2BZxzebEy6MRWSkb5gs4mznd5R%2Bh27FLA9gUO7rn8yIiPNcvUtqGbRIMkNp8Zgsl1Ok8mkAqDU%2BOAhjAZWe3JOeM7fGVC7CsIJadThAUp48ztH9bHTsJ8FCnO9%2BZvUGV%2BuswlfTu8mmjAhMLfg7yeNYuUQ%2FNlcFwhgzHH1BzwwQ0q%2FXP27a2gQsD9BiiaTBM2YGu9ao3INvnFJIx2SEuyJ&X-Amz-Signature=718bcac7d9892ae208c7fa899d93002e09ff5685e5db22dbd52a27707c40708e&X-Amz-SignedHeaders=host&x-id=GetObject)

Understanding and leveraging these packages, especially SciKit Learn, simplifies the machine learning process and reduces the amount of coding required compared to using pure Python or other individual packages.

___
### **Supervised vs Unsupervised Algorithms**
Understanding the difference between supervised and unsupervised learning is fundamental in machine learning.
#### **Supervised Learning**
Supervised learning involves teaching a machine learning model using a labeled dataset. This means the model is trained on data where the input features and the output labels are known. For example, in a cancer dataset, features like clump thickness and cell size (attributes) are used to predict if a cell is malignant or benign (label). The goal is to predict future instances based on this training.
- **Types of Supervised Learning**:
	- **Classification**: Predicts discrete class labels. For example, classifying emails as spam or not spam.
	- **Regression**: Predicts continuous values. For example, predicting the CO2 emission of a car based on its engine size and number of cylinders.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d97478ab-3688-44b7-9ac9-b31943e9e39a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWXXK3CV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIAz1TZ0t1nHranaNO2ujy7L3t3KGOePUKlWBbypa2IvEAiA8lzp33u2J4c4pYM9YN5tBL9K2kzqvyV%2F4esPSs02sFCr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMZIMvRrQTO8%2B2%2FB1EKtwDa8YiJEc5FOovWOEbTwZ%2Bg0KutoS14N1z259RPy53zvT49Sb9AEJ%2Bj53OfvfIUjYfYffzYqygVWqf7AA%2BrNu2zshPDILAQY7gZla15OBuhv6mbokvE3Te%2BoDtcysxBeup887ZRS%2BjGWxoqYGczL2d7XB6LjlOzJNd4pfiIARdRHDSRYDd%2BeGerGhfrtZdS0fRg%2B37NupXA4zOs%2BU86Cpb4gIuobaX7rADfqrNhlXEretyVvX1a2lMbFmO9NkrOpSuDQ36%2Bd4ozJwA1T6o6wVFqY%2FtxS%2BVTPba7F4kvcNnqxgh5SoZGq7DPrltmjTHGdou5NxgY2hTTMyjWAEw1TE1oa2uIb70c3XUZQg%2F4LedqObEc4FV8fG%2FeUAvxC15Xh8w0dR7Q43KKK00se2Je740%2F0nqiT0vxmXniiVYQzf3lsTZod2%2FozBl75J3DwBdFCH1dP6hxpdWuKJiIISwFaghZJsI9vaSSL6DjKVGGT4inwfv8T9BAc7ba3jlXLCxOr5NeLq5PnGsialawE6T5rrl6%2Fxm7VXtWVsLJtOeHRRo7g3LtE3cezq0Q3aasd5e4cy%2FXoOLewvUbTTfAUO9LR%2FMQQcz7AOfEX7JkqyVFg2070O%2Bk8f3km%2FG8JPIOQcwna6HvQY6pgH%2BABFL8PT%2BZxzebEy6MRWSkb5gs4mznd5R%2Bh27FLA9gUO7rn8yIiPNcvUtqGbRIMkNp8Zgsl1Ok8mkAqDU%2BOAhjAZWe3JOeM7fGVC7CsIJadThAUp48ztH9bHTsJ8FCnO9%2BZvUGV%2BuswlfTu8mmjAhMLfg7yeNYuUQ%2FNlcFwhgzHH1BzwwQ0q%2FXP27a2gQsD9BiiaTBM2YGu9ao3INvnFJIx2SEuyJ&X-Amz-Signature=6b6cbcc7de0ea76e4d84c8e39c66ecbaa0a5abd9617bd42d8e7e223f40d7358f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Unsupervised Learning**
Unsupervised learning involves training a model on data without labeled responses. The model tries to learn the underlying structure of the data on its own.
- **Common Unsupervised Learning Techniques**:
	- **Clustering**: Grouping data points into clusters based on their similarity. It is widely used for customer segmentation, organizing music genres, etc.
	- **Dimensionality Reduction**: Reducing the number of features in the data to simplify the model and make the classification easier.
	- **Market Basket Analysis**: Identifying items that frequently co-occur in transactions.
	- **Density Estimation**: Exploring the data to find some underlying structure.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efcaecea-9440-472e-8abf-cb0ac379999a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWXXK3CV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIAz1TZ0t1nHranaNO2ujy7L3t3KGOePUKlWBbypa2IvEAiA8lzp33u2J4c4pYM9YN5tBL9K2kzqvyV%2F4esPSs02sFCr%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMZIMvRrQTO8%2B2%2FB1EKtwDa8YiJEc5FOovWOEbTwZ%2Bg0KutoS14N1z259RPy53zvT49Sb9AEJ%2Bj53OfvfIUjYfYffzYqygVWqf7AA%2BrNu2zshPDILAQY7gZla15OBuhv6mbokvE3Te%2BoDtcysxBeup887ZRS%2BjGWxoqYGczL2d7XB6LjlOzJNd4pfiIARdRHDSRYDd%2BeGerGhfrtZdS0fRg%2B37NupXA4zOs%2BU86Cpb4gIuobaX7rADfqrNhlXEretyVvX1a2lMbFmO9NkrOpSuDQ36%2Bd4ozJwA1T6o6wVFqY%2FtxS%2BVTPba7F4kvcNnqxgh5SoZGq7DPrltmjTHGdou5NxgY2hTTMyjWAEw1TE1oa2uIb70c3XUZQg%2F4LedqObEc4FV8fG%2FeUAvxC15Xh8w0dR7Q43KKK00se2Je740%2F0nqiT0vxmXniiVYQzf3lsTZod2%2FozBl75J3DwBdFCH1dP6hxpdWuKJiIISwFaghZJsI9vaSSL6DjKVGGT4inwfv8T9BAc7ba3jlXLCxOr5NeLq5PnGsialawE6T5rrl6%2Fxm7VXtWVsLJtOeHRRo7g3LtE3cezq0Q3aasd5e4cy%2FXoOLewvUbTTfAUO9LR%2FMQQcz7AOfEX7JkqyVFg2070O%2Bk8f3km%2FG8JPIOQcwna6HvQY6pgH%2BABFL8PT%2BZxzebEy6MRWSkb5gs4mznd5R%2Bh27FLA9gUO7rn8yIiPNcvUtqGbRIMkNp8Zgsl1Ok8mkAqDU%2BOAhjAZWe3JOeM7fGVC7CsIJadThAUp48ztH9bHTsJ8FCnO9%2BZvUGV%2BuswlfTu8mmjAhMLfg7yeNYuUQ%2FNlcFwhgzHH1BzwwQ0q%2FXP27a2gQsD9BiiaTBM2YGu9ao3INvnFJIx2SEuyJ&X-Amz-Signature=2e11334b39ca2e79166a4e34205ae3c084cb59dc170b37cc4a1c378e3829d0b2&X-Amz-SignedHeaders=host&x-id=GetObject)

#### **Key Differences Between Supervised and Unsupervised**
- **Data**:
	- Supervised Learning: Uses labeled data.
	- Unsupervised Learning: Uses unlabeled data.
- **Techniques**:
	- Supervised Learning: Includes classification and regression.
	- Unsupervised Learning: Includes clustering, dimensionality reduction, market basket analysis, and density estimation.
- **Outcome Control**:
	- Supervised Learning: More controllable environment due to labeled data.
	- Unsupervised Learning: Less controllable, model draws conclusions from the data without predefined labels.
**Recap**
The main distinction between supervised and unsupervised learning is that supervised learning uses labeled data to train models, while unsupervised learning uses unlabeled data, allowing the model to find hidden patterns or intrinsic structures. Supervised learning methods are more straightforward in terms of evaluation and control compared to the often complex algorithms and less predictable outcomes in unsupervised learning.
