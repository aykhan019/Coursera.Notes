

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXTRUYJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBqoeSvP%2Ft9fyxx65s3bT7wq9qb2AC4Jr%2B1AmLhkKRqdAiBD7BNZwRWxn4G1N%2B%2BSR7nt0A1FS6WsFH0KuLVYa5ZFzir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMIgoFsurNQCaCh7S9KtwDzWvWkWV7oZGtHclR4L%2BGaD7beFnVUqyDXwbMR3KMDP%2F52UFtACgyoODElf%2Fh6jQ5LbhZot7sWG7V3qIv4qzXKFqyanv84wM4kzCuqGZd9Hl9pZDHvPCEJmFMflZ9SyHROr%2BcZLdw7IAfp1u%2F8sxxkYDSXoJ7As5IrWTuc3BnKoBO40msd%2FUeYeachcMJCv9%2F4HNI%2BotQKQee46bYA0B%2Bv6ABzdAlOCAXh9xeoOc%2B%2Fdb2juDbzdjVKBeprRAwpzkWLiU%2Bq8qsPEFhYRDyfL10hzn2kTeMJ9sCpYzZNtW0RBa0QJo7F1UdIUQIdmoZ6UMKCXZhAQxibJd9tNv2PWk108gzYXwBMTCgh1vvTggAJXJ0wNb22r3MJjwMQCK19EPvKcKf3OUim1JzLHfZWXr2frNT0BYO8V5ss6ZFEPKVt%2FR98dSd1VLU9zBmj3BH7LMyQkzndVC6tnphvHsAJ4hTdKHRfRpEUwVScUwTOkAVFSmL3%2BKzR0lwHJn9PvMHroKWE%2F4%2BNyLqN0IZrs%2Fiqgk%2BRIaHHQNURfB3pWlvVfRudjL9GCEM%2BU4NOdtWV8WMf6aPfF1MzVNTBSikBHAvKRBE7ymJP83FMlAuMFoNEzrAaEIZkp2fX4OpbLGUlc8w9JKHvQY6pgFfX1jo14FPn33wM%2FL1DPyDUne1xYCqVtBQ7vwjko7VnqkrOm2uH%2F%2F4hKBDbRuSKX3KONqoemDZXpbjReCXh6ghJTq1isH5LBuBx2d71WS2vj3Dd9n28q%2FU7hFNcCSdUNEEnlgnNskACLz%2BpMGuJXWmIZupeoprzH4O51va3U1la9v4v3SgNVQnS3uPATI9UmPcZVHCV7POy96%2BFGnEHhaatPXiaaaJ&X-Amz-Signature=f7e7d185fc86afee4110f04582ce4ec858b9bc8148d17152656bdeada3f4060e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example Dataset
Consider a dataset related to CO2 emissions from different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emission
#### Predictive Question
Given this dataset, is it possible to predict the CO2 emission of a car using other fields such as engine size or cylinders? → Yes
### Historical Data and Prediction
Assume there is historical data from different cars. The goal is to estimate the CO2 emission of a new or unknown car, such as the one in row 9, which hasn't been manufactured yet. Regression methods can be used to make this prediction.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXTRUYJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBqoeSvP%2Ft9fyxx65s3bT7wq9qb2AC4Jr%2B1AmLhkKRqdAiBD7BNZwRWxn4G1N%2B%2BSR7nt0A1FS6WsFH0KuLVYa5ZFzir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMIgoFsurNQCaCh7S9KtwDzWvWkWV7oZGtHclR4L%2BGaD7beFnVUqyDXwbMR3KMDP%2F52UFtACgyoODElf%2Fh6jQ5LbhZot7sWG7V3qIv4qzXKFqyanv84wM4kzCuqGZd9Hl9pZDHvPCEJmFMflZ9SyHROr%2BcZLdw7IAfp1u%2F8sxxkYDSXoJ7As5IrWTuc3BnKoBO40msd%2FUeYeachcMJCv9%2F4HNI%2BotQKQee46bYA0B%2Bv6ABzdAlOCAXh9xeoOc%2B%2Fdb2juDbzdjVKBeprRAwpzkWLiU%2Bq8qsPEFhYRDyfL10hzn2kTeMJ9sCpYzZNtW0RBa0QJo7F1UdIUQIdmoZ6UMKCXZhAQxibJd9tNv2PWk108gzYXwBMTCgh1vvTggAJXJ0wNb22r3MJjwMQCK19EPvKcKf3OUim1JzLHfZWXr2frNT0BYO8V5ss6ZFEPKVt%2FR98dSd1VLU9zBmj3BH7LMyQkzndVC6tnphvHsAJ4hTdKHRfRpEUwVScUwTOkAVFSmL3%2BKzR0lwHJn9PvMHroKWE%2F4%2BNyLqN0IZrs%2Fiqgk%2BRIaHHQNURfB3pWlvVfRudjL9GCEM%2BU4NOdtWV8WMf6aPfF1MzVNTBSikBHAvKRBE7ymJP83FMlAuMFoNEzrAaEIZkp2fX4OpbLGUlc8w9JKHvQY6pgFfX1jo14FPn33wM%2FL1DPyDUne1xYCqVtBQ7vwjko7VnqkrOm2uH%2F%2F4hKBDbRuSKX3KONqoemDZXpbjReCXh6ghJTq1isH5LBuBx2d71WS2vj3Dd9n28q%2FU7hFNcCSdUNEEnlgnNskACLz%2BpMGuJXWmIZupeoprzH4O51va3U1la9v4v3SgNVQnS3uPATI9UmPcZVHCV7POy96%2BFGnEHhaatPXiaaaJ&X-Amz-Signature=1e1c6e52360d42e901f4c86fb154959792929d85e979f7756e904d513384628d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Types of Variables in Regression
- **Dependent Variable (Y):** The state, target, or final goal to be predicted.
- **Independent Variables (X):** The causes or explanatory variables.
### Types of Regression Models
#### Simple Regression
- **Definition:** Uses one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using the variable of engine size.
- **Nature:** Can be linear or non-linear based on the relationship between the independent and dependent variables.
#### Multiple Regression
- **Definition:** Uses more than one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using engine size and the number of cylinders.
- **Nature:** Can be linear or non-linear depending on the relationship between the dependent and independent variables.
### Applications of Regression
#### Sales Forecasting
Predicting a salesperson's total yearly sales using independent variables such as age, education, and years of experience.
#### Psychology
Determining individual satisfaction based on demographic and psychological factors.
#### Real Estate
Predicting the price of a house based on its size, number of bedrooms, and other features.
#### Employment Income
Predicting employment income using variables such as hours of work, education, occupation, age, and years of experience.
#### Other Fields
Regression analysis is also useful in finance, healthcare, retail, and more.
### Conclusion
Regression analysis has numerous applications across various fields. It helps in estimating continuous values using historical data and independent variables. Various regression algorithms exist, each suited to specific conditions, providing a foundation for exploring different regression techniques.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXTRUYJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBqoeSvP%2Ft9fyxx65s3bT7wq9qb2AC4Jr%2B1AmLhkKRqdAiBD7BNZwRWxn4G1N%2B%2BSR7nt0A1FS6WsFH0KuLVYa5ZFzir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMIgoFsurNQCaCh7S9KtwDzWvWkWV7oZGtHclR4L%2BGaD7beFnVUqyDXwbMR3KMDP%2F52UFtACgyoODElf%2Fh6jQ5LbhZot7sWG7V3qIv4qzXKFqyanv84wM4kzCuqGZd9Hl9pZDHvPCEJmFMflZ9SyHROr%2BcZLdw7IAfp1u%2F8sxxkYDSXoJ7As5IrWTuc3BnKoBO40msd%2FUeYeachcMJCv9%2F4HNI%2BotQKQee46bYA0B%2Bv6ABzdAlOCAXh9xeoOc%2B%2Fdb2juDbzdjVKBeprRAwpzkWLiU%2Bq8qsPEFhYRDyfL10hzn2kTeMJ9sCpYzZNtW0RBa0QJo7F1UdIUQIdmoZ6UMKCXZhAQxibJd9tNv2PWk108gzYXwBMTCgh1vvTggAJXJ0wNb22r3MJjwMQCK19EPvKcKf3OUim1JzLHfZWXr2frNT0BYO8V5ss6ZFEPKVt%2FR98dSd1VLU9zBmj3BH7LMyQkzndVC6tnphvHsAJ4hTdKHRfRpEUwVScUwTOkAVFSmL3%2BKzR0lwHJn9PvMHroKWE%2F4%2BNyLqN0IZrs%2Fiqgk%2BRIaHHQNURfB3pWlvVfRudjL9GCEM%2BU4NOdtWV8WMf6aPfF1MzVNTBSikBHAvKRBE7ymJP83FMlAuMFoNEzrAaEIZkp2fX4OpbLGUlc8w9JKHvQY6pgFfX1jo14FPn33wM%2FL1DPyDUne1xYCqVtBQ7vwjko7VnqkrOm2uH%2F%2F4hKBDbRuSKX3KONqoemDZXpbjReCXh6ghJTq1isH5LBuBx2d71WS2vj3Dd9n28q%2FU7hFNcCSdUNEEnlgnNskACLz%2BpMGuJXWmIZupeoprzH4O51va3U1la9v4v3SgNVQnS3uPATI9UmPcZVHCV7POy96%2BFGnEHhaatPXiaaaJ&X-Amz-Signature=6d97ae1f531954dc6aaf5c4906f04d9ee1bfcabb7a6622ad96460c5d84f4ccbf&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## Introduction to Linear Regression
Linear regression is an effective method for predicting a continuous value using other variables. This introduction provides the necessary background to use linear regression effectively.
### Dataset Overview
Consider a dataset related to CO2 emissions of different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emissions
The goal is to predict the CO2 emission of a car using another field, such as engine size. Linear regression can be used for this purpose.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXTRUYJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBqoeSvP%2Ft9fyxx65s3bT7wq9qb2AC4Jr%2B1AmLhkKRqdAiBD7BNZwRWxn4G1N%2B%2BSR7nt0A1FS6WsFH0KuLVYa5ZFzir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMIgoFsurNQCaCh7S9KtwDzWvWkWV7oZGtHclR4L%2BGaD7beFnVUqyDXwbMR3KMDP%2F52UFtACgyoODElf%2Fh6jQ5LbhZot7sWG7V3qIv4qzXKFqyanv84wM4kzCuqGZd9Hl9pZDHvPCEJmFMflZ9SyHROr%2BcZLdw7IAfp1u%2F8sxxkYDSXoJ7As5IrWTuc3BnKoBO40msd%2FUeYeachcMJCv9%2F4HNI%2BotQKQee46bYA0B%2Bv6ABzdAlOCAXh9xeoOc%2B%2Fdb2juDbzdjVKBeprRAwpzkWLiU%2Bq8qsPEFhYRDyfL10hzn2kTeMJ9sCpYzZNtW0RBa0QJo7F1UdIUQIdmoZ6UMKCXZhAQxibJd9tNv2PWk108gzYXwBMTCgh1vvTggAJXJ0wNb22r3MJjwMQCK19EPvKcKf3OUim1JzLHfZWXr2frNT0BYO8V5ss6ZFEPKVt%2FR98dSd1VLU9zBmj3BH7LMyQkzndVC6tnphvHsAJ4hTdKHRfRpEUwVScUwTOkAVFSmL3%2BKzR0lwHJn9PvMHroKWE%2F4%2BNyLqN0IZrs%2Fiqgk%2BRIaHHQNURfB3pWlvVfRudjL9GCEM%2BU4NOdtWV8WMf6aPfF1MzVNTBSikBHAvKRBE7ymJP83FMlAuMFoNEzrAaEIZkp2fX4OpbLGUlc8w9JKHvQY6pgFfX1jo14FPn33wM%2FL1DPyDUne1xYCqVtBQ7vwjko7VnqkrOm2uH%2F%2F4hKBDbRuSKX3KONqoemDZXpbjReCXh6ghJTq1isH5LBuBx2d71WS2vj3Dd9n28q%2FU7hFNcCSdUNEEnlgnNskACLz%2BpMGuJXWmIZupeoprzH4O51va3U1la9v4v3SgNVQnS3uPATI9UmPcZVHCV7POy96%2BFGnEHhaatPXiaaaJ&X-Amz-Signature=07505339a3cadf2f87f1bba3ca45b1369666596ca8ebd4110fa4bb17f553163c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Linear Regression Basics
Linear regression is the approximation of a linear model to describe the relationship between two or more variables.
#### Variables in Linear Regression
- **Dependent Variable (Y):** The continuous value being predicted.
- **Independent Variable (X):** The explanatory variable(s), which can be categorical or continuous.
#### Types of Linear Regression
1. **Simple Linear Regression:**
	- Uses one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size.
2. **Multiple Linear Regression:**
	- Uses more than one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size and number of cylinders.
### How Linear Regression Works
#### Scatter Plot
A scatter plot can be used to visualize the relationship between variables, such as engine size (independent variable) and CO2 emission (dependent variable). The plot helps to identify if the variables are linearly related.
#### Fitting a Line
Linear regression fits a line through the data points. For example, as the engine size increases, the CO2 emissions also increase. The objective is to find a line that best fits the data, which can be used to predict CO2 emissions.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXTRUYJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBqoeSvP%2Ft9fyxx65s3bT7wq9qb2AC4Jr%2B1AmLhkKRqdAiBD7BNZwRWxn4G1N%2B%2BSR7nt0A1FS6WsFH0KuLVYa5ZFzir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMIgoFsurNQCaCh7S9KtwDzWvWkWV7oZGtHclR4L%2BGaD7beFnVUqyDXwbMR3KMDP%2F52UFtACgyoODElf%2Fh6jQ5LbhZot7sWG7V3qIv4qzXKFqyanv84wM4kzCuqGZd9Hl9pZDHvPCEJmFMflZ9SyHROr%2BcZLdw7IAfp1u%2F8sxxkYDSXoJ7As5IrWTuc3BnKoBO40msd%2FUeYeachcMJCv9%2F4HNI%2BotQKQee46bYA0B%2Bv6ABzdAlOCAXh9xeoOc%2B%2Fdb2juDbzdjVKBeprRAwpzkWLiU%2Bq8qsPEFhYRDyfL10hzn2kTeMJ9sCpYzZNtW0RBa0QJo7F1UdIUQIdmoZ6UMKCXZhAQxibJd9tNv2PWk108gzYXwBMTCgh1vvTggAJXJ0wNb22r3MJjwMQCK19EPvKcKf3OUim1JzLHfZWXr2frNT0BYO8V5ss6ZFEPKVt%2FR98dSd1VLU9zBmj3BH7LMyQkzndVC6tnphvHsAJ4hTdKHRfRpEUwVScUwTOkAVFSmL3%2BKzR0lwHJn9PvMHroKWE%2F4%2BNyLqN0IZrs%2Fiqgk%2BRIaHHQNURfB3pWlvVfRudjL9GCEM%2BU4NOdtWV8WMf6aPfF1MzVNTBSikBHAvKRBE7ymJP83FMlAuMFoNEzrAaEIZkp2fX4OpbLGUlc8w9JKHvQY6pgFfX1jo14FPn33wM%2FL1DPyDUne1xYCqVtBQ7vwjko7VnqkrOm2uH%2F%2F4hKBDbRuSKX3KONqoemDZXpbjReCXh6ghJTq1isH5LBuBx2d71WS2vj3Dd9n28q%2FU7hFNcCSdUNEEnlgnNskACLz%2BpMGuJXWmIZupeoprzH4O51va3U1la9v4v3SgNVQnS3uPATI9UmPcZVHCV7POy96%2BFGnEHhaatPXiaaaJ&X-Amz-Signature=fafcd100dbabd6a931f0584ae22477dc743f71e105db1d13f90a134280e3effc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXTRUYJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBqoeSvP%2Ft9fyxx65s3bT7wq9qb2AC4Jr%2B1AmLhkKRqdAiBD7BNZwRWxn4G1N%2B%2BSR7nt0A1FS6WsFH0KuLVYa5ZFzir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMIgoFsurNQCaCh7S9KtwDzWvWkWV7oZGtHclR4L%2BGaD7beFnVUqyDXwbMR3KMDP%2F52UFtACgyoODElf%2Fh6jQ5LbhZot7sWG7V3qIv4qzXKFqyanv84wM4kzCuqGZd9Hl9pZDHvPCEJmFMflZ9SyHROr%2BcZLdw7IAfp1u%2F8sxxkYDSXoJ7As5IrWTuc3BnKoBO40msd%2FUeYeachcMJCv9%2F4HNI%2BotQKQee46bYA0B%2Bv6ABzdAlOCAXh9xeoOc%2B%2Fdb2juDbzdjVKBeprRAwpzkWLiU%2Bq8qsPEFhYRDyfL10hzn2kTeMJ9sCpYzZNtW0RBa0QJo7F1UdIUQIdmoZ6UMKCXZhAQxibJd9tNv2PWk108gzYXwBMTCgh1vvTggAJXJ0wNb22r3MJjwMQCK19EPvKcKf3OUim1JzLHfZWXr2frNT0BYO8V5ss6ZFEPKVt%2FR98dSd1VLU9zBmj3BH7LMyQkzndVC6tnphvHsAJ4hTdKHRfRpEUwVScUwTOkAVFSmL3%2BKzR0lwHJn9PvMHroKWE%2F4%2BNyLqN0IZrs%2Fiqgk%2BRIaHHQNURfB3pWlvVfRudjL9GCEM%2BU4NOdtWV8WMf6aPfF1MzVNTBSikBHAvKRBE7ymJP83FMlAuMFoNEzrAaEIZkp2fX4OpbLGUlc8w9JKHvQY6pgFfX1jo14FPn33wM%2FL1DPyDUne1xYCqVtBQ7vwjko7VnqkrOm2uH%2F%2F4hKBDbRuSKX3KONqoemDZXpbjReCXh6ghJTq1isH5LBuBx2d71WS2vj3Dd9n28q%2FU7hFNcCSdUNEEnlgnNskACLz%2BpMGuJXWmIZupeoprzH4O51va3U1la9v4v3SgNVQnS3uPATI9UmPcZVHCV7POy96%2BFGnEHhaatPXiaaaJ&X-Amz-Signature=1f745c1a9a9ae28c8444fc28cd2e7de689e713fa543708edc9b89dcd14573212&X-Amz-SignedHeaders=host&x-id=GetObject)
### Mathematical Representation
The fitted line in linear regression is represented as a polynomial. For a simple linear regression with one independent variable , the model is:
$ \hat{y} = \theta_0 + \theta_1 x_1 $
- $ \hat{y} $: Predicted value (dependent variable)
- $ x_1 $: Independent variable
- $ \theta_0 $: Intercept
- $ \theta_1 $: Slope or gradient of the line
#### Estimating Coefficients
- $ \theta_0 $ (intercept) and $ θ_1 $ (slope) are the parameters of the line that need to be adjusted to minimize the error.
- The goal is to minimize the mean squared error (MSE), which is the mean of all residual errors (the distance from data points to the fitted line).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXTRUYJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBqoeSvP%2Ft9fyxx65s3bT7wq9qb2AC4Jr%2B1AmLhkKRqdAiBD7BNZwRWxn4G1N%2B%2BSR7nt0A1FS6WsFH0KuLVYa5ZFzir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMIgoFsurNQCaCh7S9KtwDzWvWkWV7oZGtHclR4L%2BGaD7beFnVUqyDXwbMR3KMDP%2F52UFtACgyoODElf%2Fh6jQ5LbhZot7sWG7V3qIv4qzXKFqyanv84wM4kzCuqGZd9Hl9pZDHvPCEJmFMflZ9SyHROr%2BcZLdw7IAfp1u%2F8sxxkYDSXoJ7As5IrWTuc3BnKoBO40msd%2FUeYeachcMJCv9%2F4HNI%2BotQKQee46bYA0B%2Bv6ABzdAlOCAXh9xeoOc%2B%2Fdb2juDbzdjVKBeprRAwpzkWLiU%2Bq8qsPEFhYRDyfL10hzn2kTeMJ9sCpYzZNtW0RBa0QJo7F1UdIUQIdmoZ6UMKCXZhAQxibJd9tNv2PWk108gzYXwBMTCgh1vvTggAJXJ0wNb22r3MJjwMQCK19EPvKcKf3OUim1JzLHfZWXr2frNT0BYO8V5ss6ZFEPKVt%2FR98dSd1VLU9zBmj3BH7LMyQkzndVC6tnphvHsAJ4hTdKHRfRpEUwVScUwTOkAVFSmL3%2BKzR0lwHJn9PvMHroKWE%2F4%2BNyLqN0IZrs%2Fiqgk%2BRIaHHQNURfB3pWlvVfRudjL9GCEM%2BU4NOdtWV8WMf6aPfF1MzVNTBSikBHAvKRBE7ymJP83FMlAuMFoNEzrAaEIZkp2fX4OpbLGUlc8w9JKHvQY6pgFfX1jo14FPn33wM%2FL1DPyDUne1xYCqVtBQ7vwjko7VnqkrOm2uH%2F%2F4hKBDbRuSKX3KONqoemDZXpbjReCXh6ghJTq1isH5LBuBx2d71WS2vj3Dd9n28q%2FU7hFNcCSdUNEEnlgnNskACLz%2BpMGuJXWmIZupeoprzH4O51va3U1la9v4v3SgNVQnS3uPATI9UmPcZVHCV7POy96%2BFGnEHhaatPXiaaaJ&X-Amz-Signature=94e125cd75cf6d4b9a9a2a8b906783c3ce6eb80d201f4e4391b60264d4232c89&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXTRUYJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBqoeSvP%2Ft9fyxx65s3bT7wq9qb2AC4Jr%2B1AmLhkKRqdAiBD7BNZwRWxn4G1N%2B%2BSR7nt0A1FS6WsFH0KuLVYa5ZFzir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMIgoFsurNQCaCh7S9KtwDzWvWkWV7oZGtHclR4L%2BGaD7beFnVUqyDXwbMR3KMDP%2F52UFtACgyoODElf%2Fh6jQ5LbhZot7sWG7V3qIv4qzXKFqyanv84wM4kzCuqGZd9Hl9pZDHvPCEJmFMflZ9SyHROr%2BcZLdw7IAfp1u%2F8sxxkYDSXoJ7As5IrWTuc3BnKoBO40msd%2FUeYeachcMJCv9%2F4HNI%2BotQKQee46bYA0B%2Bv6ABzdAlOCAXh9xeoOc%2B%2Fdb2juDbzdjVKBeprRAwpzkWLiU%2Bq8qsPEFhYRDyfL10hzn2kTeMJ9sCpYzZNtW0RBa0QJo7F1UdIUQIdmoZ6UMKCXZhAQxibJd9tNv2PWk108gzYXwBMTCgh1vvTggAJXJ0wNb22r3MJjwMQCK19EPvKcKf3OUim1JzLHfZWXr2frNT0BYO8V5ss6ZFEPKVt%2FR98dSd1VLU9zBmj3BH7LMyQkzndVC6tnphvHsAJ4hTdKHRfRpEUwVScUwTOkAVFSmL3%2BKzR0lwHJn9PvMHroKWE%2F4%2BNyLqN0IZrs%2Fiqgk%2BRIaHHQNURfB3pWlvVfRudjL9GCEM%2BU4NOdtWV8WMf6aPfF1MzVNTBSikBHAvKRBE7ymJP83FMlAuMFoNEzrAaEIZkp2fX4OpbLGUlc8w9JKHvQY6pgFfX1jo14FPn33wM%2FL1DPyDUne1xYCqVtBQ7vwjko7VnqkrOm2uH%2F%2F4hKBDbRuSKX3KONqoemDZXpbjReCXh6ghJTq1isH5LBuBx2d71WS2vj3Dd9n28q%2FU7hFNcCSdUNEEnlgnNskACLz%2BpMGuJXWmIZupeoprzH4O51va3U1la9v4v3SgNVQnS3uPATI9UmPcZVHCV7POy96%2BFGnEHhaatPXiaaaJ&X-Amz-Signature=79a66d34eb1fc3e53c663bde956b1669f48857b7aa31024c73c566ea2533fb9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example Calculation
For a dataset with known values:
- If $ θ_1 $= 43.98 and $  θ_0 $ = 92.94, the linear model is:
$$ CO2Emission=92.94+43.98×EngineSize $$
#### Prediction Example
For a car with an engine size of 2.4:
$$ CO2Emission=92.94+43.98×2.4=198.492 $$
### Why Linear Regression is Useful
- **Simplicity:** Easy to use and understand.
- **Speed:** Fast and efficient.
- **No Parameter Tuning:** Does not require parameter tuning like other algorithms (e.g., k-nearest neighbors, neural networks).
- **Interpretability:** Highly interpretable and provides clear insights into relationships between variables.
___

## Model Evaluation in Regression
Model evaluation in regression aims to assess how well a model can predict unknown data. Two main evaluation approaches are commonly used: train and test on the same dataset, and train/test split. Additionally, K-fold cross-validation is introduced as a more advanced method to address some limitations of the other two approaches.
### Evaluation Approaches
6. **Train and Test on the Same Dataset:**
	- **Process:**
		- Use the entire dataset to train the model.
		- Select a portion of the dataset as the test set (without labels during prediction).
		- Predict target values using the model.
		- Compare predicted values with actual values to calculate accuracy.
	- **Metrics:**
		- Compare actual values y with predicted values $ \hat{y} $.
		- Calculate the error as the average difference between predicted and actual values.
	- **Advantages:**
		- Simple and straightforward.
	- **Disadvantages:**
		- High training accuracy but low out-of-sample accuracy due to overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOQRNNRG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCID4DEVBmRYw%2BM98mXEerzWECxW8jR3JZssGP1itJFAOWAiAdwUahaD%2BMtj22ObeZrOt1QhGYiYg9xSWKo3jwUS%2BROCr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMboPuRvYIFcDlK%2BmzKtwDvE82Rs%2F0kw0wlySfMLunPQiNjqHNNkCLekThlj6%2B0Zd0wMgT6zl1%2BZFcxi14wiCcl4YCjV%2BsRa5b8OD9ZjrO6OI180RC2KR5WfbBDUaAy9aj293M0X%2B3c34qDwWqmLHokmU%2F3bfIqwjYvbRpYENkIWKpimdS3M9cYsDtm4R58C4Kq8zSWWq0A7M%2BHwHlKxFx%2BelXVQhP3Gu%2BwmSG%2FlK1Pkh7RIvG6gKHrMYCZi0FCL3IC2taQGnICwZ9lLe3P6%2BlS5x86lafQjfb7eEFqiS%2BM83Pnao6M3KkZMwkaNL5bo6QhRDM1SMLZHbW7n0jZK9iM8h%2Bm3Od1reON8rrqwPOl4tiAvde9cpHpJ2KOPAS180hvf1TnIDGatJqR1tuqraqqSw%2FMU4CRBcqyq9W5DLDvcVrMh5cdJdVEiCJircbeVT7wSd0%2FYSg4A1gXCq3A9AsWh2UfHfSS%2FbA4KyRjEd8ylVmuwx7n29QN2YCGHF5OcAikj5Q4tBY4JYy%2FOWKlqiR2SrKNhOh2JYPNy%2BYcrezI2CTq5LPvqnJEuj8pIOfxbNbQ26kESGbkyTlqEh5yAq4Lk8hnbsVWGEuDeCiiJcht5KpwCGW%2BTg0tzQi3dNe%2BEjHUj3Njk25cJc%2FYbwwnZGHvQY6pgGbEnqhIoe1wfL1yzH2OVWwnVwfD%2BqDVkQtXlHRk1yF6mEb4xrFXPpjtzxO0UmVrYZh2JAZ0Y2zJb%2F2zTPoyN7Nhg%2BeskqkpE%2FL8yLPKlUt3bE0ci0nIePzPUFjb58Ue0FQj8xCI3JquItoxl%2Fk7qDdVNGp8LWSyIrgXGQLOaqQMj%2FqfHVZFwKdkO1f8oPoCEXWdQgmVRSFRQ9BVtTRCC4Ew8WFGRQD&X-Amz-Signature=3cb5dfef5e7e4760c72386e7c108d5ecf192617798fb82355327f3b15892d181&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Predict on the same dataset
predictions = model.predict(X)

# Calculate training accuracy (MSE)
mse = mean_squared_error(y, predictions)
print(f'Mean Squared Error: {mse}')
```
7. **Train/Test Split:**
	- **Process:**
		- Split the dataset into training and testing sets (mutually exclusive).
		- Train the model on the training set.
		- Test the model on the test set by predicting target values.
		- Compare predicted values with actual values to calculate accuracy.
	- **Advantages:**
		- Provides a better evaluation of out-of-sample accuracy.
		- More realistic for real-world problems.
	- **Disadvantages:**
		- Dependent on the specific split of the dataset, which can introduce variation.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662772HU5F%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIHesL%2BNt60Zrl9M0IAz5U90csvFr92oUSqqL%2BvAaICDpAiEAp3JHAhuAWZHN%2BecTWAJjyAkEFBMq2ZxC1O2kGfTQINgq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDGX69l3RPkeo7r2PrSrcA1Hn5%2F7oaIerMGpEgpH%2FAQobrJeNKT02BPoBCeX%2FR8iy%2BNhLKLNlSht3QA2z9fQ54oPjMQjq1VwGTc%2Fpx4%2BIz8ut0kcKktRZL21xuf%2FLmAqEpp8D%2FBCmekVJHOGMeYpDhJhxJPTFLWJUZYqloIT8JWLODKvFEAbgjCLLQou0xxBULRjjNaOhW%2BSg4FuDD68rIdItZNZ6dUMFemcKxTQVnEtGW0zA35V1GuLIXvdtgbDdqSn3PZfUih%2BKDO%2F5G4vCUjYhEsLvKFDI7VFQOzSWMZfrjpzrj8vBD2x5xFo2Qyx9vyOpYAWo926gfS29fI0Sb6XXc7MrD8YIbzpXyTYDarSy%2FXlboBSM9L5hex0sc2ZBegXQKS3Nzu2s1WHm4Rvuoe%2FqBPxSHTrBBUiYUzdVQ11bEL21mOR618dLGgEpAePAXDw%2Fcg%2BoqItF2U1fYObu8No6p4WR6cjErtQJxHL5zVDpDEZ6utwuUNUj%2BMZ2VSJ8L1%2B35bE%2BMnFJp9b9Ds55eC5yrrTD1x3WGATwEmLCqQQIJ5y5Ikbk%2BPXxfzg7TIk4jdEf6JaakAVF%2BaSHmlIC6CbgD16AMokvRRDTwd0uDCy2IXe3hsVqzUdooeNdGuewcCB3tREHGUY9t%2F1cMNiTh70GOqUBmATr82QH67rgLjAY2NlP1cJT%2F0LT4plwwNwcQPgYZP%2BgwMBR%2F14hszprjZ48saeaA64LiIqUyy7EF1zjche7Rr2GuRYC0IbpL%2BlseSL0XzS%2F1UCkCGfz4uWT%2FNVBrI6PVPv6%2Fe3B3OlrCcpU1SbKg4UCNRuAPxkXx%2FmuH5dDIdF1K7IQPZ%2BCGj6dqHedJu7wJ2Qq4P5xc9%2FrqIqx3SY3NqBWgnkk&X-Amz-Signature=f720c2034764bfe0b531b3b76849655575b4991b500849e8ef9c5b6b34bda785&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import train_test_split

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model on the test set
predictions = model.predict(X_test)

# Calculate out-of-sample accuracy (MSE)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error on Test Set: {mse}')
```
### Key Concepts
- **Training Accuracy:** The percentage of correct predictions the model makes on the training dataset. High training accuracy may indicate overfitting.
- **Out-of-Sample Accuracy:** The percentage of correct predictions the model makes on data it has not been trained on. High out-of-sample accuracy indicates better generalization to new data.
### K-Fold Cross-Validation
K-fold cross-validation is a method to address the dependency and variation issues in the train/test split approach. It provides a more consistent measure of out-of-sample accuracy by performing multiple train/test splits.
- **Process:**
	- Divide the dataset into  equal folds.
	- For each fold:
		- Use one fold as the test set and the remaining $ K−1 $ folds as the training set.
		- Train the model on the training set and evaluate it on the test set.
	- Repeat the process for each fold.
	- Average the accuracy results from all folds to obtain a final evaluation metric.
**Example with **$ K=4 $
- Split the dataset into 4 equal parts.
- In each iteration, use a different part as the test set and the rest as the training set.
- Compute accuracy for each fold and average the results.
**Advantages of K-Fold Cross-Validation:**
- Reduces the dependency on a specific train/test split.
- Provides a more reliable estimate of out-of-sample accuracy.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMJTMKPV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDxIjfbY5sbVFPpyl6j5I9aWH8C6TpXboMaV3iM4T1UqQIhAOj%2BQZMcKaZMqVBS6TL5cR0dvTsdRskhGCqRz6fCXGHMKv8DCCkQABoMNjM3NDIzMTgzODA1IgwqkboHZUNkJwDmCJoq3APvFWGe8yKh58oBCOMBVJ0L9vh9o9E9tjdiuFD6H6EcZQ4lg06c9I%2FX0Wr%2FS8nXTj1Q%2B7pLEm6m7fuLqByNr7tU51nGtkT3yksAK1aWzFTQSY9eHeo0xhtLdQqOgZThy8BY4pH0EFu4xc7O7HC3t5zrrz49Dnz4Z9MVxNc7S6pOhLVWRjU%2BEgg2k6ObV9qwJn2Jen16gDxgp4AfH9S6LS7XsD7UHa4RbhT3G%2B9NJbSix4eGqZU4n%2BmGo6xjKGImbUI87bgWVzmsYZoLy5KI68dKk9peybgzPeXqdZdZ97xvbE9AzVMQSTeYH5%2FPyjvSWBRJ4Br7Fc29rCOL0Xb%2BGsUKls9GsTt7l95m4QfXpq%2B2Un2POg9oySVgocGzZg4Zn7eoSAB%2BNRnkPVFtEqy%2FoN7zFgu7BIM0tMmYea6RzE3lINzK6RIkXHMtXRdzp5%2FPc9eGkcti%2F0cjfKKo%2BeZppzVYrDAQn6brMIedQYZeR20ACWTK0aJTp0X31ZpeMFPbBLBp4GXcAtmi7wKJmXyLRXcgEbMFnJ2PIyOnb55T0Y3X7CstSCwrjOxtcXBn%2B0FomWZOjZQZYDbt04Z9b7sKrowoGvtGRW75QuDbM1ExlCP7xy7f2X%2FLqOdWCocF4DCZkYe9BjqkAZMgTgNW%2BNxDPijq%2BvtdGUKfus%2B27byQXmZeZ%2BUcbbhuI2Brfuv5g9zdIr8Hv%2Fmyx9EmNKA%2F9LVQ5kKd37rlCFBxJJ1iYV7AZozotVdc1TOnsSIKkWedTUjzRfVP%2BC3LmxoCWh%2Fz%2Fdewha5t9LOaINytEmNddVranpeBV3MktXq%2F08NlOvearxVID0qPuIdLlaz459kwGW345J9lzF64liFKkpnT&X-Amz-Signature=d8d95123ab4b4c5190597a6759469720ecfe0507f5d3ae8abe8a5a5cf1ed3879&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import cross_val_score

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Perform K-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=4, scoring='neg_mean_squared_error')
mse_scores = -scores
print(f'Mean Squared Error for each fold: {mse_scores}')
print(f'Average Mean Squared Error: {mse_scores.mean()}')
```
### **Formula for Mean Squared Error (MSE):**
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
 $$
Where $ y_i  $ are the actual values, $ \hat{y}_i  $ are the predicted values, and $ n  $ is the number of observations.
### Summary
- **Train and Test on the Same Dataset:** Simple but prone to overfitting with high training accuracy and low out-of-sample accuracy.
- **Train/Test Split:** Provides better out-of-sample accuracy but can still be affected by dataset dependency.
- **K-Fold Cross-Validation:** Mitigates issues of train/test split by averaging results over multiple splits, offering a more consistent evaluation metric.
___
## Model Evaluation Metrics for Regression
### Introduction
Evaluation metrics are essential for assessing the performance of a regression model. These metrics compare actual values to predicted values, providing insights into areas needing improvement. Several key metrics are used to evaluate regression models, including Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Relative Absolute Error (RAE), Relative Squared Error (RSE), and R-squared ($ R^2 $).
### Error Definition
In regression, the error is the difference between the actual data points and the predicted values from the model. This difference can be measured in various ways.
### Mean Absolute Error (MAE)
Mean Absolute Error is the average of the absolute differences between actual and predicted values. It is easy to understand and represents the average error in the same units as the data.
$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
 $$
#### Code Example
```python
from sklearn.metrics import mean_absolute_error

# Example data
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate MAE
mae = mean_absolute_error(y_true, y_pred)
print(f"Mean Absolute Error: {mae}")
```
### Mean Squared Error (MSE)
Mean Squared Error is the average of the squared differences between actual and predicted values. It emphasizes larger errors more than smaller ones due to the squaring term, making it more sensitive to outliers.
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \frac{RSS}{n} $$
#### Code Example
```python
from sklearn.metrics import mean_squared_error

# Calculate MSE
mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error: {mse}")
```
### Root Mean Squared Error (RMSE)
Root Mean Squared Error is the square root of the mean squared error. It is popular because it is in the same units as the response variable, making it easier to interpret.
$$ \text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
 $$
#### Code Example
```python
import numpy as np

# Calculate RMSE
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")
```
### Relative Absolute Error (RAE)
Relative Absolute Error (RAE) is a metric expressed as a ratio normalizing the absolute error. It measures the average absolute difference between the actual and predicted values relative to the average absolute difference between the actual values and their mean.
$$ \text{RAE} = \frac{\sum_{i=1}^{n} |y_i - \hat{y}_i|}{\sum_{i=1}^{n} |y_i - \bar{y}|}
 $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RAE
rae = np.sum(np.abs(y_true - y_pred)) / np.sum(np.abs(y_true - np.mean(y_true)))
print(f"Relative Absolute Error: {rae}")
```
### Relative Squared Error (RSE)
Relative Squared Error is similar to RAE but uses squared differences. It is widely adopted for calculating $ R^2 $.
$$ \text{RSE} = \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RSE
rse = np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2)
print(f"Relative Squared Error: {rse}")
```
### R-squared ($ R^2 $)
R-squared is not an error metric per se (by itself), but it is a popular measure of model accuracy. It indicates how close the data points are to the fitted regression line. A higher $ R^2 $ value indicates a better fit.
$$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} = 1 - RSE $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
from sklearn.metrics import r2_score

# Calculate R-squared
r2 = r2_score(y_true, y_pred)
print(f"R-squared: {r2}")
```
### Residual Sum of Squares (RSS)
The Residual Sum of Squares (RSS) is a measure of the discrepancy between the data and an estimation model. It is calculated as the sum of the squared differences between the observed actual outcomes and the outcomes predicted by the model.
$$ \text{RSS} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = MSE * n $$
#### Code Example
```python
# Calculate RSS
rss = np.sum((y_true - y_pred) ** 2)
print(f"Residual Sum of Squares: {rss}")
```
### Summary
Each of these metrics quantifies different aspects of model performance. The choice of metric depends on the specific model, data type, and domain knowledge. Understanding and selecting the appropriate metric is crucial for evaluating and improving regression models.
___
## Multiple Linear Regression
### **Linear Regression Models**
- **Simple Linear Regression**: Utilizes one independent variable to estimate a dependent variable (e.g., predicting CO₂ emissions based on engine size).
- **Multiple Linear Regression**: Involves multiple independent variables to predict a dependent variable (e.g., predicting CO₂ emissions using engine size and the number of cylinders).
### **Applications of Multiple Linear Regression**
8. **Identifying Effect Strength**: Determines how independent variables affect the dependent variable. For instance, assessing how revision time, test anxiety, lecture attendance, and gender influence student exam performance.
9. **Predicting Impact of Changes**: Evaluates how changes in independent variables affect the dependent variable. For example, predicting how a patient's blood pressure changes with variations in body mass index, keeping other factors constant.
### **Model Representation**
- **Equation**: The model can be expressed as $ \hat{y}=θ_0+θ_1x_1+θ_2x_2+…+θ_nx_n $.
- **Vector Form**: In multidimensional space, the model is represented as $ \theta^T x $, where $ θ $ is the vector of parameters and $ x $ is the feature set. The first element of $ x $ is set to one to account for the intercept ($ \theta_0 $).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMJTMKPV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDxIjfbY5sbVFPpyl6j5I9aWH8C6TpXboMaV3iM4T1UqQIhAOj%2BQZMcKaZMqVBS6TL5cR0dvTsdRskhGCqRz6fCXGHMKv8DCCkQABoMNjM3NDIzMTgzODA1IgwqkboHZUNkJwDmCJoq3APvFWGe8yKh58oBCOMBVJ0L9vh9o9E9tjdiuFD6H6EcZQ4lg06c9I%2FX0Wr%2FS8nXTj1Q%2B7pLEm6m7fuLqByNr7tU51nGtkT3yksAK1aWzFTQSY9eHeo0xhtLdQqOgZThy8BY4pH0EFu4xc7O7HC3t5zrrz49Dnz4Z9MVxNc7S6pOhLVWRjU%2BEgg2k6ObV9qwJn2Jen16gDxgp4AfH9S6LS7XsD7UHa4RbhT3G%2B9NJbSix4eGqZU4n%2BmGo6xjKGImbUI87bgWVzmsYZoLy5KI68dKk9peybgzPeXqdZdZ97xvbE9AzVMQSTeYH5%2FPyjvSWBRJ4Br7Fc29rCOL0Xb%2BGsUKls9GsTt7l95m4QfXpq%2B2Un2POg9oySVgocGzZg4Zn7eoSAB%2BNRnkPVFtEqy%2FoN7zFgu7BIM0tMmYea6RzE3lINzK6RIkXHMtXRdzp5%2FPc9eGkcti%2F0cjfKKo%2BeZppzVYrDAQn6brMIedQYZeR20ACWTK0aJTp0X31ZpeMFPbBLBp4GXcAtmi7wKJmXyLRXcgEbMFnJ2PIyOnb55T0Y3X7CstSCwrjOxtcXBn%2B0FomWZOjZQZYDbt04Z9b7sKrowoGvtGRW75QuDbM1ExlCP7xy7f2X%2FLqOdWCocF4DCZkYe9BjqkAZMgTgNW%2BNxDPijq%2BvtdGUKfus%2B27byQXmZeZ%2BUcbbhuI2Brfuv5g9zdIr8Hv%2Fmyx9EmNKA%2F9LVQ5kKd37rlCFBxJJ1iYV7AZozotVdc1TOnsSIKkWedTUjzRfVP%2BC3LmxoCWh%2Fz%2Fdewha5t9LOaINytEmNddVranpeBV3MktXq%2F08NlOvearxVID0qPuIdLlaz459kwGW345J9lzF64liFKkpnT&X-Amz-Signature=b2e0ffcb2e86b5c3b9b4712d17a28eebd2b2fd10ae6cdc044b5c4c34b17f0369&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
Here’s an example of implementing Multiple Linear Regression in Python using `scikit-learn`:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Coefficients and intercept
print(f'Intercept: {model.intercept_}')
print(f'Coefficients: {model.coef_}')

# Making predictions
predictions = model.predict(X)
print(f'Predictions: {predictions}')
```
### **Error and Optimization**
- **Error Calculation**: The error for a prediction is the difference between the actual and predicted values. For example, if the actual value $  y $ is 196 and the predicted value $ \hat{y} $ is 140, the error is $ 196−140=56 $.
- **Mean Squared Error (MSE)**: The average of the squared errors across all predictions. The objective is to minimize MSE to find the best parameters.
### **Parameter Estimation Methods**
10. **Ordinary Least Squares (OLS)**: Estimates coefficients by minimizing MSE using matrix operations. Suitable for smaller datasets but can be slow for larger ones.
11. **Optimization Algorithms**: Methods like `Gradient Descent` iteratively adjust coefficients to minimize error. Suitable for large datasets. Some Optimization Algorithms:` Gradient Descent, Stochastic Gradient Descent, Newton’s Metho`
#### **Code Example:**
Here's a simple implementation of Gradient Descent for linear regression:
```python
import numpy as np

def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(iterations):
        gradient = X.T @ (X @ theta - y) / m
        theta -= learning_rate * gradient
    return theta

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Adding intercept term (column of ones)
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Apply gradient descent
theta = gradient_descent(X_b, y)
print(f'Optimized coefficients: {theta}')
```
### **Prediction Phase**
- **Using Parameters**: Once parameters are found, predictions are made by plugging input values into the model equation. For instance, with $ \theta_0 = 125 $, $ \theta_1 = 6.2 $, $ \theta_2 = 14 $, and input values, CO₂ emissions for a car can be predicted.
### **Concerns in Multiple Linear Regression**
- **Number of Variables**: Adding too many variables without justification can lead to overfitting, where the model becomes too complex and less generalizable.
- **Variable Types**: Categorical variables can be included by converting them to numerical values (e.g., coding car type as 0 or 1).
- **Linearity**: Ensure a linear relationship between the dependent variable and independent variables (maybe scatterplot). Non-linear relationships may require non-linear regression.
___
