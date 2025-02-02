

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXS7JVWD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qLPKmDKlqaDwrF0gMrIDMdr%2BR25M52iPehxsr8tIQAiAWJeo8%2FwAfl5q4ZQxnHEFDQmaP9IGP9rav5yVa%2F6AiSSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1scc6MNfYKDe44LjKtwDoYBkKhUVAGOC9%2B0CQgOxljXmgiuSbVhKN%2BVWuobnLu5nI6156d%2F3zKH7tSodLiA4v7x6rW1Wz%2BDOCTUS92R5%2BnT7JVfk25TNjtmlnn0uOJzBMQ8D32Rx15Hyz5RLhvPd5U%2B36uUhtgSulj%2BOtdapLTGcJZUjNJpH95tC1q3740wWJ83x4S87k9DU2Bkw0S0jc6IOwuK63DSQc0Qfi8MtcxrXMb3MAoD1T76uxGOGiTDKgWxJ%2F8DmdnRi%2Fu2%2FrsBHDgnNUfmK%2F%2FzuRbxEHnfIb92XfOujwZ3kOOp3t6bqzuMSIc9L2fas2YKdGucsCVrS7aa%2BqTQeTemlZMZTp4cI36y1enCg3VdrL29qh89BD2FDsgUDzU2ZNv%2B%2FAgl7v0rLKZ90V0ocD1gK7D%2FG91nrUwX%2F%2FsyCyE5Ee6HilwhVOQmDcI6j%2FyQ45v4phQWOhWNQyx8hAQ5pMeyiPtSw3yZlymSVlSQpAv8%2FPvtb7kTi5usU9RqG9wBmIuINFk1q4hM6RvwfRUhMm8WEZwSg0DCPOxdUpCgrIkl75cYQpafuYlKEX%2Fdhg0O5q9ZouoOFAV9uVv4DrnsesQvC9b2EFENVc30ThlMeSRMSJ8eB6IPdUg6z70OKqNUPpZJerokw%2Bpv8vAY6pgFuMNDNKX25iTyyvx5UYS6ucpq6xFeVGZra7WYdsyJ5Qgveh28o3mJ%2BIgv1sSFQWzV4CV87F%2BPKiGLjpueKgNzxbu89nlv2NN06nQeHS%2FHY%2BSvGUqPa5%2FQNUzwcJQPt878xYdTjk4%2FUuDFcSorhzkGFWRRbRIiNr6Swhxv7AkZf3rtqo9JNrP1Rrq3hiv%2BCLD3kh8LrB1tU%2BRDfB0xvcD23USa%2FXhQr&X-Amz-Signature=e30ed25b3bd81bd602974950b117c80eb1a62fdaa57645c31cfa9389ff1daddf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXS7JVWD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qLPKmDKlqaDwrF0gMrIDMdr%2BR25M52iPehxsr8tIQAiAWJeo8%2FwAfl5q4ZQxnHEFDQmaP9IGP9rav5yVa%2F6AiSSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1scc6MNfYKDe44LjKtwDoYBkKhUVAGOC9%2B0CQgOxljXmgiuSbVhKN%2BVWuobnLu5nI6156d%2F3zKH7tSodLiA4v7x6rW1Wz%2BDOCTUS92R5%2BnT7JVfk25TNjtmlnn0uOJzBMQ8D32Rx15Hyz5RLhvPd5U%2B36uUhtgSulj%2BOtdapLTGcJZUjNJpH95tC1q3740wWJ83x4S87k9DU2Bkw0S0jc6IOwuK63DSQc0Qfi8MtcxrXMb3MAoD1T76uxGOGiTDKgWxJ%2F8DmdnRi%2Fu2%2FrsBHDgnNUfmK%2F%2FzuRbxEHnfIb92XfOujwZ3kOOp3t6bqzuMSIc9L2fas2YKdGucsCVrS7aa%2BqTQeTemlZMZTp4cI36y1enCg3VdrL29qh89BD2FDsgUDzU2ZNv%2B%2FAgl7v0rLKZ90V0ocD1gK7D%2FG91nrUwX%2F%2FsyCyE5Ee6HilwhVOQmDcI6j%2FyQ45v4phQWOhWNQyx8hAQ5pMeyiPtSw3yZlymSVlSQpAv8%2FPvtb7kTi5usU9RqG9wBmIuINFk1q4hM6RvwfRUhMm8WEZwSg0DCPOxdUpCgrIkl75cYQpafuYlKEX%2Fdhg0O5q9ZouoOFAV9uVv4DrnsesQvC9b2EFENVc30ThlMeSRMSJ8eB6IPdUg6z70OKqNUPpZJerokw%2Bpv8vAY6pgFuMNDNKX25iTyyvx5UYS6ucpq6xFeVGZra7WYdsyJ5Qgveh28o3mJ%2BIgv1sSFQWzV4CV87F%2BPKiGLjpueKgNzxbu89nlv2NN06nQeHS%2FHY%2BSvGUqPa5%2FQNUzwcJQPt878xYdTjk4%2FUuDFcSorhzkGFWRRbRIiNr6Swhxv7AkZf3rtqo9JNrP1Rrq3hiv%2BCLD3kh8LrB1tU%2BRDfB0xvcD23USa%2FXhQr&X-Amz-Signature=26da7cd209aeee5a51266cb71d89557550ff2df5754e737e6c81819c3d20c550&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXS7JVWD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qLPKmDKlqaDwrF0gMrIDMdr%2BR25M52iPehxsr8tIQAiAWJeo8%2FwAfl5q4ZQxnHEFDQmaP9IGP9rav5yVa%2F6AiSSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1scc6MNfYKDe44LjKtwDoYBkKhUVAGOC9%2B0CQgOxljXmgiuSbVhKN%2BVWuobnLu5nI6156d%2F3zKH7tSodLiA4v7x6rW1Wz%2BDOCTUS92R5%2BnT7JVfk25TNjtmlnn0uOJzBMQ8D32Rx15Hyz5RLhvPd5U%2B36uUhtgSulj%2BOtdapLTGcJZUjNJpH95tC1q3740wWJ83x4S87k9DU2Bkw0S0jc6IOwuK63DSQc0Qfi8MtcxrXMb3MAoD1T76uxGOGiTDKgWxJ%2F8DmdnRi%2Fu2%2FrsBHDgnNUfmK%2F%2FzuRbxEHnfIb92XfOujwZ3kOOp3t6bqzuMSIc9L2fas2YKdGucsCVrS7aa%2BqTQeTemlZMZTp4cI36y1enCg3VdrL29qh89BD2FDsgUDzU2ZNv%2B%2FAgl7v0rLKZ90V0ocD1gK7D%2FG91nrUwX%2F%2FsyCyE5Ee6HilwhVOQmDcI6j%2FyQ45v4phQWOhWNQyx8hAQ5pMeyiPtSw3yZlymSVlSQpAv8%2FPvtb7kTi5usU9RqG9wBmIuINFk1q4hM6RvwfRUhMm8WEZwSg0DCPOxdUpCgrIkl75cYQpafuYlKEX%2Fdhg0O5q9ZouoOFAV9uVv4DrnsesQvC9b2EFENVc30ThlMeSRMSJ8eB6IPdUg6z70OKqNUPpZJerokw%2Bpv8vAY6pgFuMNDNKX25iTyyvx5UYS6ucpq6xFeVGZra7WYdsyJ5Qgveh28o3mJ%2BIgv1sSFQWzV4CV87F%2BPKiGLjpueKgNzxbu89nlv2NN06nQeHS%2FHY%2BSvGUqPa5%2FQNUzwcJQPt878xYdTjk4%2FUuDFcSorhzkGFWRRbRIiNr6Swhxv7AkZf3rtqo9JNrP1Rrq3hiv%2BCLD3kh8LrB1tU%2BRDfB0xvcD23USa%2FXhQr&X-Amz-Signature=866e53852f32def81002fd8b577360556b93cf1963f7e6a380f49d76a106031d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXS7JVWD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qLPKmDKlqaDwrF0gMrIDMdr%2BR25M52iPehxsr8tIQAiAWJeo8%2FwAfl5q4ZQxnHEFDQmaP9IGP9rav5yVa%2F6AiSSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1scc6MNfYKDe44LjKtwDoYBkKhUVAGOC9%2B0CQgOxljXmgiuSbVhKN%2BVWuobnLu5nI6156d%2F3zKH7tSodLiA4v7x6rW1Wz%2BDOCTUS92R5%2BnT7JVfk25TNjtmlnn0uOJzBMQ8D32Rx15Hyz5RLhvPd5U%2B36uUhtgSulj%2BOtdapLTGcJZUjNJpH95tC1q3740wWJ83x4S87k9DU2Bkw0S0jc6IOwuK63DSQc0Qfi8MtcxrXMb3MAoD1T76uxGOGiTDKgWxJ%2F8DmdnRi%2Fu2%2FrsBHDgnNUfmK%2F%2FzuRbxEHnfIb92XfOujwZ3kOOp3t6bqzuMSIc9L2fas2YKdGucsCVrS7aa%2BqTQeTemlZMZTp4cI36y1enCg3VdrL29qh89BD2FDsgUDzU2ZNv%2B%2FAgl7v0rLKZ90V0ocD1gK7D%2FG91nrUwX%2F%2FsyCyE5Ee6HilwhVOQmDcI6j%2FyQ45v4phQWOhWNQyx8hAQ5pMeyiPtSw3yZlymSVlSQpAv8%2FPvtb7kTi5usU9RqG9wBmIuINFk1q4hM6RvwfRUhMm8WEZwSg0DCPOxdUpCgrIkl75cYQpafuYlKEX%2Fdhg0O5q9ZouoOFAV9uVv4DrnsesQvC9b2EFENVc30ThlMeSRMSJ8eB6IPdUg6z70OKqNUPpZJerokw%2Bpv8vAY6pgFuMNDNKX25iTyyvx5UYS6ucpq6xFeVGZra7WYdsyJ5Qgveh28o3mJ%2BIgv1sSFQWzV4CV87F%2BPKiGLjpueKgNzxbu89nlv2NN06nQeHS%2FHY%2BSvGUqPa5%2FQNUzwcJQPt878xYdTjk4%2FUuDFcSorhzkGFWRRbRIiNr6Swhxv7AkZf3rtqo9JNrP1Rrq3hiv%2BCLD3kh8LrB1tU%2BRDfB0xvcD23USa%2FXhQr&X-Amz-Signature=cd536f10245a64baacb157d983177cfec5e743a62e561060d0442364793d6807&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXS7JVWD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qLPKmDKlqaDwrF0gMrIDMdr%2BR25M52iPehxsr8tIQAiAWJeo8%2FwAfl5q4ZQxnHEFDQmaP9IGP9rav5yVa%2F6AiSSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1scc6MNfYKDe44LjKtwDoYBkKhUVAGOC9%2B0CQgOxljXmgiuSbVhKN%2BVWuobnLu5nI6156d%2F3zKH7tSodLiA4v7x6rW1Wz%2BDOCTUS92R5%2BnT7JVfk25TNjtmlnn0uOJzBMQ8D32Rx15Hyz5RLhvPd5U%2B36uUhtgSulj%2BOtdapLTGcJZUjNJpH95tC1q3740wWJ83x4S87k9DU2Bkw0S0jc6IOwuK63DSQc0Qfi8MtcxrXMb3MAoD1T76uxGOGiTDKgWxJ%2F8DmdnRi%2Fu2%2FrsBHDgnNUfmK%2F%2FzuRbxEHnfIb92XfOujwZ3kOOp3t6bqzuMSIc9L2fas2YKdGucsCVrS7aa%2BqTQeTemlZMZTp4cI36y1enCg3VdrL29qh89BD2FDsgUDzU2ZNv%2B%2FAgl7v0rLKZ90V0ocD1gK7D%2FG91nrUwX%2F%2FsyCyE5Ee6HilwhVOQmDcI6j%2FyQ45v4phQWOhWNQyx8hAQ5pMeyiPtSw3yZlymSVlSQpAv8%2FPvtb7kTi5usU9RqG9wBmIuINFk1q4hM6RvwfRUhMm8WEZwSg0DCPOxdUpCgrIkl75cYQpafuYlKEX%2Fdhg0O5q9ZouoOFAV9uVv4DrnsesQvC9b2EFENVc30ThlMeSRMSJ8eB6IPdUg6z70OKqNUPpZJerokw%2Bpv8vAY6pgFuMNDNKX25iTyyvx5UYS6ucpq6xFeVGZra7WYdsyJ5Qgveh28o3mJ%2BIgv1sSFQWzV4CV87F%2BPKiGLjpueKgNzxbu89nlv2NN06nQeHS%2FHY%2BSvGUqPa5%2FQNUzwcJQPt878xYdTjk4%2FUuDFcSorhzkGFWRRbRIiNr6Swhxv7AkZf3rtqo9JNrP1Rrq3hiv%2BCLD3kh8LrB1tU%2BRDfB0xvcD23USa%2FXhQr&X-Amz-Signature=46f252d28d866e01bd07904462c6b931f6b9a3c867dce4a9629614773d77f618&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXS7JVWD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qLPKmDKlqaDwrF0gMrIDMdr%2BR25M52iPehxsr8tIQAiAWJeo8%2FwAfl5q4ZQxnHEFDQmaP9IGP9rav5yVa%2F6AiSSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1scc6MNfYKDe44LjKtwDoYBkKhUVAGOC9%2B0CQgOxljXmgiuSbVhKN%2BVWuobnLu5nI6156d%2F3zKH7tSodLiA4v7x6rW1Wz%2BDOCTUS92R5%2BnT7JVfk25TNjtmlnn0uOJzBMQ8D32Rx15Hyz5RLhvPd5U%2B36uUhtgSulj%2BOtdapLTGcJZUjNJpH95tC1q3740wWJ83x4S87k9DU2Bkw0S0jc6IOwuK63DSQc0Qfi8MtcxrXMb3MAoD1T76uxGOGiTDKgWxJ%2F8DmdnRi%2Fu2%2FrsBHDgnNUfmK%2F%2FzuRbxEHnfIb92XfOujwZ3kOOp3t6bqzuMSIc9L2fas2YKdGucsCVrS7aa%2BqTQeTemlZMZTp4cI36y1enCg3VdrL29qh89BD2FDsgUDzU2ZNv%2B%2FAgl7v0rLKZ90V0ocD1gK7D%2FG91nrUwX%2F%2FsyCyE5Ee6HilwhVOQmDcI6j%2FyQ45v4phQWOhWNQyx8hAQ5pMeyiPtSw3yZlymSVlSQpAv8%2FPvtb7kTi5usU9RqG9wBmIuINFk1q4hM6RvwfRUhMm8WEZwSg0DCPOxdUpCgrIkl75cYQpafuYlKEX%2Fdhg0O5q9ZouoOFAV9uVv4DrnsesQvC9b2EFENVc30ThlMeSRMSJ8eB6IPdUg6z70OKqNUPpZJerokw%2Bpv8vAY6pgFuMNDNKX25iTyyvx5UYS6ucpq6xFeVGZra7WYdsyJ5Qgveh28o3mJ%2BIgv1sSFQWzV4CV87F%2BPKiGLjpueKgNzxbu89nlv2NN06nQeHS%2FHY%2BSvGUqPa5%2FQNUzwcJQPt878xYdTjk4%2FUuDFcSorhzkGFWRRbRIiNr6Swhxv7AkZf3rtqo9JNrP1Rrq3hiv%2BCLD3kh8LrB1tU%2BRDfB0xvcD23USa%2FXhQr&X-Amz-Signature=690a155298e8c90fa52a5dda9ec3d24a0388e3ecf261909751da4c5cc07aa944&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXS7JVWD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qLPKmDKlqaDwrF0gMrIDMdr%2BR25M52iPehxsr8tIQAiAWJeo8%2FwAfl5q4ZQxnHEFDQmaP9IGP9rav5yVa%2F6AiSSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1scc6MNfYKDe44LjKtwDoYBkKhUVAGOC9%2B0CQgOxljXmgiuSbVhKN%2BVWuobnLu5nI6156d%2F3zKH7tSodLiA4v7x6rW1Wz%2BDOCTUS92R5%2BnT7JVfk25TNjtmlnn0uOJzBMQ8D32Rx15Hyz5RLhvPd5U%2B36uUhtgSulj%2BOtdapLTGcJZUjNJpH95tC1q3740wWJ83x4S87k9DU2Bkw0S0jc6IOwuK63DSQc0Qfi8MtcxrXMb3MAoD1T76uxGOGiTDKgWxJ%2F8DmdnRi%2Fu2%2FrsBHDgnNUfmK%2F%2FzuRbxEHnfIb92XfOujwZ3kOOp3t6bqzuMSIc9L2fas2YKdGucsCVrS7aa%2BqTQeTemlZMZTp4cI36y1enCg3VdrL29qh89BD2FDsgUDzU2ZNv%2B%2FAgl7v0rLKZ90V0ocD1gK7D%2FG91nrUwX%2F%2FsyCyE5Ee6HilwhVOQmDcI6j%2FyQ45v4phQWOhWNQyx8hAQ5pMeyiPtSw3yZlymSVlSQpAv8%2FPvtb7kTi5usU9RqG9wBmIuINFk1q4hM6RvwfRUhMm8WEZwSg0DCPOxdUpCgrIkl75cYQpafuYlKEX%2Fdhg0O5q9ZouoOFAV9uVv4DrnsesQvC9b2EFENVc30ThlMeSRMSJ8eB6IPdUg6z70OKqNUPpZJerokw%2Bpv8vAY6pgFuMNDNKX25iTyyvx5UYS6ucpq6xFeVGZra7WYdsyJ5Qgveh28o3mJ%2BIgv1sSFQWzV4CV87F%2BPKiGLjpueKgNzxbu89nlv2NN06nQeHS%2FHY%2BSvGUqPa5%2FQNUzwcJQPt878xYdTjk4%2FUuDFcSorhzkGFWRRbRIiNr6Swhxv7AkZf3rtqo9JNrP1Rrq3hiv%2BCLD3kh8LrB1tU%2BRDfB0xvcD23USa%2FXhQr&X-Amz-Signature=779b4dedf22279a0c67d176be5335869cb32daf8f43307a1b679e4a61df13e6e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXS7JVWD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0qLPKmDKlqaDwrF0gMrIDMdr%2BR25M52iPehxsr8tIQAiAWJeo8%2FwAfl5q4ZQxnHEFDQmaP9IGP9rav5yVa%2F6AiSSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1scc6MNfYKDe44LjKtwDoYBkKhUVAGOC9%2B0CQgOxljXmgiuSbVhKN%2BVWuobnLu5nI6156d%2F3zKH7tSodLiA4v7x6rW1Wz%2BDOCTUS92R5%2BnT7JVfk25TNjtmlnn0uOJzBMQ8D32Rx15Hyz5RLhvPd5U%2B36uUhtgSulj%2BOtdapLTGcJZUjNJpH95tC1q3740wWJ83x4S87k9DU2Bkw0S0jc6IOwuK63DSQc0Qfi8MtcxrXMb3MAoD1T76uxGOGiTDKgWxJ%2F8DmdnRi%2Fu2%2FrsBHDgnNUfmK%2F%2FzuRbxEHnfIb92XfOujwZ3kOOp3t6bqzuMSIc9L2fas2YKdGucsCVrS7aa%2BqTQeTemlZMZTp4cI36y1enCg3VdrL29qh89BD2FDsgUDzU2ZNv%2B%2FAgl7v0rLKZ90V0ocD1gK7D%2FG91nrUwX%2F%2FsyCyE5Ee6HilwhVOQmDcI6j%2FyQ45v4phQWOhWNQyx8hAQ5pMeyiPtSw3yZlymSVlSQpAv8%2FPvtb7kTi5usU9RqG9wBmIuINFk1q4hM6RvwfRUhMm8WEZwSg0DCPOxdUpCgrIkl75cYQpafuYlKEX%2Fdhg0O5q9ZouoOFAV9uVv4DrnsesQvC9b2EFENVc30ThlMeSRMSJ8eB6IPdUg6z70OKqNUPpZJerokw%2Bpv8vAY6pgFuMNDNKX25iTyyvx5UYS6ucpq6xFeVGZra7WYdsyJ5Qgveh28o3mJ%2BIgv1sSFQWzV4CV87F%2BPKiGLjpueKgNzxbu89nlv2NN06nQeHS%2FHY%2BSvGUqPa5%2FQNUzwcJQPt878xYdTjk4%2FUuDFcSorhzkGFWRRbRIiNr6Swhxv7AkZf3rtqo9JNrP1Rrq3hiv%2BCLD3kh8LrB1tU%2BRDfB0xvcD23USa%2FXhQr&X-Amz-Signature=38bb09467dfe50d298067d8b65556c7a59b3b2c0b5db83895c251a7916ae3df5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WD6MYYB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAC%2BUV8KrQNkmpjM9cGAEnPyi%2BkWaTiLZGHmDwWvtNzTAiADcMx0YciZuoY%2Fe41Q7TKGunXjVRPxvvDqeDKthrPWjCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDQG7IIyTyGHXg9PXKtwD6oS0j3scMpUdi7MlYkbu8jumhpBL%2BVOARUehde39n4VRKSK8riJmtnFrsq%2BD%2Fl4cplVxI9qomjAMZqhmgjrQlzY3ffiQrUdSLhZcOR7TA32Gnh%2Fhk4rRVtK5KjRhc0CVA%2BBNFS68ONxTZKWxaHX%2FikVsqn3oM%2FjezwuhjVc8pf%2Bi8zoy6wBsHSBYsSQj8L5mLGg29i5YqXwvTSrtsIeSFnEOIr1%2B2FUS3KFi3IsJGkyDchHnfxUWN2tMoNqz7%2F4TItZygBHBnEQ1RRJw%2FY1r2mcJesuxJlERdScZpSPQY39GTrtWFnE8X7C4LCAxTaOjKE%2BJWIHmiArJ%2F2NT4mFUooUpb45%2BRwX7WWX%2BCR6IgkAuU3UuUa2KOwVw%2BmcG16MwF6%2F%2FJeujLII7Lt3Ht%2FGvdUfDyIqZfNG2asWI8%2BBxWJzoFYBqI7uusE0MUDZUoZnW0Y55aypnn%2F8nTPi1VZUsCYZ8qlkvlzmNYQF2gBIo3Rzytpyx5upt4agi90BoXid7O5ZPqTJENvyrwigN7Gryh6w1nOxJgWQ%2BRL2X300V3Pz8ZlGPX4xY1TOr5ikKfBYs6LKsk7dnKJoPAqBxQnh32xiC2XsXAWg22MWAS2uIANjgIc0mBo973PcCmB0wzpv8vAY6pgHCTei%2FnXAYbf%2F1LVgjnBfc9KTql0d0Efsiy9Y9UTXqD6%2B9u%2FwbfLmidg%2F%2FkzYh5Lv1QkITpjD%2Fr%2FfbG%2BtrV4hVmistj%2FlhGL3jk72lFR3VNoMgTZsdsTTYKfS9JD9lkIQN45YbJaQM4s1ThHQjoHi6od%2Be9MeyLqRO1HM%2BefBN1C19SSpNOn9i9Jm1%2FWB4B6LHjxM368WIhRmVkJDfRwTEbD4KiXdk&X-Amz-Signature=bd1d01ddda70d061a9b7108b3007b09d6d2c3422e41d115604d44670cb7eb8f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFKCY4XA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTyb6keO5XPZ3mXK5cLfJmoUnH%2BPzbMYvN4QF%2FagB57AIgagBlYBbuj9gwbi3RLt4pnCSEIoh6JyLs3m9hD8Avrr0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNH3iZK4eAtycH15yrcA7kgmvcPSSZnpZHJa8PPv3dtRVqbSxLUK1BVOdqqirp5rojZFmmNegp8gZAylg%2FyMM9SbtCMbezuq3A7KY1kqU7h9ksQZn7L5Hxt9rY96DAcCo0eMlJYzNBli4DZ03IZ7UxkJ37yuPeII9IenqUtqgLf8SFd2fcTcfg9Rs%2BLqNe006Rf0MoFrY22p2lP5d5X6ej8J56kNmNwtVX%2Fb9t8d3Bd2RWDHajmYGG1QYiiDgB0ERklzjxEA7ceEstkNrxVIOPIHfyrCZfDTQq5RNJWK64eKblwlW2tJefML9uyYouy02%2BCJDbnBSQewhzRCQ5c8MdIM5gmvK%2B0XvMoYh1ibdSx%2Bqqo6VGRPSG4xwDG3XM0nF6EWZyJqEYGmaSXEzDZb02wjUTIScsaTMEiEaHlrbRYJo2cNHeU8wPFwDNJ%2B%2BzLpXFEGEnQRmNV4uSBQIW2xlABfrFdnFIG8EOxrV99DR0esfiNxTaFLG55cfBQ%2BQXLwmfX6xEP8mOx%2BOIfb70dL89RFFTsIL%2FldjWL8EOr7Mp2N%2FTmFRD5JFe2aoBXy40LnpPHhPM5cmX9S%2FFKky3IKqGUg04fDzl1gByJsYdtiBPITZRMVxuvp8%2FdfkoobVfPrJ08I6i8R4Bti5wjMO6b%2FLwGOqUBxjP6Z0qbCDYu0Ec8ytIqepTHP2LjVyye8u8HtwaJ6VNjnvBVFQl56PLDraxrEonSl%2FhEjwfK2jo1f%2FXUgaDGjYBfxmEBg62Px7WvunNXsJoaQV375CPGLYs3C38E1uMi%2Fpy3Bh5ZM9XN3Eh2BGAYHhFZADNsbw1pF2QLUrAUiohXvOFFMOt%2BZ0rQeKm1i965ZkegkJC2QoELSXDX2V8ZJ2%2BNvi74&X-Amz-Signature=b5e1bef033fe1758a521e3894fdbca002b8a49610bde735849f0249ee06a0100&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466474RM3G3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWGd0Ne2Sb6pjx1uqL5Y%2BG8UAzIq%2FNHe3jRjE4h8en7AIgXHVJKkzLhLu3R2DV1MiNCHy5Il0RUqvOaPSEhDD1F2UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz%2BNIeOcK2cp%2B5L3ircA53186oky%2BBUmGmgQkmVqjRftXy6EZM0MFUObkxvwg68AQPBCbdKrrKM0AKbfgS0zfFfh%2FC7pb6unZ2zlFmw8nIcSabZo9Vy37MonSIgO1CtcfB0eOJ0GZwZpAGTLd1sYZopBZrNVC2qd4Ukv8fF7FMNayeDxl2U2HROgtxp7I4%2FJ3Pq0CQ4YuaTOgxkGRbn1lRuiaIRLlE3Bw4dQXfSyBVS0RGJWutumzhh%2B4EEzBHmQNyZEyZxUr9eyKPtbX0IOioKqrTlxbU0PTScVHW5t5xBRGqEbbhXAiE29yr%2FdS40YAMkPZNDnKzGPIDwNoee9AKGWvk7C7BYg4PGnjv81%2BTDXCUwHKRiQpvIvmv6axcACCBPGC2FzdpvggHiKo8GLYjLJ7i3e2OM%2FexYBTYcMrMmsboyndC6cwV5ZoZWGyahdv9r%2FOkMzBxGQSZ9TVf3Q%2FZLSEFKiY8qRqbDOW%2FEmkdGvxoY%2BXFKYlKFQwQCxtFFfwUiYVAjSonHkgOrvdSdpZwO%2BeQHrGASngQF2vwdj8azjSidYYP%2BS%2B%2BIcXfOszdlMgWBYkiylOLENpGSVcO%2F6vFe9r4XpxzRl2Z%2FpWYqcS%2BFOFF14mhOcK94mFqyCiLrHc%2ByLXa%2BuEhAbmZaMKOc%2FLwGOqUBMOMAiR6JONHqIKktrqaNh%2BhELlbSoayCM4cklfEWHQeIf9fgBGHSaRNxdIhUycwgLnwOi2JjdAq5CX0DOQvJSlhAhcB2IgR2%2BzB203fxE%2BdYOmbBMB%2BBm52MdW8IAzQHXucC7tczExl1QFsszXNQP9xeVKn4WcCjz7l6a2585MSsdCIRVOwrovHqJmtJgr0jCS%2BqsuuaFn%2B7aRIFUdiOqR6ZYCZ5&X-Amz-Signature=c503f34881cd52844d0366ca92e7b9c583d4c5d6aea2d02b3a68a64f693a2b05&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466474RM3G3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWGd0Ne2Sb6pjx1uqL5Y%2BG8UAzIq%2FNHe3jRjE4h8en7AIgXHVJKkzLhLu3R2DV1MiNCHy5Il0RUqvOaPSEhDD1F2UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHz%2BNIeOcK2cp%2B5L3ircA53186oky%2BBUmGmgQkmVqjRftXy6EZM0MFUObkxvwg68AQPBCbdKrrKM0AKbfgS0zfFfh%2FC7pb6unZ2zlFmw8nIcSabZo9Vy37MonSIgO1CtcfB0eOJ0GZwZpAGTLd1sYZopBZrNVC2qd4Ukv8fF7FMNayeDxl2U2HROgtxp7I4%2FJ3Pq0CQ4YuaTOgxkGRbn1lRuiaIRLlE3Bw4dQXfSyBVS0RGJWutumzhh%2B4EEzBHmQNyZEyZxUr9eyKPtbX0IOioKqrTlxbU0PTScVHW5t5xBRGqEbbhXAiE29yr%2FdS40YAMkPZNDnKzGPIDwNoee9AKGWvk7C7BYg4PGnjv81%2BTDXCUwHKRiQpvIvmv6axcACCBPGC2FzdpvggHiKo8GLYjLJ7i3e2OM%2FexYBTYcMrMmsboyndC6cwV5ZoZWGyahdv9r%2FOkMzBxGQSZ9TVf3Q%2FZLSEFKiY8qRqbDOW%2FEmkdGvxoY%2BXFKYlKFQwQCxtFFfwUiYVAjSonHkgOrvdSdpZwO%2BeQHrGASngQF2vwdj8azjSidYYP%2BS%2B%2BIcXfOszdlMgWBYkiylOLENpGSVcO%2F6vFe9r4XpxzRl2Z%2FpWYqcS%2BFOFF14mhOcK94mFqyCiLrHc%2ByLXa%2BuEhAbmZaMKOc%2FLwGOqUBMOMAiR6JONHqIKktrqaNh%2BhELlbSoayCM4cklfEWHQeIf9fgBGHSaRNxdIhUycwgLnwOi2JjdAq5CX0DOQvJSlhAhcB2IgR2%2BzB203fxE%2BdYOmbBMB%2BBm52MdW8IAzQHXucC7tczExl1QFsszXNQP9xeVKn4WcCjz7l6a2585MSsdCIRVOwrovHqJmtJgr0jCS%2BqsuuaFn%2B7aRIFUdiOqR6ZYCZ5&X-Amz-Signature=f3692af0563529df1bdd0fd577ba945cdb540d002e2a4ecdba4a6494a4fe8c57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
