

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VNSCZGK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIESZTbRuS391BSzycFp6meVYg3TquZe8pOemPRG78HkpAiEA0J6Rq4YFh6tcTwQlLjLFPyVXC%2FBoscm4BsV5gQ1U1P8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGca0WxuD6z00VJ3mCrcA95XrGv3Ij49LroK%2BA7b%2BU4y6Z4duROdcfEyxkPmr0utX5rLwVBz9ktO7rSerUkP4isxrSuGCFfV9q5UUMMV3yzYY06J0tUcm3xS7w0mfu%2BWgziZEyXioJVrltnE%2BJUpV7QbkB5rM3QG%2FD6yy4LHwpAPyskOLmuMFLXXvVZCMqU%2F02eQCJZE51uuCR8mDJs91s8A4pR%2FOv1sB7bSNrJ7PnpaZnPBbF7TL%2BvYhksBbMycdlH7ENqOcjOz1SFE9tPp4O6IvR1%2BtIoNITZbvCe4k5fiVn33fx1G%2B2yY%2BvEGqn3qJwZ9I2G5w1zkJaf75lGVMy%2Bjt18mHzHy4NYusKztDO9vEjEy%2BEdXIHXIzCc1iJE2gOmm1U5NfwbmGguB29%2Bzd7uuDYCECM96e6MOjUtlJvazhEiFKQ48vLTfGZP0uc4iQ4t7Xixafhjaop8RHj1D8QutLBKOiyjiQBp44GZnVOXm4kngdSWPihn%2FXfOrHFHgU0SalQ9QYFsafPJUFqnMtH6juW0RC%2Ff6Vx2wubA51ZoCrL5un92VOJY%2B28Khh0EK17H2rVBM3cvrWW8yj7vVXseeth92wlflCWiBUX%2BEhLkPKt8N300DjPhoHxvNIwzBwxlrWcpRAq6hHaSOMOef5rwGOqUBiu7uVl6CFOnne1I6rtM0XZPbqQudcdYd8dMz9JkIeqccVCSWmrEPU3GYffvkf4L52bhYG1Q4BRQ8ysK3LqyBIaAtGQgdqkoiZxICrz9Qf87WEKZwj1pvuJhMcJkQKarQs4Y9rJYPs%2BH8FLvhuAs5ol79i8XeBhdWDP5uMyzSpFm5Z3HhmD9o0IQexTPM9nQ9JdoQrhx%2FbkrOvdv8KV%2FaAoov%2FTFk&X-Amz-Signature=0fb184983aa0c5dfe9b21564aa97e97e0e368d9fae6601b17e1953447474911b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VNSCZGK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIESZTbRuS391BSzycFp6meVYg3TquZe8pOemPRG78HkpAiEA0J6Rq4YFh6tcTwQlLjLFPyVXC%2FBoscm4BsV5gQ1U1P8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGca0WxuD6z00VJ3mCrcA95XrGv3Ij49LroK%2BA7b%2BU4y6Z4duROdcfEyxkPmr0utX5rLwVBz9ktO7rSerUkP4isxrSuGCFfV9q5UUMMV3yzYY06J0tUcm3xS7w0mfu%2BWgziZEyXioJVrltnE%2BJUpV7QbkB5rM3QG%2FD6yy4LHwpAPyskOLmuMFLXXvVZCMqU%2F02eQCJZE51uuCR8mDJs91s8A4pR%2FOv1sB7bSNrJ7PnpaZnPBbF7TL%2BvYhksBbMycdlH7ENqOcjOz1SFE9tPp4O6IvR1%2BtIoNITZbvCe4k5fiVn33fx1G%2B2yY%2BvEGqn3qJwZ9I2G5w1zkJaf75lGVMy%2Bjt18mHzHy4NYusKztDO9vEjEy%2BEdXIHXIzCc1iJE2gOmm1U5NfwbmGguB29%2Bzd7uuDYCECM96e6MOjUtlJvazhEiFKQ48vLTfGZP0uc4iQ4t7Xixafhjaop8RHj1D8QutLBKOiyjiQBp44GZnVOXm4kngdSWPihn%2FXfOrHFHgU0SalQ9QYFsafPJUFqnMtH6juW0RC%2Ff6Vx2wubA51ZoCrL5un92VOJY%2B28Khh0EK17H2rVBM3cvrWW8yj7vVXseeth92wlflCWiBUX%2BEhLkPKt8N300DjPhoHxvNIwzBwxlrWcpRAq6hHaSOMOef5rwGOqUBiu7uVl6CFOnne1I6rtM0XZPbqQudcdYd8dMz9JkIeqccVCSWmrEPU3GYffvkf4L52bhYG1Q4BRQ8ysK3LqyBIaAtGQgdqkoiZxICrz9Qf87WEKZwj1pvuJhMcJkQKarQs4Y9rJYPs%2BH8FLvhuAs5ol79i8XeBhdWDP5uMyzSpFm5Z3HhmD9o0IQexTPM9nQ9JdoQrhx%2FbkrOvdv8KV%2FaAoov%2FTFk&X-Amz-Signature=df2d4c3fad6ba5c79527662c0ab85a9e022f07855531c1e0f469d206d7cbc03d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VNSCZGK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIESZTbRuS391BSzycFp6meVYg3TquZe8pOemPRG78HkpAiEA0J6Rq4YFh6tcTwQlLjLFPyVXC%2FBoscm4BsV5gQ1U1P8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGca0WxuD6z00VJ3mCrcA95XrGv3Ij49LroK%2BA7b%2BU4y6Z4duROdcfEyxkPmr0utX5rLwVBz9ktO7rSerUkP4isxrSuGCFfV9q5UUMMV3yzYY06J0tUcm3xS7w0mfu%2BWgziZEyXioJVrltnE%2BJUpV7QbkB5rM3QG%2FD6yy4LHwpAPyskOLmuMFLXXvVZCMqU%2F02eQCJZE51uuCR8mDJs91s8A4pR%2FOv1sB7bSNrJ7PnpaZnPBbF7TL%2BvYhksBbMycdlH7ENqOcjOz1SFE9tPp4O6IvR1%2BtIoNITZbvCe4k5fiVn33fx1G%2B2yY%2BvEGqn3qJwZ9I2G5w1zkJaf75lGVMy%2Bjt18mHzHy4NYusKztDO9vEjEy%2BEdXIHXIzCc1iJE2gOmm1U5NfwbmGguB29%2Bzd7uuDYCECM96e6MOjUtlJvazhEiFKQ48vLTfGZP0uc4iQ4t7Xixafhjaop8RHj1D8QutLBKOiyjiQBp44GZnVOXm4kngdSWPihn%2FXfOrHFHgU0SalQ9QYFsafPJUFqnMtH6juW0RC%2Ff6Vx2wubA51ZoCrL5un92VOJY%2B28Khh0EK17H2rVBM3cvrWW8yj7vVXseeth92wlflCWiBUX%2BEhLkPKt8N300DjPhoHxvNIwzBwxlrWcpRAq6hHaSOMOef5rwGOqUBiu7uVl6CFOnne1I6rtM0XZPbqQudcdYd8dMz9JkIeqccVCSWmrEPU3GYffvkf4L52bhYG1Q4BRQ8ysK3LqyBIaAtGQgdqkoiZxICrz9Qf87WEKZwj1pvuJhMcJkQKarQs4Y9rJYPs%2BH8FLvhuAs5ol79i8XeBhdWDP5uMyzSpFm5Z3HhmD9o0IQexTPM9nQ9JdoQrhx%2FbkrOvdv8KV%2FaAoov%2FTFk&X-Amz-Signature=927f2f460619742f854888b9f9b59d81183233150edaec583a52811b4258940f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VNSCZGK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIESZTbRuS391BSzycFp6meVYg3TquZe8pOemPRG78HkpAiEA0J6Rq4YFh6tcTwQlLjLFPyVXC%2FBoscm4BsV5gQ1U1P8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGca0WxuD6z00VJ3mCrcA95XrGv3Ij49LroK%2BA7b%2BU4y6Z4duROdcfEyxkPmr0utX5rLwVBz9ktO7rSerUkP4isxrSuGCFfV9q5UUMMV3yzYY06J0tUcm3xS7w0mfu%2BWgziZEyXioJVrltnE%2BJUpV7QbkB5rM3QG%2FD6yy4LHwpAPyskOLmuMFLXXvVZCMqU%2F02eQCJZE51uuCR8mDJs91s8A4pR%2FOv1sB7bSNrJ7PnpaZnPBbF7TL%2BvYhksBbMycdlH7ENqOcjOz1SFE9tPp4O6IvR1%2BtIoNITZbvCe4k5fiVn33fx1G%2B2yY%2BvEGqn3qJwZ9I2G5w1zkJaf75lGVMy%2Bjt18mHzHy4NYusKztDO9vEjEy%2BEdXIHXIzCc1iJE2gOmm1U5NfwbmGguB29%2Bzd7uuDYCECM96e6MOjUtlJvazhEiFKQ48vLTfGZP0uc4iQ4t7Xixafhjaop8RHj1D8QutLBKOiyjiQBp44GZnVOXm4kngdSWPihn%2FXfOrHFHgU0SalQ9QYFsafPJUFqnMtH6juW0RC%2Ff6Vx2wubA51ZoCrL5un92VOJY%2B28Khh0EK17H2rVBM3cvrWW8yj7vVXseeth92wlflCWiBUX%2BEhLkPKt8N300DjPhoHxvNIwzBwxlrWcpRAq6hHaSOMOef5rwGOqUBiu7uVl6CFOnne1I6rtM0XZPbqQudcdYd8dMz9JkIeqccVCSWmrEPU3GYffvkf4L52bhYG1Q4BRQ8ysK3LqyBIaAtGQgdqkoiZxICrz9Qf87WEKZwj1pvuJhMcJkQKarQs4Y9rJYPs%2BH8FLvhuAs5ol79i8XeBhdWDP5uMyzSpFm5Z3HhmD9o0IQexTPM9nQ9JdoQrhx%2FbkrOvdv8KV%2FaAoov%2FTFk&X-Amz-Signature=a34b8a222f0776874ae7d34adb3464b2a1bdf327dc0aa0c2211a28f0bae572e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VNSCZGK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIESZTbRuS391BSzycFp6meVYg3TquZe8pOemPRG78HkpAiEA0J6Rq4YFh6tcTwQlLjLFPyVXC%2FBoscm4BsV5gQ1U1P8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGca0WxuD6z00VJ3mCrcA95XrGv3Ij49LroK%2BA7b%2BU4y6Z4duROdcfEyxkPmr0utX5rLwVBz9ktO7rSerUkP4isxrSuGCFfV9q5UUMMV3yzYY06J0tUcm3xS7w0mfu%2BWgziZEyXioJVrltnE%2BJUpV7QbkB5rM3QG%2FD6yy4LHwpAPyskOLmuMFLXXvVZCMqU%2F02eQCJZE51uuCR8mDJs91s8A4pR%2FOv1sB7bSNrJ7PnpaZnPBbF7TL%2BvYhksBbMycdlH7ENqOcjOz1SFE9tPp4O6IvR1%2BtIoNITZbvCe4k5fiVn33fx1G%2B2yY%2BvEGqn3qJwZ9I2G5w1zkJaf75lGVMy%2Bjt18mHzHy4NYusKztDO9vEjEy%2BEdXIHXIzCc1iJE2gOmm1U5NfwbmGguB29%2Bzd7uuDYCECM96e6MOjUtlJvazhEiFKQ48vLTfGZP0uc4iQ4t7Xixafhjaop8RHj1D8QutLBKOiyjiQBp44GZnVOXm4kngdSWPihn%2FXfOrHFHgU0SalQ9QYFsafPJUFqnMtH6juW0RC%2Ff6Vx2wubA51ZoCrL5un92VOJY%2B28Khh0EK17H2rVBM3cvrWW8yj7vVXseeth92wlflCWiBUX%2BEhLkPKt8N300DjPhoHxvNIwzBwxlrWcpRAq6hHaSOMOef5rwGOqUBiu7uVl6CFOnne1I6rtM0XZPbqQudcdYd8dMz9JkIeqccVCSWmrEPU3GYffvkf4L52bhYG1Q4BRQ8ysK3LqyBIaAtGQgdqkoiZxICrz9Qf87WEKZwj1pvuJhMcJkQKarQs4Y9rJYPs%2BH8FLvhuAs5ol79i8XeBhdWDP5uMyzSpFm5Z3HhmD9o0IQexTPM9nQ9JdoQrhx%2FbkrOvdv8KV%2FaAoov%2FTFk&X-Amz-Signature=17f97f68148f1a2361bce310359b1bda3ee14a136b5d30f789c6e9035929882b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VNSCZGK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIESZTbRuS391BSzycFp6meVYg3TquZe8pOemPRG78HkpAiEA0J6Rq4YFh6tcTwQlLjLFPyVXC%2FBoscm4BsV5gQ1U1P8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGca0WxuD6z00VJ3mCrcA95XrGv3Ij49LroK%2BA7b%2BU4y6Z4duROdcfEyxkPmr0utX5rLwVBz9ktO7rSerUkP4isxrSuGCFfV9q5UUMMV3yzYY06J0tUcm3xS7w0mfu%2BWgziZEyXioJVrltnE%2BJUpV7QbkB5rM3QG%2FD6yy4LHwpAPyskOLmuMFLXXvVZCMqU%2F02eQCJZE51uuCR8mDJs91s8A4pR%2FOv1sB7bSNrJ7PnpaZnPBbF7TL%2BvYhksBbMycdlH7ENqOcjOz1SFE9tPp4O6IvR1%2BtIoNITZbvCe4k5fiVn33fx1G%2B2yY%2BvEGqn3qJwZ9I2G5w1zkJaf75lGVMy%2Bjt18mHzHy4NYusKztDO9vEjEy%2BEdXIHXIzCc1iJE2gOmm1U5NfwbmGguB29%2Bzd7uuDYCECM96e6MOjUtlJvazhEiFKQ48vLTfGZP0uc4iQ4t7Xixafhjaop8RHj1D8QutLBKOiyjiQBp44GZnVOXm4kngdSWPihn%2FXfOrHFHgU0SalQ9QYFsafPJUFqnMtH6juW0RC%2Ff6Vx2wubA51ZoCrL5un92VOJY%2B28Khh0EK17H2rVBM3cvrWW8yj7vVXseeth92wlflCWiBUX%2BEhLkPKt8N300DjPhoHxvNIwzBwxlrWcpRAq6hHaSOMOef5rwGOqUBiu7uVl6CFOnne1I6rtM0XZPbqQudcdYd8dMz9JkIeqccVCSWmrEPU3GYffvkf4L52bhYG1Q4BRQ8ysK3LqyBIaAtGQgdqkoiZxICrz9Qf87WEKZwj1pvuJhMcJkQKarQs4Y9rJYPs%2BH8FLvhuAs5ol79i8XeBhdWDP5uMyzSpFm5Z3HhmD9o0IQexTPM9nQ9JdoQrhx%2FbkrOvdv8KV%2FaAoov%2FTFk&X-Amz-Signature=ff47f684d8103e35ad1002892947ab20af5df1bf2a7da26691eda16f00789077&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VNSCZGK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIESZTbRuS391BSzycFp6meVYg3TquZe8pOemPRG78HkpAiEA0J6Rq4YFh6tcTwQlLjLFPyVXC%2FBoscm4BsV5gQ1U1P8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGca0WxuD6z00VJ3mCrcA95XrGv3Ij49LroK%2BA7b%2BU4y6Z4duROdcfEyxkPmr0utX5rLwVBz9ktO7rSerUkP4isxrSuGCFfV9q5UUMMV3yzYY06J0tUcm3xS7w0mfu%2BWgziZEyXioJVrltnE%2BJUpV7QbkB5rM3QG%2FD6yy4LHwpAPyskOLmuMFLXXvVZCMqU%2F02eQCJZE51uuCR8mDJs91s8A4pR%2FOv1sB7bSNrJ7PnpaZnPBbF7TL%2BvYhksBbMycdlH7ENqOcjOz1SFE9tPp4O6IvR1%2BtIoNITZbvCe4k5fiVn33fx1G%2B2yY%2BvEGqn3qJwZ9I2G5w1zkJaf75lGVMy%2Bjt18mHzHy4NYusKztDO9vEjEy%2BEdXIHXIzCc1iJE2gOmm1U5NfwbmGguB29%2Bzd7uuDYCECM96e6MOjUtlJvazhEiFKQ48vLTfGZP0uc4iQ4t7Xixafhjaop8RHj1D8QutLBKOiyjiQBp44GZnVOXm4kngdSWPihn%2FXfOrHFHgU0SalQ9QYFsafPJUFqnMtH6juW0RC%2Ff6Vx2wubA51ZoCrL5un92VOJY%2B28Khh0EK17H2rVBM3cvrWW8yj7vVXseeth92wlflCWiBUX%2BEhLkPKt8N300DjPhoHxvNIwzBwxlrWcpRAq6hHaSOMOef5rwGOqUBiu7uVl6CFOnne1I6rtM0XZPbqQudcdYd8dMz9JkIeqccVCSWmrEPU3GYffvkf4L52bhYG1Q4BRQ8ysK3LqyBIaAtGQgdqkoiZxICrz9Qf87WEKZwj1pvuJhMcJkQKarQs4Y9rJYPs%2BH8FLvhuAs5ol79i8XeBhdWDP5uMyzSpFm5Z3HhmD9o0IQexTPM9nQ9JdoQrhx%2FbkrOvdv8KV%2FaAoov%2FTFk&X-Amz-Signature=db991d8631146097bc93f3640c9271ad2604fa5d6cfc200b932fe9559f4f09c2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VNSCZGK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIESZTbRuS391BSzycFp6meVYg3TquZe8pOemPRG78HkpAiEA0J6Rq4YFh6tcTwQlLjLFPyVXC%2FBoscm4BsV5gQ1U1P8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGca0WxuD6z00VJ3mCrcA95XrGv3Ij49LroK%2BA7b%2BU4y6Z4duROdcfEyxkPmr0utX5rLwVBz9ktO7rSerUkP4isxrSuGCFfV9q5UUMMV3yzYY06J0tUcm3xS7w0mfu%2BWgziZEyXioJVrltnE%2BJUpV7QbkB5rM3QG%2FD6yy4LHwpAPyskOLmuMFLXXvVZCMqU%2F02eQCJZE51uuCR8mDJs91s8A4pR%2FOv1sB7bSNrJ7PnpaZnPBbF7TL%2BvYhksBbMycdlH7ENqOcjOz1SFE9tPp4O6IvR1%2BtIoNITZbvCe4k5fiVn33fx1G%2B2yY%2BvEGqn3qJwZ9I2G5w1zkJaf75lGVMy%2Bjt18mHzHy4NYusKztDO9vEjEy%2BEdXIHXIzCc1iJE2gOmm1U5NfwbmGguB29%2Bzd7uuDYCECM96e6MOjUtlJvazhEiFKQ48vLTfGZP0uc4iQ4t7Xixafhjaop8RHj1D8QutLBKOiyjiQBp44GZnVOXm4kngdSWPihn%2FXfOrHFHgU0SalQ9QYFsafPJUFqnMtH6juW0RC%2Ff6Vx2wubA51ZoCrL5un92VOJY%2B28Khh0EK17H2rVBM3cvrWW8yj7vVXseeth92wlflCWiBUX%2BEhLkPKt8N300DjPhoHxvNIwzBwxlrWcpRAq6hHaSOMOef5rwGOqUBiu7uVl6CFOnne1I6rtM0XZPbqQudcdYd8dMz9JkIeqccVCSWmrEPU3GYffvkf4L52bhYG1Q4BRQ8ysK3LqyBIaAtGQgdqkoiZxICrz9Qf87WEKZwj1pvuJhMcJkQKarQs4Y9rJYPs%2BH8FLvhuAs5ol79i8XeBhdWDP5uMyzSpFm5Z3HhmD9o0IQexTPM9nQ9JdoQrhx%2FbkrOvdv8KV%2FaAoov%2FTFk&X-Amz-Signature=c2ebe49b336963e5200e99460e6f41f21d9c4777eec4456bbad9f68378e3eb2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOJE3YSI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCp5c2DJaoYU5L2z8LHulFqhaQTldNzKmpBBfjD3ENytAIgTEBPT3%2BvOjCA4gXMndEhHku7JN5BAeV0P4c4UPxUHO8qiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNjnBPdz%2BZAaXAIB9CrcAwtHICLNuv%2B8jv%2F7hzKcd9c7I78T3sIvme53M8mJRaYO%2FyxcZrqZd72AU5tPowHS0iziczgR0X4GM%2B9Qv0VQoltEwVAQ8wVamfw2mbx8Dhgcdoce9tgUppV7YofLdr1zK025jlS05TS%2FSwjRCJ5gjhtrrzYwuSApM2prCydDFAzpoRjqj3%2F2GMqQ7w7x8Bu5XrO6r7fSws%2BmTZ5MXeafNyLaptpG7vXAj4N9hapOV%2FWB8O1lhx9lWDBRXwZTU1Rn2IbANxNX9ryq2IKiPyob2GTnvVN2lqXC%2BthgSW5qKOYibipkqtBqo%2BHCjkmubFFOxHtg7zLGqC48%2BxUan2m8i4eqvev1x8FWRbC09OV3y7EouNqjVIIJZXSDvEm80JyNfx2itHGmXLaVq3QxjJ8pivuTVhXb4MmKfBLK1ohxPu%2BolL%2Fxo6LiobSXhDDXNzkNjqsHaKfHyyEBzeI3pKEWWjc%2FILxeDoYLLUhan9lpCCvLw11kzwTzpxi%2FBvR7Y4PeSqn4qiUNvI6OCzHKnCdDUFqKb4hAnVc4s4xV4SWKWQmquaUBrDR1a2WGvxtb%2BrtQevMMy83aHXzaiKbdmMXSOkeoJZJIrdwuyFQGxU87TymIM%2BWqXvguss7VHj3BMPif5rwGOqUBu7EywoH3k7wzhP2cNmOrTCHfxLBlE43Vuxsv6I51eNrFs%2BzqevKn%2B8c4i2QQ8wHlJzcd3QKuMB2vqaChKfwT0ugTZAq3jSJ%2BKvVyfKiaNNGBzdYm%2BPn3%2BkrdYXN3KrnSGxPJa1x%2Bb7LIIM82oTcPyIjZY%2Fv6wh0apB0%2BCiba7uxaerJOtspMxAgCDiVaA4544BRzs%2BG1l%2Fz0XlnFbVaPg4eU4CU3&X-Amz-Signature=61c7acff99cdf40ab283efd6d4d6f7e45e29f231f9b53579c94028e536018e87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZY3LFNQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIE%2FS02BUxdl%2FwM3w1CdggeBuUWS7O1YTnM8PlwR%2BcHw3AiAAstesqjN5PTKx0ZIuynbxvyy7uwfexllcG2tWtiIl1yqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy5nKN4nc2i0Pc6sfKtwDqzaLYwbo96DUi3fPlzDeLV1TsIfhQVf3uNBpx45EWZ7JVr%2Fan%2BJFtDl4nZn%2FdIFg%2BKlQ9qRoNX8OKm5bxIWDXgDdasNemyfL6l5yCWl%2BdE2FDmx1vqy49b%2BYmzUbRyMLFwPfOrwPyLiKo%2FdS%2F9MhTZAgjTt8CLXwxAWv2i45Xnj1zFoFwE%2BQ0nhsDBQg3VPQmS%2BC0rotDiuJJWI8FkP0sIRwavAGvtPbwUWAS1lQ%2BwplunNkj5aLflwgv41eQBqWXHbwOwOfBlNfucfruc3Z9EM4U0qmkRu0pG4ROKuEJXw0e8%2F76T6gxagmlLOglbUedHU8IUVOpm5UatCmGcAkECLdGDV4jUqcL4NVI7h9m7GDrSRDzlUKXe4gj%2FBOef1dERxP6WoweYfNKAtZVz9LArJupPaaYM497KkFRSEJh6Bc7RSF%2FCUlY%2BtH7h%2BMKcUHZLaGannQbM4p1NOqWEbX%2Fphy02hc%2BNF7EeWEIyED3BZRAJuDYTareFmW%2FSWtFRNu4LqwodHbVbgAoEWEgDJPbT7H09JxfbihK%2BqVj2Y%2FPmy4b1bk6lfFQ0GyYMbYBzQIO8DCI%2BFGrDzhC1d9BzoXLCrM9DJVHIfKORm2S4iTjtgYhVoBJQXZCy1GZNswtp%2FmvAY6pgFsiZfYG1FME5ThSwvn9YYkYxOb4MS8RAz%2FXZ7FszJL8J0bWYfPfvmxuesAY%2FX7Sjug9j%2F4XnxIsE8p9E1kMDHOs%2FeABU5uPj1ZoOH8Tla1VioeL0uUyXrchXFXMPq%2FNZEaqVKdkFy8rZwzoSSK19RL6EUc9DnyWkegPcTUaGP6uPVGH9kJByRq6QiYvgp655MU3vV6%2Bf7HhfILYV%2Fpkl%2FHY4ONYq5W&X-Amz-Signature=428cfb2e4808b61283b3010697d5ce3943d4ade04f92fca4ff959f8eec021260&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWHJBHZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICOf5ITBHXPMAKVVfRgSa%2F6Eb2q6fV4goEKDZZ3es%2FZxAiBY59hYeDqaKE3H8z%2FYcXigDTJHU4rHWisC0RM64Hr7PyqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Fy7okl739byATXwhKtwDpfnn9ZOttT7m905HeaXSnXRp8RZ4YNDBhVnCpoAI3SPhItygGtq0hcwr%2Fore%2Bn6wsk7cVgaDjrh4f6gnSpCrRHsw7b7LRmVJdU375cgU505rRcvSItkyhALipNXSNTtc%2FetrFO2mquPBf74xvvkJgxSCUcf%2BZ93N3Icyf3IzpfoQfqe2LINPJAFH4ZnVFRfRWCqAtRH5ttW5ax%2FcTmcwSL%2BO2NO1rbcxTDJo%2BVmzYSaXzsxTQyOxNn%2FIyw2PqDnqQp9HOOFZw0ylIjRM8bJ4dKt3l1QS1h4Fg0ILWqAxseSezJewhTjenSpNC2Y3IpQxvK%2F53fKHr6umW4cxRB%2BS4M4nc69KdyyyWSqsIZ9FG1lKvTAvwBia8kEH2SZd6W7io5Wjj9vB0Kdt9UeM8w18yA8wzEjXg1fV0TZWE578P7nOAfZK3KyHNbepqkeHogekdwJxrsepsF7q9C2Z4zkQiMK5iZF7x6RkL0fXlf9M9PryJK%2F%2FcgugcPMNLx5MCtO%2BNiT46HPE9QPlhdrmQwpTUKWqKF95yCrslHDcjjL5G0c%2FcLhze9wfD0%2BVBL2Mcn0uCaXj%2Fxm0EgqsUFYOLQMbQ12lFkpKpr7UWLFv2DO17nXHe9XlxIBzy%2BF8%2F2UwiaDmvAY6pgGsQzUc6y%2BawWv2ou02mwL%2FyxBPjko49UVVLIdP3gbhahB%2FbqgRhYWSxnUBCx0CYsaMvcU5kQXow8fai5xIBFb1UsH4ffxMw8FAoHFQzwWc1LfC0bnb5qTJulUDNtQ1rc3dRaUUQCP%2Bz7sB6sFIiQK%2BAdOcEcX8YjvE%2FfdtNCpmowoiztUUbVF3n9hCbcccqUpaxj2IDdcCvINKoZ%2BZnoBqUvFWd47m&X-Amz-Signature=13d2d64425d618eabc578f50a214c7a50228b26108dbfcf4850345f9b4b08fd2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDWHJBHZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICOf5ITBHXPMAKVVfRgSa%2F6Eb2q6fV4goEKDZZ3es%2FZxAiBY59hYeDqaKE3H8z%2FYcXigDTJHU4rHWisC0RM64Hr7PyqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Fy7okl739byATXwhKtwDpfnn9ZOttT7m905HeaXSnXRp8RZ4YNDBhVnCpoAI3SPhItygGtq0hcwr%2Fore%2Bn6wsk7cVgaDjrh4f6gnSpCrRHsw7b7LRmVJdU375cgU505rRcvSItkyhALipNXSNTtc%2FetrFO2mquPBf74xvvkJgxSCUcf%2BZ93N3Icyf3IzpfoQfqe2LINPJAFH4ZnVFRfRWCqAtRH5ttW5ax%2FcTmcwSL%2BO2NO1rbcxTDJo%2BVmzYSaXzsxTQyOxNn%2FIyw2PqDnqQp9HOOFZw0ylIjRM8bJ4dKt3l1QS1h4Fg0ILWqAxseSezJewhTjenSpNC2Y3IpQxvK%2F53fKHr6umW4cxRB%2BS4M4nc69KdyyyWSqsIZ9FG1lKvTAvwBia8kEH2SZd6W7io5Wjj9vB0Kdt9UeM8w18yA8wzEjXg1fV0TZWE578P7nOAfZK3KyHNbepqkeHogekdwJxrsepsF7q9C2Z4zkQiMK5iZF7x6RkL0fXlf9M9PryJK%2F%2FcgugcPMNLx5MCtO%2BNiT46HPE9QPlhdrmQwpTUKWqKF95yCrslHDcjjL5G0c%2FcLhze9wfD0%2BVBL2Mcn0uCaXj%2Fxm0EgqsUFYOLQMbQ12lFkpKpr7UWLFv2DO17nXHe9XlxIBzy%2BF8%2F2UwiaDmvAY6pgGsQzUc6y%2BawWv2ou02mwL%2FyxBPjko49UVVLIdP3gbhahB%2FbqgRhYWSxnUBCx0CYsaMvcU5kQXow8fai5xIBFb1UsH4ffxMw8FAoHFQzwWc1LfC0bnb5qTJulUDNtQ1rc3dRaUUQCP%2Bz7sB6sFIiQK%2BAdOcEcX8YjvE%2FfdtNCpmowoiztUUbVF3n9hCbcccqUpaxj2IDdcCvINKoZ%2BZnoBqUvFWd47m&X-Amz-Signature=66fae65c44acbd72882ca8bd7037bc605978e56e1978c27f1a367e695aadb04a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
