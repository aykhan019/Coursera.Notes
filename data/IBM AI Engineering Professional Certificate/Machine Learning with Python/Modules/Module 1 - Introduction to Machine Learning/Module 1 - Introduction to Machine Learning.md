

# Module 1: Introduction to Machine Learning
### What is Machine Learning?
Machine Learning is a subfield of computer science that gives computers the ability to learn from data without being explicitly programmed. It involves the development of algorithms that can recognize patterns, make decisions, and improve themselves over time.
### How Does Machine Learning Work?
Machine Learning algorithms, inspired by the human learning process, iteratively learn from data. These algorithms allow computers to discover hidden insights and patterns within large datasets. The models created through Machine Learning can assist in a variety of tasks, such as object recognition, text summarization, recommendation systems, and more.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f70e0ef3-5da8-43ee-97c7-307c710790ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIAYKCSK%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC8S4pkQgA8ZLqnwgTqnTAAgoOGktMAeQ%2FTxgZiHc1sNgIhAP4bFowYeKXnGlnMnbsqoDA0KmVzHUroRZTrl7E4sb96KogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrcTu1TOLD5HPed%2FUq3AMsZUJ42CRkxi0VKVAQNdxHEODQoRXE9BjxTWO3K%2ByevA3se%2BcY1dQsJ5OsGzqDZLU%2B2Xxxj8VJzlKjPNCq5VpnlJsXtv55igQ1b2zstUE1vjVnNo8%2FFUCCoix7zlFaYpB%2BP62Y2%2FNNhxTbC%2BX9KzDirUC%2F3aTVKYZEvVkYBols6m6cmO5lKEPVaII1cLwkt6oVA2AccasbjUrOptLBJkugGXJniuZDyAyRIZirZnTJJyfY73oJD%2Bl8CpCSEJy3E0Oo7cswGdpB5LefClZDJNenxj0rPQVEt5%2FnJuoPlap7FB781C%2BKn1Q8OCWvMhYg%2B40mb%2F6%2B2v6YjWRe4cMf676RbDdTBOK6XGeniZTyZ67IyEmbtPNGoYSaItJKFC1VacmnOX5JJM%2Bb%2BmOgosNS%2FmRlZJwR%2FD8I6eN4etS8qQrMF2V0ulvoylubAhkpZf8mhpmUfzi50AoCx2xjtw3ajG8n8ZAS8bo1Zz9a1UDWPO5N33TyYgdVa6rN22yeCb6oVwvdjioaf4LOqARhHGZcUhgvmdpGvzuJgoNx%2BgvjhhmiSAsDbQrPmbmIzyhdK4whQroEbNGy38dfWUDnMFjX3dLD23H5HoBGZZCjzwrjtrb7Z5xXwUqEHUtPH9psWzDPo6K%2FBjqkAXlLo8L%2FZviF%2F9dlmO06ItjVPOqSqVbgGqhsaDCSdAqF5VAw4P1ifnvERWTL5dqSeMW5GjhCLlQz4TiABTy3higluJN0v08g3KQMJvGr%2F%2Fmd6iwYiBrQaFQrWWcdGiVEOrAlJfVUSEbW2O0rzPlbTEYLPMQbA0E71%2FIgrlO%2FTOlvcaoOujPs67%2FIzmOW1LVgGcJhqx%2Fd9pwKXtm6T1xK8MCrBcw6&X-Amz-Signature=338979a8d6c2ecf9f5c7711f201345ac09e331ca435222128a983c3441fbac3f&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f3682ae8-1011-4662-9f34-0e5b8ac9951f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIAYKCSK%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC8S4pkQgA8ZLqnwgTqnTAAgoOGktMAeQ%2FTxgZiHc1sNgIhAP4bFowYeKXnGlnMnbsqoDA0KmVzHUroRZTrl7E4sb96KogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrcTu1TOLD5HPed%2FUq3AMsZUJ42CRkxi0VKVAQNdxHEODQoRXE9BjxTWO3K%2ByevA3se%2BcY1dQsJ5OsGzqDZLU%2B2Xxxj8VJzlKjPNCq5VpnlJsXtv55igQ1b2zstUE1vjVnNo8%2FFUCCoix7zlFaYpB%2BP62Y2%2FNNhxTbC%2BX9KzDirUC%2F3aTVKYZEvVkYBols6m6cmO5lKEPVaII1cLwkt6oVA2AccasbjUrOptLBJkugGXJniuZDyAyRIZirZnTJJyfY73oJD%2Bl8CpCSEJy3E0Oo7cswGdpB5LefClZDJNenxj0rPQVEt5%2FnJuoPlap7FB781C%2BKn1Q8OCWvMhYg%2B40mb%2F6%2B2v6YjWRe4cMf676RbDdTBOK6XGeniZTyZ67IyEmbtPNGoYSaItJKFC1VacmnOX5JJM%2Bb%2BmOgosNS%2FmRlZJwR%2FD8I6eN4etS8qQrMF2V0ulvoylubAhkpZf8mhpmUfzi50AoCx2xjtw3ajG8n8ZAS8bo1Zz9a1UDWPO5N33TyYgdVa6rN22yeCb6oVwvdjioaf4LOqARhHGZcUhgvmdpGvzuJgoNx%2BgvjhhmiSAsDbQrPmbmIzyhdK4whQroEbNGy38dfWUDnMFjX3dLD23H5HoBGZZCjzwrjtrb7Z5xXwUqEHUtPH9psWzDPo6K%2FBjqkAXlLo8L%2FZviF%2F9dlmO06ItjVPOqSqVbgGqhsaDCSdAqF5VAw4P1ifnvERWTL5dqSeMW5GjhCLlQz4TiABTy3higluJN0v08g3KQMJvGr%2F%2Fmd6iwYiBrQaFQrWWcdGiVEOrAlJfVUSEbW2O0rzPlbTEYLPMQbA0E71%2FIgrlO%2FTOlvcaoOujPs67%2FIzmOW1LVgGcJhqx%2Fd9pwKXtm6T1xK8MCrBcw6&X-Amz-Signature=0fa01d2ab8f37418e4651bacc77ec42f5fd88365a86938b5adfc171d15865cc2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/b437e049-e272-41b4-bb95-e2807ba514ca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIAYKCSK%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC8S4pkQgA8ZLqnwgTqnTAAgoOGktMAeQ%2FTxgZiHc1sNgIhAP4bFowYeKXnGlnMnbsqoDA0KmVzHUroRZTrl7E4sb96KogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrcTu1TOLD5HPed%2FUq3AMsZUJ42CRkxi0VKVAQNdxHEODQoRXE9BjxTWO3K%2ByevA3se%2BcY1dQsJ5OsGzqDZLU%2B2Xxxj8VJzlKjPNCq5VpnlJsXtv55igQ1b2zstUE1vjVnNo8%2FFUCCoix7zlFaYpB%2BP62Y2%2FNNhxTbC%2BX9KzDirUC%2F3aTVKYZEvVkYBols6m6cmO5lKEPVaII1cLwkt6oVA2AccasbjUrOptLBJkugGXJniuZDyAyRIZirZnTJJyfY73oJD%2Bl8CpCSEJy3E0Oo7cswGdpB5LefClZDJNenxj0rPQVEt5%2FnJuoPlap7FB781C%2BKn1Q8OCWvMhYg%2B40mb%2F6%2B2v6YjWRe4cMf676RbDdTBOK6XGeniZTyZ67IyEmbtPNGoYSaItJKFC1VacmnOX5JJM%2Bb%2BmOgosNS%2FmRlZJwR%2FD8I6eN4etS8qQrMF2V0ulvoylubAhkpZf8mhpmUfzi50AoCx2xjtw3ajG8n8ZAS8bo1Zz9a1UDWPO5N33TyYgdVa6rN22yeCb6oVwvdjioaf4LOqARhHGZcUhgvmdpGvzuJgoNx%2BgvjhhmiSAsDbQrPmbmIzyhdK4whQroEbNGy38dfWUDnMFjX3dLD23H5HoBGZZCjzwrjtrb7Z5xXwUqEHUtPH9psWzDPo6K%2FBjqkAXlLo8L%2FZviF%2F9dlmO06ItjVPOqSqVbgGqhsaDCSdAqF5VAw4P1ifnvERWTL5dqSeMW5GjhCLlQz4TiABTy3higluJN0v08g3KQMJvGr%2F%2Fmd6iwYiBrQaFQrWWcdGiVEOrAlJfVUSEbW2O0rzPlbTEYLPMQbA0E71%2FIgrlO%2FTOlvcaoOujPs67%2FIzmOW1LVgGcJhqx%2Fd9pwKXtm6T1xK8MCrBcw6&X-Amz-Signature=951067091654df765755bf6dfbd38500dd8ec78a410bdf4da8eb6f302a398b3f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cea31c5d-b49d-4d39-8566-ec7e66e033b4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIAYKCSK%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC8S4pkQgA8ZLqnwgTqnTAAgoOGktMAeQ%2FTxgZiHc1sNgIhAP4bFowYeKXnGlnMnbsqoDA0KmVzHUroRZTrl7E4sb96KogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrcTu1TOLD5HPed%2FUq3AMsZUJ42CRkxi0VKVAQNdxHEODQoRXE9BjxTWO3K%2ByevA3se%2BcY1dQsJ5OsGzqDZLU%2B2Xxxj8VJzlKjPNCq5VpnlJsXtv55igQ1b2zstUE1vjVnNo8%2FFUCCoix7zlFaYpB%2BP62Y2%2FNNhxTbC%2BX9KzDirUC%2F3aTVKYZEvVkYBols6m6cmO5lKEPVaII1cLwkt6oVA2AccasbjUrOptLBJkugGXJniuZDyAyRIZirZnTJJyfY73oJD%2Bl8CpCSEJy3E0Oo7cswGdpB5LefClZDJNenxj0rPQVEt5%2FnJuoPlap7FB781C%2BKn1Q8OCWvMhYg%2B40mb%2F6%2B2v6YjWRe4cMf676RbDdTBOK6XGeniZTyZ67IyEmbtPNGoYSaItJKFC1VacmnOX5JJM%2Bb%2BmOgosNS%2FmRlZJwR%2FD8I6eN4etS8qQrMF2V0ulvoylubAhkpZf8mhpmUfzi50AoCx2xjtw3ajG8n8ZAS8bo1Zz9a1UDWPO5N33TyYgdVa6rN22yeCb6oVwvdjioaf4LOqARhHGZcUhgvmdpGvzuJgoNx%2BgvjhhmiSAsDbQrPmbmIzyhdK4whQroEbNGy38dfWUDnMFjX3dLD23H5HoBGZZCjzwrjtrb7Z5xXwUqEHUtPH9psWzDPo6K%2FBjqkAXlLo8L%2FZviF%2F9dlmO06ItjVPOqSqVbgGqhsaDCSdAqF5VAw4P1ifnvERWTL5dqSeMW5GjhCLlQz4TiABTy3higluJN0v08g3KQMJvGr%2F%2Fmd6iwYiBrQaFQrWWcdGiVEOrAlJfVUSEbW2O0rzPlbTEYLPMQbA0E71%2FIgrlO%2FTOlvcaoOujPs67%2FIzmOW1LVgGcJhqx%2Fd9pwKXtm6T1xK8MCrBcw6&X-Amz-Signature=8a85174a78727d92808cddac60ccaf03a0e1af482624b6e3491630c86d29a96a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a7c7fcb1-e868-4073-9392-bd1424f11933/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIAYKCSK%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC8S4pkQgA8ZLqnwgTqnTAAgoOGktMAeQ%2FTxgZiHc1sNgIhAP4bFowYeKXnGlnMnbsqoDA0KmVzHUroRZTrl7E4sb96KogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrcTu1TOLD5HPed%2FUq3AMsZUJ42CRkxi0VKVAQNdxHEODQoRXE9BjxTWO3K%2ByevA3se%2BcY1dQsJ5OsGzqDZLU%2B2Xxxj8VJzlKjPNCq5VpnlJsXtv55igQ1b2zstUE1vjVnNo8%2FFUCCoix7zlFaYpB%2BP62Y2%2FNNhxTbC%2BX9KzDirUC%2F3aTVKYZEvVkYBols6m6cmO5lKEPVaII1cLwkt6oVA2AccasbjUrOptLBJkugGXJniuZDyAyRIZirZnTJJyfY73oJD%2Bl8CpCSEJy3E0Oo7cswGdpB5LefClZDJNenxj0rPQVEt5%2FnJuoPlap7FB781C%2BKn1Q8OCWvMhYg%2B40mb%2F6%2B2v6YjWRe4cMf676RbDdTBOK6XGeniZTyZ67IyEmbtPNGoYSaItJKFC1VacmnOX5JJM%2Bb%2BmOgosNS%2FmRlZJwR%2FD8I6eN4etS8qQrMF2V0ulvoylubAhkpZf8mhpmUfzi50AoCx2xjtw3ajG8n8ZAS8bo1Zz9a1UDWPO5N33TyYgdVa6rN22yeCb6oVwvdjioaf4LOqARhHGZcUhgvmdpGvzuJgoNx%2BgvjhhmiSAsDbQrPmbmIzyhdK4whQroEbNGy38dfWUDnMFjX3dLD23H5HoBGZZCjzwrjtrb7Z5xXwUqEHUtPH9psWzDPo6K%2FBjqkAXlLo8L%2FZviF%2F9dlmO06ItjVPOqSqVbgGqhsaDCSdAqF5VAw4P1ifnvERWTL5dqSeMW5GjhCLlQz4TiABTy3higluJN0v08g3KQMJvGr%2F%2Fmd6iwYiBrQaFQrWWcdGiVEOrAlJfVUSEbW2O0rzPlbTEYLPMQbA0E71%2FIgrlO%2FTOlvcaoOujPs67%2FIzmOW1LVgGcJhqx%2Fd9pwKXtm6T1xK8MCrBcw6&X-Amz-Signature=2d2ecf443970908966d143d24318f8279c561aad1dd0fff08dd7b1a57425e480&X-Amz-SignedHeaders=host&x-id=GetObject)

Understanding and leveraging these packages, especially SciKit Learn, simplifies the machine learning process and reduces the amount of coding required compared to using pure Python or other individual packages.

___
### **Supervised vs Unsupervised Algorithms**
Understanding the difference between supervised and unsupervised learning is fundamental in machine learning.
#### **Supervised Learning**
Supervised learning involves teaching a machine learning model using a labeled dataset. This means the model is trained on data where the input features and the output labels are known. For example, in a cancer dataset, features like clump thickness and cell size (attributes) are used to predict if a cell is malignant or benign (label). The goal is to predict future instances based on this training.
- **Types of Supervised Learning**:
	- **Classification**: Predicts discrete class labels. For example, classifying emails as spam or not spam.
	- **Regression**: Predicts continuous values. For example, predicting the CO2 emission of a car based on its engine size and number of cylinders.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d97478ab-3688-44b7-9ac9-b31943e9e39a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIAYKCSK%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC8S4pkQgA8ZLqnwgTqnTAAgoOGktMAeQ%2FTxgZiHc1sNgIhAP4bFowYeKXnGlnMnbsqoDA0KmVzHUroRZTrl7E4sb96KogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrcTu1TOLD5HPed%2FUq3AMsZUJ42CRkxi0VKVAQNdxHEODQoRXE9BjxTWO3K%2ByevA3se%2BcY1dQsJ5OsGzqDZLU%2B2Xxxj8VJzlKjPNCq5VpnlJsXtv55igQ1b2zstUE1vjVnNo8%2FFUCCoix7zlFaYpB%2BP62Y2%2FNNhxTbC%2BX9KzDirUC%2F3aTVKYZEvVkYBols6m6cmO5lKEPVaII1cLwkt6oVA2AccasbjUrOptLBJkugGXJniuZDyAyRIZirZnTJJyfY73oJD%2Bl8CpCSEJy3E0Oo7cswGdpB5LefClZDJNenxj0rPQVEt5%2FnJuoPlap7FB781C%2BKn1Q8OCWvMhYg%2B40mb%2F6%2B2v6YjWRe4cMf676RbDdTBOK6XGeniZTyZ67IyEmbtPNGoYSaItJKFC1VacmnOX5JJM%2Bb%2BmOgosNS%2FmRlZJwR%2FD8I6eN4etS8qQrMF2V0ulvoylubAhkpZf8mhpmUfzi50AoCx2xjtw3ajG8n8ZAS8bo1Zz9a1UDWPO5N33TyYgdVa6rN22yeCb6oVwvdjioaf4LOqARhHGZcUhgvmdpGvzuJgoNx%2BgvjhhmiSAsDbQrPmbmIzyhdK4whQroEbNGy38dfWUDnMFjX3dLD23H5HoBGZZCjzwrjtrb7Z5xXwUqEHUtPH9psWzDPo6K%2FBjqkAXlLo8L%2FZviF%2F9dlmO06ItjVPOqSqVbgGqhsaDCSdAqF5VAw4P1ifnvERWTL5dqSeMW5GjhCLlQz4TiABTy3higluJN0v08g3KQMJvGr%2F%2Fmd6iwYiBrQaFQrWWcdGiVEOrAlJfVUSEbW2O0rzPlbTEYLPMQbA0E71%2FIgrlO%2FTOlvcaoOujPs67%2FIzmOW1LVgGcJhqx%2Fd9pwKXtm6T1xK8MCrBcw6&X-Amz-Signature=3fdb7bf33775eba9684e7fe9c1c49dd25a1b1a11c1c608ff1df40c2f89608307&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Unsupervised Learning**
Unsupervised learning involves training a model on data without labeled responses. The model tries to learn the underlying structure of the data on its own.
- **Common Unsupervised Learning Techniques**:
	- **Clustering**: Grouping data points into clusters based on their similarity. It is widely used for customer segmentation, organizing music genres, etc.
	- **Dimensionality Reduction**: Reducing the number of features in the data to simplify the model and make the classification easier.
	- **Market Basket Analysis**: Identifying items that frequently co-occur in transactions.
	- **Density Estimation**: Exploring the data to find some underlying structure.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efcaecea-9440-472e-8abf-cb0ac379999a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIAYKCSK%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQC8S4pkQgA8ZLqnwgTqnTAAgoOGktMAeQ%2FTxgZiHc1sNgIhAP4bFowYeKXnGlnMnbsqoDA0KmVzHUroRZTrl7E4sb96KogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwrcTu1TOLD5HPed%2FUq3AMsZUJ42CRkxi0VKVAQNdxHEODQoRXE9BjxTWO3K%2ByevA3se%2BcY1dQsJ5OsGzqDZLU%2B2Xxxj8VJzlKjPNCq5VpnlJsXtv55igQ1b2zstUE1vjVnNo8%2FFUCCoix7zlFaYpB%2BP62Y2%2FNNhxTbC%2BX9KzDirUC%2F3aTVKYZEvVkYBols6m6cmO5lKEPVaII1cLwkt6oVA2AccasbjUrOptLBJkugGXJniuZDyAyRIZirZnTJJyfY73oJD%2Bl8CpCSEJy3E0Oo7cswGdpB5LefClZDJNenxj0rPQVEt5%2FnJuoPlap7FB781C%2BKn1Q8OCWvMhYg%2B40mb%2F6%2B2v6YjWRe4cMf676RbDdTBOK6XGeniZTyZ67IyEmbtPNGoYSaItJKFC1VacmnOX5JJM%2Bb%2BmOgosNS%2FmRlZJwR%2FD8I6eN4etS8qQrMF2V0ulvoylubAhkpZf8mhpmUfzi50AoCx2xjtw3ajG8n8ZAS8bo1Zz9a1UDWPO5N33TyYgdVa6rN22yeCb6oVwvdjioaf4LOqARhHGZcUhgvmdpGvzuJgoNx%2BgvjhhmiSAsDbQrPmbmIzyhdK4whQroEbNGy38dfWUDnMFjX3dLD23H5HoBGZZCjzwrjtrb7Z5xXwUqEHUtPH9psWzDPo6K%2FBjqkAXlLo8L%2FZviF%2F9dlmO06ItjVPOqSqVbgGqhsaDCSdAqF5VAw4P1ifnvERWTL5dqSeMW5GjhCLlQz4TiABTy3higluJN0v08g3KQMJvGr%2F%2Fmd6iwYiBrQaFQrWWcdGiVEOrAlJfVUSEbW2O0rzPlbTEYLPMQbA0E71%2FIgrlO%2FTOlvcaoOujPs67%2FIzmOW1LVgGcJhqx%2Fd9pwKXtm6T1xK8MCrBcw6&X-Amz-Signature=9e5f11a92bbdf73ebb9ff397e917507b71c3f59de88235922349b0618392415f&X-Amz-SignedHeaders=host&x-id=GetObject)

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
