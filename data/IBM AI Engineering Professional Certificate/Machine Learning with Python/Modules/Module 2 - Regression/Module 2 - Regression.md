

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMN2V76V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDvru3I1MXhouEFC860YZIsU5ICVORiLina4FRP3BktpQIhAPnzrnF1TiCmQACGgJylobW9dCQum2oyX603jbSAB9HjKv8DCC8QABoMNjM3NDIzMTgzODA1IgwqlrORgGEsKIk7VNoq3AOtP23yJkgRHINY3upH0uFCvzpCLP%2BMbi%2B9lOkt0r%2Bp6TK8qIT3NGaDN1azvGoaxEWAfv0TY0jnGkxUu8pBiznb9Bqsrmafr5WL5FXv545kU29JxcCqLN5%2FVMgjFlcqMg%2FMFJaKg4Lmf8DLsv0pTD5fNDyQ5mmtfdrojR8ccITBccpNu73dHYSmcCWjytu5fuX%2F%2Biuli%2BljBBB1V4GYbO9pv0XYLlAImiZMlMs%2F5VIC2Gyz8sIFZliyiP07rL9lMLGPl6XvncrtXlbf%2BoKGoj8mbpHnVsAFuDuan38Bx8hQn%2BjuF6FyGSCghlW7vaqb94iCF4oGcXJBGL5IYyK9T2EDblEHpEWqf05K6U7sf1oQVKFkalQY9VGgzj4A70kptzMbgJVtxEwE57jd4MIWG7bMYlDzqVTjkcNVWh%2B%2BUKD8V2v%2B1JYfTwAMAcSXRX3WWOXWMj0vGhkIeXlH6X3iF0LpOQUhMqiNUD1zvet1Z7OITh4i0rrtzwYV2Z4ItCgoBZdJUIATYjsNKXa8KHdeKAQuh0HZdHNMyGUXzzQptvKy5LaMd4geEK5uIOSqi5TMWOGTXuO0OqYuugskruzRXPlLr5X6D6iEp%2Fsz4LurMARujkkhHWSsgu0b3e1diDCzvIi9BjqkAU3yNN958K5c8uv1ZIgGrUVESAu9v7UkWH1bsi5lE4icHMw%2BYsCT35mN6IKe6hi1ad%2FFsC2vn%2BDqUG1%2Bk87idolIAqfmTNgbWlm4csanehKn2pKZk60FMEPznajsMymaKjuqRXj2IMET9W1ENmgcomMNlPQLQgOnYhz3dn1m9Ix6AZtQp3AcCPP5brEwjNIgrX5isYAaCPSqJS6iJdZI2qULr9u3&X-Amz-Signature=fb06831c645bdf981d03c50a29cfb118f8c16e65514f4fb4d98c980e9098a2d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMN2V76V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDvru3I1MXhouEFC860YZIsU5ICVORiLina4FRP3BktpQIhAPnzrnF1TiCmQACGgJylobW9dCQum2oyX603jbSAB9HjKv8DCC8QABoMNjM3NDIzMTgzODA1IgwqlrORgGEsKIk7VNoq3AOtP23yJkgRHINY3upH0uFCvzpCLP%2BMbi%2B9lOkt0r%2Bp6TK8qIT3NGaDN1azvGoaxEWAfv0TY0jnGkxUu8pBiznb9Bqsrmafr5WL5FXv545kU29JxcCqLN5%2FVMgjFlcqMg%2FMFJaKg4Lmf8DLsv0pTD5fNDyQ5mmtfdrojR8ccITBccpNu73dHYSmcCWjytu5fuX%2F%2Biuli%2BljBBB1V4GYbO9pv0XYLlAImiZMlMs%2F5VIC2Gyz8sIFZliyiP07rL9lMLGPl6XvncrtXlbf%2BoKGoj8mbpHnVsAFuDuan38Bx8hQn%2BjuF6FyGSCghlW7vaqb94iCF4oGcXJBGL5IYyK9T2EDblEHpEWqf05K6U7sf1oQVKFkalQY9VGgzj4A70kptzMbgJVtxEwE57jd4MIWG7bMYlDzqVTjkcNVWh%2B%2BUKD8V2v%2B1JYfTwAMAcSXRX3WWOXWMj0vGhkIeXlH6X3iF0LpOQUhMqiNUD1zvet1Z7OITh4i0rrtzwYV2Z4ItCgoBZdJUIATYjsNKXa8KHdeKAQuh0HZdHNMyGUXzzQptvKy5LaMd4geEK5uIOSqi5TMWOGTXuO0OqYuugskruzRXPlLr5X6D6iEp%2Fsz4LurMARujkkhHWSsgu0b3e1diDCzvIi9BjqkAU3yNN958K5c8uv1ZIgGrUVESAu9v7UkWH1bsi5lE4icHMw%2BYsCT35mN6IKe6hi1ad%2FFsC2vn%2BDqUG1%2Bk87idolIAqfmTNgbWlm4csanehKn2pKZk60FMEPznajsMymaKjuqRXj2IMET9W1ENmgcomMNlPQLQgOnYhz3dn1m9Ix6AZtQp3AcCPP5brEwjNIgrX5isYAaCPSqJS6iJdZI2qULr9u3&X-Amz-Signature=5628cf33890dcb55449575e2fec51c7e46395191ebdae483cc9a412214f45b4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMN2V76V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDvru3I1MXhouEFC860YZIsU5ICVORiLina4FRP3BktpQIhAPnzrnF1TiCmQACGgJylobW9dCQum2oyX603jbSAB9HjKv8DCC8QABoMNjM3NDIzMTgzODA1IgwqlrORgGEsKIk7VNoq3AOtP23yJkgRHINY3upH0uFCvzpCLP%2BMbi%2B9lOkt0r%2Bp6TK8qIT3NGaDN1azvGoaxEWAfv0TY0jnGkxUu8pBiznb9Bqsrmafr5WL5FXv545kU29JxcCqLN5%2FVMgjFlcqMg%2FMFJaKg4Lmf8DLsv0pTD5fNDyQ5mmtfdrojR8ccITBccpNu73dHYSmcCWjytu5fuX%2F%2Biuli%2BljBBB1V4GYbO9pv0XYLlAImiZMlMs%2F5VIC2Gyz8sIFZliyiP07rL9lMLGPl6XvncrtXlbf%2BoKGoj8mbpHnVsAFuDuan38Bx8hQn%2BjuF6FyGSCghlW7vaqb94iCF4oGcXJBGL5IYyK9T2EDblEHpEWqf05K6U7sf1oQVKFkalQY9VGgzj4A70kptzMbgJVtxEwE57jd4MIWG7bMYlDzqVTjkcNVWh%2B%2BUKD8V2v%2B1JYfTwAMAcSXRX3WWOXWMj0vGhkIeXlH6X3iF0LpOQUhMqiNUD1zvet1Z7OITh4i0rrtzwYV2Z4ItCgoBZdJUIATYjsNKXa8KHdeKAQuh0HZdHNMyGUXzzQptvKy5LaMd4geEK5uIOSqi5TMWOGTXuO0OqYuugskruzRXPlLr5X6D6iEp%2Fsz4LurMARujkkhHWSsgu0b3e1diDCzvIi9BjqkAU3yNN958K5c8uv1ZIgGrUVESAu9v7UkWH1bsi5lE4icHMw%2BYsCT35mN6IKe6hi1ad%2FFsC2vn%2BDqUG1%2Bk87idolIAqfmTNgbWlm4csanehKn2pKZk60FMEPznajsMymaKjuqRXj2IMET9W1ENmgcomMNlPQLQgOnYhz3dn1m9Ix6AZtQp3AcCPP5brEwjNIgrX5isYAaCPSqJS6iJdZI2qULr9u3&X-Amz-Signature=b19a1eb869180735c2b814f2e6ed70712b2ecc5c5aaa74f46c09b2a9e31f3b8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMN2V76V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDvru3I1MXhouEFC860YZIsU5ICVORiLina4FRP3BktpQIhAPnzrnF1TiCmQACGgJylobW9dCQum2oyX603jbSAB9HjKv8DCC8QABoMNjM3NDIzMTgzODA1IgwqlrORgGEsKIk7VNoq3AOtP23yJkgRHINY3upH0uFCvzpCLP%2BMbi%2B9lOkt0r%2Bp6TK8qIT3NGaDN1azvGoaxEWAfv0TY0jnGkxUu8pBiznb9Bqsrmafr5WL5FXv545kU29JxcCqLN5%2FVMgjFlcqMg%2FMFJaKg4Lmf8DLsv0pTD5fNDyQ5mmtfdrojR8ccITBccpNu73dHYSmcCWjytu5fuX%2F%2Biuli%2BljBBB1V4GYbO9pv0XYLlAImiZMlMs%2F5VIC2Gyz8sIFZliyiP07rL9lMLGPl6XvncrtXlbf%2BoKGoj8mbpHnVsAFuDuan38Bx8hQn%2BjuF6FyGSCghlW7vaqb94iCF4oGcXJBGL5IYyK9T2EDblEHpEWqf05K6U7sf1oQVKFkalQY9VGgzj4A70kptzMbgJVtxEwE57jd4MIWG7bMYlDzqVTjkcNVWh%2B%2BUKD8V2v%2B1JYfTwAMAcSXRX3WWOXWMj0vGhkIeXlH6X3iF0LpOQUhMqiNUD1zvet1Z7OITh4i0rrtzwYV2Z4ItCgoBZdJUIATYjsNKXa8KHdeKAQuh0HZdHNMyGUXzzQptvKy5LaMd4geEK5uIOSqi5TMWOGTXuO0OqYuugskruzRXPlLr5X6D6iEp%2Fsz4LurMARujkkhHWSsgu0b3e1diDCzvIi9BjqkAU3yNN958K5c8uv1ZIgGrUVESAu9v7UkWH1bsi5lE4icHMw%2BYsCT35mN6IKe6hi1ad%2FFsC2vn%2BDqUG1%2Bk87idolIAqfmTNgbWlm4csanehKn2pKZk60FMEPznajsMymaKjuqRXj2IMET9W1ENmgcomMNlPQLQgOnYhz3dn1m9Ix6AZtQp3AcCPP5brEwjNIgrX5isYAaCPSqJS6iJdZI2qULr9u3&X-Amz-Signature=2a618689b791000b587cd8c12984f328dab91769dffd959dbe7f42a4123d7efb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMN2V76V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDvru3I1MXhouEFC860YZIsU5ICVORiLina4FRP3BktpQIhAPnzrnF1TiCmQACGgJylobW9dCQum2oyX603jbSAB9HjKv8DCC8QABoMNjM3NDIzMTgzODA1IgwqlrORgGEsKIk7VNoq3AOtP23yJkgRHINY3upH0uFCvzpCLP%2BMbi%2B9lOkt0r%2Bp6TK8qIT3NGaDN1azvGoaxEWAfv0TY0jnGkxUu8pBiznb9Bqsrmafr5WL5FXv545kU29JxcCqLN5%2FVMgjFlcqMg%2FMFJaKg4Lmf8DLsv0pTD5fNDyQ5mmtfdrojR8ccITBccpNu73dHYSmcCWjytu5fuX%2F%2Biuli%2BljBBB1V4GYbO9pv0XYLlAImiZMlMs%2F5VIC2Gyz8sIFZliyiP07rL9lMLGPl6XvncrtXlbf%2BoKGoj8mbpHnVsAFuDuan38Bx8hQn%2BjuF6FyGSCghlW7vaqb94iCF4oGcXJBGL5IYyK9T2EDblEHpEWqf05K6U7sf1oQVKFkalQY9VGgzj4A70kptzMbgJVtxEwE57jd4MIWG7bMYlDzqVTjkcNVWh%2B%2BUKD8V2v%2B1JYfTwAMAcSXRX3WWOXWMj0vGhkIeXlH6X3iF0LpOQUhMqiNUD1zvet1Z7OITh4i0rrtzwYV2Z4ItCgoBZdJUIATYjsNKXa8KHdeKAQuh0HZdHNMyGUXzzQptvKy5LaMd4geEK5uIOSqi5TMWOGTXuO0OqYuugskruzRXPlLr5X6D6iEp%2Fsz4LurMARujkkhHWSsgu0b3e1diDCzvIi9BjqkAU3yNN958K5c8uv1ZIgGrUVESAu9v7UkWH1bsi5lE4icHMw%2BYsCT35mN6IKe6hi1ad%2FFsC2vn%2BDqUG1%2Bk87idolIAqfmTNgbWlm4csanehKn2pKZk60FMEPznajsMymaKjuqRXj2IMET9W1ENmgcomMNlPQLQgOnYhz3dn1m9Ix6AZtQp3AcCPP5brEwjNIgrX5isYAaCPSqJS6iJdZI2qULr9u3&X-Amz-Signature=9dc300cb263db6bb1f3476e650ebfd6f3c03a2e24edd075baef48deaf856cae1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMN2V76V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDvru3I1MXhouEFC860YZIsU5ICVORiLina4FRP3BktpQIhAPnzrnF1TiCmQACGgJylobW9dCQum2oyX603jbSAB9HjKv8DCC8QABoMNjM3NDIzMTgzODA1IgwqlrORgGEsKIk7VNoq3AOtP23yJkgRHINY3upH0uFCvzpCLP%2BMbi%2B9lOkt0r%2Bp6TK8qIT3NGaDN1azvGoaxEWAfv0TY0jnGkxUu8pBiznb9Bqsrmafr5WL5FXv545kU29JxcCqLN5%2FVMgjFlcqMg%2FMFJaKg4Lmf8DLsv0pTD5fNDyQ5mmtfdrojR8ccITBccpNu73dHYSmcCWjytu5fuX%2F%2Biuli%2BljBBB1V4GYbO9pv0XYLlAImiZMlMs%2F5VIC2Gyz8sIFZliyiP07rL9lMLGPl6XvncrtXlbf%2BoKGoj8mbpHnVsAFuDuan38Bx8hQn%2BjuF6FyGSCghlW7vaqb94iCF4oGcXJBGL5IYyK9T2EDblEHpEWqf05K6U7sf1oQVKFkalQY9VGgzj4A70kptzMbgJVtxEwE57jd4MIWG7bMYlDzqVTjkcNVWh%2B%2BUKD8V2v%2B1JYfTwAMAcSXRX3WWOXWMj0vGhkIeXlH6X3iF0LpOQUhMqiNUD1zvet1Z7OITh4i0rrtzwYV2Z4ItCgoBZdJUIATYjsNKXa8KHdeKAQuh0HZdHNMyGUXzzQptvKy5LaMd4geEK5uIOSqi5TMWOGTXuO0OqYuugskruzRXPlLr5X6D6iEp%2Fsz4LurMARujkkhHWSsgu0b3e1diDCzvIi9BjqkAU3yNN958K5c8uv1ZIgGrUVESAu9v7UkWH1bsi5lE4icHMw%2BYsCT35mN6IKe6hi1ad%2FFsC2vn%2BDqUG1%2Bk87idolIAqfmTNgbWlm4csanehKn2pKZk60FMEPznajsMymaKjuqRXj2IMET9W1ENmgcomMNlPQLQgOnYhz3dn1m9Ix6AZtQp3AcCPP5brEwjNIgrX5isYAaCPSqJS6iJdZI2qULr9u3&X-Amz-Signature=7207c0c07b4224ee78d031c8db898c7b503fb68afebccb561f13b81fe2ba84d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMN2V76V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDvru3I1MXhouEFC860YZIsU5ICVORiLina4FRP3BktpQIhAPnzrnF1TiCmQACGgJylobW9dCQum2oyX603jbSAB9HjKv8DCC8QABoMNjM3NDIzMTgzODA1IgwqlrORgGEsKIk7VNoq3AOtP23yJkgRHINY3upH0uFCvzpCLP%2BMbi%2B9lOkt0r%2Bp6TK8qIT3NGaDN1azvGoaxEWAfv0TY0jnGkxUu8pBiznb9Bqsrmafr5WL5FXv545kU29JxcCqLN5%2FVMgjFlcqMg%2FMFJaKg4Lmf8DLsv0pTD5fNDyQ5mmtfdrojR8ccITBccpNu73dHYSmcCWjytu5fuX%2F%2Biuli%2BljBBB1V4GYbO9pv0XYLlAImiZMlMs%2F5VIC2Gyz8sIFZliyiP07rL9lMLGPl6XvncrtXlbf%2BoKGoj8mbpHnVsAFuDuan38Bx8hQn%2BjuF6FyGSCghlW7vaqb94iCF4oGcXJBGL5IYyK9T2EDblEHpEWqf05K6U7sf1oQVKFkalQY9VGgzj4A70kptzMbgJVtxEwE57jd4MIWG7bMYlDzqVTjkcNVWh%2B%2BUKD8V2v%2B1JYfTwAMAcSXRX3WWOXWMj0vGhkIeXlH6X3iF0LpOQUhMqiNUD1zvet1Z7OITh4i0rrtzwYV2Z4ItCgoBZdJUIATYjsNKXa8KHdeKAQuh0HZdHNMyGUXzzQptvKy5LaMd4geEK5uIOSqi5TMWOGTXuO0OqYuugskruzRXPlLr5X6D6iEp%2Fsz4LurMARujkkhHWSsgu0b3e1diDCzvIi9BjqkAU3yNN958K5c8uv1ZIgGrUVESAu9v7UkWH1bsi5lE4icHMw%2BYsCT35mN6IKe6hi1ad%2FFsC2vn%2BDqUG1%2Bk87idolIAqfmTNgbWlm4csanehKn2pKZk60FMEPznajsMymaKjuqRXj2IMET9W1ENmgcomMNlPQLQgOnYhz3dn1m9Ix6AZtQp3AcCPP5brEwjNIgrX5isYAaCPSqJS6iJdZI2qULr9u3&X-Amz-Signature=64efdb722fba11719cefbd7e227b8c7af566bf8aee5fcd5e34d8205af4ef70ce&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMN2V76V%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDvru3I1MXhouEFC860YZIsU5ICVORiLina4FRP3BktpQIhAPnzrnF1TiCmQACGgJylobW9dCQum2oyX603jbSAB9HjKv8DCC8QABoMNjM3NDIzMTgzODA1IgwqlrORgGEsKIk7VNoq3AOtP23yJkgRHINY3upH0uFCvzpCLP%2BMbi%2B9lOkt0r%2Bp6TK8qIT3NGaDN1azvGoaxEWAfv0TY0jnGkxUu8pBiznb9Bqsrmafr5WL5FXv545kU29JxcCqLN5%2FVMgjFlcqMg%2FMFJaKg4Lmf8DLsv0pTD5fNDyQ5mmtfdrojR8ccITBccpNu73dHYSmcCWjytu5fuX%2F%2Biuli%2BljBBB1V4GYbO9pv0XYLlAImiZMlMs%2F5VIC2Gyz8sIFZliyiP07rL9lMLGPl6XvncrtXlbf%2BoKGoj8mbpHnVsAFuDuan38Bx8hQn%2BjuF6FyGSCghlW7vaqb94iCF4oGcXJBGL5IYyK9T2EDblEHpEWqf05K6U7sf1oQVKFkalQY9VGgzj4A70kptzMbgJVtxEwE57jd4MIWG7bMYlDzqVTjkcNVWh%2B%2BUKD8V2v%2B1JYfTwAMAcSXRX3WWOXWMj0vGhkIeXlH6X3iF0LpOQUhMqiNUD1zvet1Z7OITh4i0rrtzwYV2Z4ItCgoBZdJUIATYjsNKXa8KHdeKAQuh0HZdHNMyGUXzzQptvKy5LaMd4geEK5uIOSqi5TMWOGTXuO0OqYuugskruzRXPlLr5X6D6iEp%2Fsz4LurMARujkkhHWSsgu0b3e1diDCzvIi9BjqkAU3yNN958K5c8uv1ZIgGrUVESAu9v7UkWH1bsi5lE4icHMw%2BYsCT35mN6IKe6hi1ad%2FFsC2vn%2BDqUG1%2Bk87idolIAqfmTNgbWlm4csanehKn2pKZk60FMEPznajsMymaKjuqRXj2IMET9W1ENmgcomMNlPQLQgOnYhz3dn1m9Ix6AZtQp3AcCPP5brEwjNIgrX5isYAaCPSqJS6iJdZI2qULr9u3&X-Amz-Signature=79ad932389cbdb28115b8a2bb63a2247a589a5483d930d9eeb4b1d6c972b87bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632YWCKRW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQC%2B49Nlnhnwl1mVFbXWg5bQoA8mpJvLyAVg1%2BRXTIbYfAIhANymqUMIq9JMXESR6Mwnn1dV7mGEdN8jHOvGh2q4J75RKv8DCC8QABoMNjM3NDIzMTgzODA1Igy3Siy1Pb3j%2BFf5RFkq3AOrviJiDnAZH5k9hSwc8oPt9BxSTHymUIgVU6z7tnboMrBSNI67Q%2BOGCcVZKIcDhY6NJ4EOy4BqPLzObQPU8oyKuQoWo1UWGEV0fnuCYUnm7jptuSo5Mymk%2BEjQhB8Xo3Vi4kuRd32aQh6eo2mmBTNpJ5uoAUq52Z%2FuiRDukFn00KiRbclr3B52J%2Btb53ZIYPFSl815w3tUzOR6AIkKuBSDxN6kpoQXGhsuwqoC4dtq1qmBtlLLFONTfgtrSdI0pYdvSLxLPD7nqSDifxT5xLMKxAGXabXdAvzpkQzIhj7b8jjwVY1If%2Fl2AyE1pIayet9ZW5BV5G6JgmNneyDNCLA1OOldRgCf3McM%2BLOZngdj74AzYc9bAt01QMascQwMvDbQbmA6xIbeNWXOrn017RKRdryvLz8RiINjEUewBshpQRciixhxZYkRoilswMkb7deY4OfHkj06xZNgKn%2BSyGGcB1i8uOXSASG0B%2BhacfeVVOcNogV9IKC2M%2Btbv2DnAjiyHqpzrROm%2F7bZOwjoO6W6N6zzCYPbaOQMnFZrXAG2J8DadzgYdKXNohYHUsC167TrFbsdMk565%2BiZLkBGHaJIOg9IawyhwqvKb8%2BUavHwbSw5OUwM2H29SjIosTC3vIi9BjqkAZ9sB2YI6hIWEu%2BuP8eTNdM7w2D%2FDsNAUE0BNBmJQZkErAYbF2wjVSLmgmm7kMXeynvIOH4q4tmxzsVC7UMz7kfwgik7%2FkRGvd4OUcOvvU7v8V5p%2BW3oTxY0PRq0hpXBfOtlbE0l39QpHV3rrpUQzNbv8qptrblOFw5FyDpOS55tdjNFNOr4hl7UaZGL5gwx%2FYCUm41IIZFi47GWqjo3BS9iowqU&X-Amz-Signature=3d727bb8b0f40d599256af8370f538d490a438bfbefe0d5bc7b28ac40161a578&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666625WTCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIDwIQEac4orYI%2BMMraV5TL6C5ytX6qg572K2XNXtcz3ZAiEAnbKXccQiVa%2BpWpBVWiLqAez6uhDm57ZTWI4l4T2r1vMq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDLDW4FLHMyYGgOP5YyrcA5Ci6bKdv5kS45T7lvDd1C4Oe%2BCUho1EqTFMXsUiy4Q70PlHNU%2FpnlONe%2B3Z6t9oxtQ7xy%2F7IS8w5kZ3nNLdTJFHN2yLEbFe65lWx0W9dDcNqdPkWSvjDVgV2oLVW%2B2DOkNzC6xdLOtWjLCC5L7qZ0cdNjSh%2BpBoXe6tE4ngbcyyp1%2FjtFRwxTGGQ47k8gqYmcLB0OQPGvhbgICHHZQVDrNaDA6jtKqab6kWDhVN6qQoHU4JO77R%2B5JEjz0MvzdL1q3TP3M92MlH32C7VdspYszMqW9HBW7J7GG8SbqbhaSAq1cUBAa7Mo3w%2FH1gzXFm9lARVXd3oafLOAH799jCLSYzTQ6knuwpEIqHuy0sudXV8VycCHd1uMDCdCCdUdcM84G4BriOOa%2BOFustQJGXPvE%2FpfoTBTGFZ0i08wH5qdZ7%2F3yyxg7e%2Fynu9F2Bzv901p8M0R3leLyQx1SjSxXMC7%2Fg7zrUf1U4jCnHLCdsKQuOEl0duQf8ScF%2Fj7ie%2B6uf47XS%2BMSGqfTgBSnlHJQyBSXhbyu0fhmJnYuZh1JUb5j9DyQPLJ2YHZr7J7dQI4%2BGtX1L1JVAXQIgJZO4JMYRNEuPIUPCRfVtwphHjpOpGItFB6oM3v%2Bzkg4q3SiHMPK8iL0GOqUB0UwLEzisV%2BZtZAbx%2B6%2FWcZxXDghDIH4gl%2FmMXu3avXIQfLCpLhWTchCu1gV6YCgJcc2gvplwzGm3BuOGHSGiFEvLY4xs66YGhDLNW6bxprjuqNB0%2BZ6i8Kj6UBQxb%2BltnEaOsHqgqQcvY8EkxM1C%2BE23BkCLRlEo9N8Mkx1iSg5d6ADkP7taVL8f4w3rUWDMIioomHwGuAJ%2BFh3Ca%2FoZt3o3HKX9&X-Amz-Signature=4355ea56550444f8fc0b0d18a6226855b5d8c1f36fe71212023737be6eb8698d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667L3T5MZZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCiHGHZCMUgbo7urzyHieh1%2B40MtHrXSfuhDl6IuWSOYAIgSEOEe9W6kE%2F4mtu%2FmPlRZQu2hfZm7fLrUWnLOCDDwScq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMB3cuM1Fp4IwI9OVCrcAw52Uxt2mEYsG8Eu6MTe8w3iS5oTp3%2BVwPcWAY4ygIyiabfNUZlagDxMvMZkNP6N%2FLwdp4VvJvDy4Y3dWZPDNp1V3duqBLygZsie1fw80lS3FMK%2FtE3D2RyP%2BbYI7Uw%2FSVGIn92ES4iR6NpTKfas3L5pcjuoG5f6sDufPHSP0v%2Ff3wW0hRIWw8kprGvCCgGWOR9lAzpu%2BqImRdPxud%2BzloAS4CRuwZWjvQ86FUANeFdntKVxcIHIM0NFn4MEonQyTGJrLoGTxcvkg4BJ1BAidLuDoHEPMDXC6Hlm%2Fss2TxcmvMsRcPwKIn7Ce7koicqVoVgK%2BmBSwdALo5RnAXn4rXAdA92r%2FXwpRg%2BaO%2B6u56JRLHD1YuxFB5M0m%2F7iGP9Xrp%2FevjQBsuTOI9jP%2F9n3zRMouSKtajzyMBKGmBNkey%2FJBGh6%2BbuoahSGi5sLqrgLLQEMrTQk%2FFtpvA7vtBP16ElGZgRjzjMyYl9gY3cnpYYAB1OFZnv%2Bg26frG1SbuF8zhnhbizBx3jSeMgvzcUwAr7ijGxA0wCuKb5LPAAS9FHJwCNyIW%2BhJQHhmzkzTNYTZMIOsVyhBCgAMThEw9EBtb%2BzqKLItryOUANdv5%2F0psd%2FGfkNw8BQwyaG3vVmMPe8iL0GOqUB%2FGVPRkSc%2BKxNkKKO%2F3KJGHHhcYnITRrLd8gMkbWQzDsl9hiPgVl3RZJO7jg9tfgOsGviQzW6mnMXp9o5lb415La2gxm%2F2dtUuRaZVGNnEAZ3blbRYhyYDjEyS1t8T0N4rW9S0MCyq7Ki8RNdB%2Fu%2BHR6HjbIpgf%2FTzVvgLS00BiFrvxfv9sWIB7cjALhP6mVsQsKti%2BJozszbDm%2F3dSu%2BDa85qtnN&X-Amz-Signature=4e1614cf03492baff5b41f942a0a9ef725cf17f767d39342686be16d85935587&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667L3T5MZZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQCiHGHZCMUgbo7urzyHieh1%2B40MtHrXSfuhDl6IuWSOYAIgSEOEe9W6kE%2F4mtu%2FmPlRZQu2hfZm7fLrUWnLOCDDwScq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDMB3cuM1Fp4IwI9OVCrcAw52Uxt2mEYsG8Eu6MTe8w3iS5oTp3%2BVwPcWAY4ygIyiabfNUZlagDxMvMZkNP6N%2FLwdp4VvJvDy4Y3dWZPDNp1V3duqBLygZsie1fw80lS3FMK%2FtE3D2RyP%2BbYI7Uw%2FSVGIn92ES4iR6NpTKfas3L5pcjuoG5f6sDufPHSP0v%2Ff3wW0hRIWw8kprGvCCgGWOR9lAzpu%2BqImRdPxud%2BzloAS4CRuwZWjvQ86FUANeFdntKVxcIHIM0NFn4MEonQyTGJrLoGTxcvkg4BJ1BAidLuDoHEPMDXC6Hlm%2Fss2TxcmvMsRcPwKIn7Ce7koicqVoVgK%2BmBSwdALo5RnAXn4rXAdA92r%2FXwpRg%2BaO%2B6u56JRLHD1YuxFB5M0m%2F7iGP9Xrp%2FevjQBsuTOI9jP%2F9n3zRMouSKtajzyMBKGmBNkey%2FJBGh6%2BbuoahSGi5sLqrgLLQEMrTQk%2FFtpvA7vtBP16ElGZgRjzjMyYl9gY3cnpYYAB1OFZnv%2Bg26frG1SbuF8zhnhbizBx3jSeMgvzcUwAr7ijGxA0wCuKb5LPAAS9FHJwCNyIW%2BhJQHhmzkzTNYTZMIOsVyhBCgAMThEw9EBtb%2BzqKLItryOUANdv5%2F0psd%2FGfkNw8BQwyaG3vVmMPe8iL0GOqUB%2FGVPRkSc%2BKxNkKKO%2F3KJGHHhcYnITRrLd8gMkbWQzDsl9hiPgVl3RZJO7jg9tfgOsGviQzW6mnMXp9o5lb415La2gxm%2F2dtUuRaZVGNnEAZ3blbRYhyYDjEyS1t8T0N4rW9S0MCyq7Ki8RNdB%2Fu%2BHR6HjbIpgf%2FTzVvgLS00BiFrvxfv9sWIB7cjALhP6mVsQsKti%2BJozszbDm%2F3dSu%2BDa85qtnN&X-Amz-Signature=e02ca01617d697ae8aa146a264efaf282668115a76d0cbdfb7fcdd7b2b2b8e9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
