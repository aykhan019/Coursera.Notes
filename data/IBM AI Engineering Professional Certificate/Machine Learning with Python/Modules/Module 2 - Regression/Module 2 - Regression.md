

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WOD3AYZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDgMPf1n1luZXdKc0hLwx0cyxKn0PBAQTeZUcO9awcu4AIgAgpNcpS5tQPAHe85Tp2Ss2lnSbu1Su%2B%2Fw70daTrjq10q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOwwLsx9vE%2BRe8uHzircAzqT%2FmEjB3jnTvhrQ13cb9t%2Flrr03tGLJ4HIAjBGUR2nBapP%2FEDrM03VphsTjGSR2usM1bRgxqgalerQLlGHYTwzMtuK4naMJx4IpyCET24RP%2FMHESMxWUSawsepWVNCoYoMCDEKjAOv2mzV%2FZy2%2BCeH7m6%2BdUGMUzy1tl9drEY2Bwxs%2BjpyZ6GT6QrYi0wgkv3MyjI7QTApZnWUgcGPVNrdUEA5GT8ChGT5KT1Z7iMvaIcC9Kh5Gd0HiqMQYfKIUehk6%2BZWLDNEMPbwWle00iwECJv2LJrCjmi8iVL2%2BMVGVCBs6NKOWqAbuQFRkEVLnSDcFvEnqv%2BuzUBAXJnmNtlQGh55uiImBkzPMs8uH7Cckqv6DVjGjGXlY8RZQUjXSiVtlzWKxA8kcaKeat42Oa5c4YLxQ9XFJn%2FWfQUALT9lg3Q69HKh32eHs0ESh7ImESl5TNlUzNhlJ2NpFRTno1ZqSkZ9R4%2F6OuimNgZDVPgkzt3Oobekby0rW%2FSL0m0wVYwXfdSNhjTqbeFOy7rBbM03n4OWzOTYYf%2FsRbyQ06WRqEGxrTlC4oFneTD7paCuifGBfhvWep35%2BzlJ66d57q4LFkWKzOsFmltU2%2BwdVnneXR9jNU7vXpnBBGNCMPO8hL0GOqUBtEWcdehWGM9%2B04n6oqH1RXvMZxKuOM72aKNecuctQ1RVHnbYKmsroSYMRuT7n2ksdCXr6g%2B9Ny9y3fPigPQXPUWaQIdhG0%2BH2BD69k5TSSShga9DMkVcdktgqNs2UR9a%2BgXlwraI1GZVhEj5I7AMfD9WZO%2B7uU7TqO%2B1o2AP7iVDQMhaLmAE3rnBcUcsPdQSgkN%2F%2BpUrU6JMt0iVCgFfpb4H7Eaw&X-Amz-Signature=0c76b42a8270426a33f467e4dd51b79ecae9cd593ae940fe0388d620491e3b8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WOD3AYZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDgMPf1n1luZXdKc0hLwx0cyxKn0PBAQTeZUcO9awcu4AIgAgpNcpS5tQPAHe85Tp2Ss2lnSbu1Su%2B%2Fw70daTrjq10q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOwwLsx9vE%2BRe8uHzircAzqT%2FmEjB3jnTvhrQ13cb9t%2Flrr03tGLJ4HIAjBGUR2nBapP%2FEDrM03VphsTjGSR2usM1bRgxqgalerQLlGHYTwzMtuK4naMJx4IpyCET24RP%2FMHESMxWUSawsepWVNCoYoMCDEKjAOv2mzV%2FZy2%2BCeH7m6%2BdUGMUzy1tl9drEY2Bwxs%2BjpyZ6GT6QrYi0wgkv3MyjI7QTApZnWUgcGPVNrdUEA5GT8ChGT5KT1Z7iMvaIcC9Kh5Gd0HiqMQYfKIUehk6%2BZWLDNEMPbwWle00iwECJv2LJrCjmi8iVL2%2BMVGVCBs6NKOWqAbuQFRkEVLnSDcFvEnqv%2BuzUBAXJnmNtlQGh55uiImBkzPMs8uH7Cckqv6DVjGjGXlY8RZQUjXSiVtlzWKxA8kcaKeat42Oa5c4YLxQ9XFJn%2FWfQUALT9lg3Q69HKh32eHs0ESh7ImESl5TNlUzNhlJ2NpFRTno1ZqSkZ9R4%2F6OuimNgZDVPgkzt3Oobekby0rW%2FSL0m0wVYwXfdSNhjTqbeFOy7rBbM03n4OWzOTYYf%2FsRbyQ06WRqEGxrTlC4oFneTD7paCuifGBfhvWep35%2BzlJ66d57q4LFkWKzOsFmltU2%2BwdVnneXR9jNU7vXpnBBGNCMPO8hL0GOqUBtEWcdehWGM9%2B04n6oqH1RXvMZxKuOM72aKNecuctQ1RVHnbYKmsroSYMRuT7n2ksdCXr6g%2B9Ny9y3fPigPQXPUWaQIdhG0%2BH2BD69k5TSSShga9DMkVcdktgqNs2UR9a%2BgXlwraI1GZVhEj5I7AMfD9WZO%2B7uU7TqO%2B1o2AP7iVDQMhaLmAE3rnBcUcsPdQSgkN%2F%2BpUrU6JMt0iVCgFfpb4H7Eaw&X-Amz-Signature=f690e08c4a1b0ace867bc669ddc63fe77f96936d61c9ca9a66e9aac8dd48d6cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WOD3AYZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDgMPf1n1luZXdKc0hLwx0cyxKn0PBAQTeZUcO9awcu4AIgAgpNcpS5tQPAHe85Tp2Ss2lnSbu1Su%2B%2Fw70daTrjq10q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOwwLsx9vE%2BRe8uHzircAzqT%2FmEjB3jnTvhrQ13cb9t%2Flrr03tGLJ4HIAjBGUR2nBapP%2FEDrM03VphsTjGSR2usM1bRgxqgalerQLlGHYTwzMtuK4naMJx4IpyCET24RP%2FMHESMxWUSawsepWVNCoYoMCDEKjAOv2mzV%2FZy2%2BCeH7m6%2BdUGMUzy1tl9drEY2Bwxs%2BjpyZ6GT6QrYi0wgkv3MyjI7QTApZnWUgcGPVNrdUEA5GT8ChGT5KT1Z7iMvaIcC9Kh5Gd0HiqMQYfKIUehk6%2BZWLDNEMPbwWle00iwECJv2LJrCjmi8iVL2%2BMVGVCBs6NKOWqAbuQFRkEVLnSDcFvEnqv%2BuzUBAXJnmNtlQGh55uiImBkzPMs8uH7Cckqv6DVjGjGXlY8RZQUjXSiVtlzWKxA8kcaKeat42Oa5c4YLxQ9XFJn%2FWfQUALT9lg3Q69HKh32eHs0ESh7ImESl5TNlUzNhlJ2NpFRTno1ZqSkZ9R4%2F6OuimNgZDVPgkzt3Oobekby0rW%2FSL0m0wVYwXfdSNhjTqbeFOy7rBbM03n4OWzOTYYf%2FsRbyQ06WRqEGxrTlC4oFneTD7paCuifGBfhvWep35%2BzlJ66d57q4LFkWKzOsFmltU2%2BwdVnneXR9jNU7vXpnBBGNCMPO8hL0GOqUBtEWcdehWGM9%2B04n6oqH1RXvMZxKuOM72aKNecuctQ1RVHnbYKmsroSYMRuT7n2ksdCXr6g%2B9Ny9y3fPigPQXPUWaQIdhG0%2BH2BD69k5TSSShga9DMkVcdktgqNs2UR9a%2BgXlwraI1GZVhEj5I7AMfD9WZO%2B7uU7TqO%2B1o2AP7iVDQMhaLmAE3rnBcUcsPdQSgkN%2F%2BpUrU6JMt0iVCgFfpb4H7Eaw&X-Amz-Signature=c342a1dc4655ec85bb5c25b33e02260d79b6740ba97ace022064392fbb62c9c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WOD3AYZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDgMPf1n1luZXdKc0hLwx0cyxKn0PBAQTeZUcO9awcu4AIgAgpNcpS5tQPAHe85Tp2Ss2lnSbu1Su%2B%2Fw70daTrjq10q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOwwLsx9vE%2BRe8uHzircAzqT%2FmEjB3jnTvhrQ13cb9t%2Flrr03tGLJ4HIAjBGUR2nBapP%2FEDrM03VphsTjGSR2usM1bRgxqgalerQLlGHYTwzMtuK4naMJx4IpyCET24RP%2FMHESMxWUSawsepWVNCoYoMCDEKjAOv2mzV%2FZy2%2BCeH7m6%2BdUGMUzy1tl9drEY2Bwxs%2BjpyZ6GT6QrYi0wgkv3MyjI7QTApZnWUgcGPVNrdUEA5GT8ChGT5KT1Z7iMvaIcC9Kh5Gd0HiqMQYfKIUehk6%2BZWLDNEMPbwWle00iwECJv2LJrCjmi8iVL2%2BMVGVCBs6NKOWqAbuQFRkEVLnSDcFvEnqv%2BuzUBAXJnmNtlQGh55uiImBkzPMs8uH7Cckqv6DVjGjGXlY8RZQUjXSiVtlzWKxA8kcaKeat42Oa5c4YLxQ9XFJn%2FWfQUALT9lg3Q69HKh32eHs0ESh7ImESl5TNlUzNhlJ2NpFRTno1ZqSkZ9R4%2F6OuimNgZDVPgkzt3Oobekby0rW%2FSL0m0wVYwXfdSNhjTqbeFOy7rBbM03n4OWzOTYYf%2FsRbyQ06WRqEGxrTlC4oFneTD7paCuifGBfhvWep35%2BzlJ66d57q4LFkWKzOsFmltU2%2BwdVnneXR9jNU7vXpnBBGNCMPO8hL0GOqUBtEWcdehWGM9%2B04n6oqH1RXvMZxKuOM72aKNecuctQ1RVHnbYKmsroSYMRuT7n2ksdCXr6g%2B9Ny9y3fPigPQXPUWaQIdhG0%2BH2BD69k5TSSShga9DMkVcdktgqNs2UR9a%2BgXlwraI1GZVhEj5I7AMfD9WZO%2B7uU7TqO%2B1o2AP7iVDQMhaLmAE3rnBcUcsPdQSgkN%2F%2BpUrU6JMt0iVCgFfpb4H7Eaw&X-Amz-Signature=2ad9630b89ae8fbc53baf8bf570c69656cbe5a7e54135d4981619727adcab321&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WOD3AYZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDgMPf1n1luZXdKc0hLwx0cyxKn0PBAQTeZUcO9awcu4AIgAgpNcpS5tQPAHe85Tp2Ss2lnSbu1Su%2B%2Fw70daTrjq10q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOwwLsx9vE%2BRe8uHzircAzqT%2FmEjB3jnTvhrQ13cb9t%2Flrr03tGLJ4HIAjBGUR2nBapP%2FEDrM03VphsTjGSR2usM1bRgxqgalerQLlGHYTwzMtuK4naMJx4IpyCET24RP%2FMHESMxWUSawsepWVNCoYoMCDEKjAOv2mzV%2FZy2%2BCeH7m6%2BdUGMUzy1tl9drEY2Bwxs%2BjpyZ6GT6QrYi0wgkv3MyjI7QTApZnWUgcGPVNrdUEA5GT8ChGT5KT1Z7iMvaIcC9Kh5Gd0HiqMQYfKIUehk6%2BZWLDNEMPbwWle00iwECJv2LJrCjmi8iVL2%2BMVGVCBs6NKOWqAbuQFRkEVLnSDcFvEnqv%2BuzUBAXJnmNtlQGh55uiImBkzPMs8uH7Cckqv6DVjGjGXlY8RZQUjXSiVtlzWKxA8kcaKeat42Oa5c4YLxQ9XFJn%2FWfQUALT9lg3Q69HKh32eHs0ESh7ImESl5TNlUzNhlJ2NpFRTno1ZqSkZ9R4%2F6OuimNgZDVPgkzt3Oobekby0rW%2FSL0m0wVYwXfdSNhjTqbeFOy7rBbM03n4OWzOTYYf%2FsRbyQ06WRqEGxrTlC4oFneTD7paCuifGBfhvWep35%2BzlJ66d57q4LFkWKzOsFmltU2%2BwdVnneXR9jNU7vXpnBBGNCMPO8hL0GOqUBtEWcdehWGM9%2B04n6oqH1RXvMZxKuOM72aKNecuctQ1RVHnbYKmsroSYMRuT7n2ksdCXr6g%2B9Ny9y3fPigPQXPUWaQIdhG0%2BH2BD69k5TSSShga9DMkVcdktgqNs2UR9a%2BgXlwraI1GZVhEj5I7AMfD9WZO%2B7uU7TqO%2B1o2AP7iVDQMhaLmAE3rnBcUcsPdQSgkN%2F%2BpUrU6JMt0iVCgFfpb4H7Eaw&X-Amz-Signature=f321c97037979e5f7afa112af0a4ea6ea3b7f37b88c0395d6383a1fabc696131&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WOD3AYZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDgMPf1n1luZXdKc0hLwx0cyxKn0PBAQTeZUcO9awcu4AIgAgpNcpS5tQPAHe85Tp2Ss2lnSbu1Su%2B%2Fw70daTrjq10q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOwwLsx9vE%2BRe8uHzircAzqT%2FmEjB3jnTvhrQ13cb9t%2Flrr03tGLJ4HIAjBGUR2nBapP%2FEDrM03VphsTjGSR2usM1bRgxqgalerQLlGHYTwzMtuK4naMJx4IpyCET24RP%2FMHESMxWUSawsepWVNCoYoMCDEKjAOv2mzV%2FZy2%2BCeH7m6%2BdUGMUzy1tl9drEY2Bwxs%2BjpyZ6GT6QrYi0wgkv3MyjI7QTApZnWUgcGPVNrdUEA5GT8ChGT5KT1Z7iMvaIcC9Kh5Gd0HiqMQYfKIUehk6%2BZWLDNEMPbwWle00iwECJv2LJrCjmi8iVL2%2BMVGVCBs6NKOWqAbuQFRkEVLnSDcFvEnqv%2BuzUBAXJnmNtlQGh55uiImBkzPMs8uH7Cckqv6DVjGjGXlY8RZQUjXSiVtlzWKxA8kcaKeat42Oa5c4YLxQ9XFJn%2FWfQUALT9lg3Q69HKh32eHs0ESh7ImESl5TNlUzNhlJ2NpFRTno1ZqSkZ9R4%2F6OuimNgZDVPgkzt3Oobekby0rW%2FSL0m0wVYwXfdSNhjTqbeFOy7rBbM03n4OWzOTYYf%2FsRbyQ06WRqEGxrTlC4oFneTD7paCuifGBfhvWep35%2BzlJ66d57q4LFkWKzOsFmltU2%2BwdVnneXR9jNU7vXpnBBGNCMPO8hL0GOqUBtEWcdehWGM9%2B04n6oqH1RXvMZxKuOM72aKNecuctQ1RVHnbYKmsroSYMRuT7n2ksdCXr6g%2B9Ny9y3fPigPQXPUWaQIdhG0%2BH2BD69k5TSSShga9DMkVcdktgqNs2UR9a%2BgXlwraI1GZVhEj5I7AMfD9WZO%2B7uU7TqO%2B1o2AP7iVDQMhaLmAE3rnBcUcsPdQSgkN%2F%2BpUrU6JMt0iVCgFfpb4H7Eaw&X-Amz-Signature=5e4289ed16a0213e1dfbb12664523e81326bbc0abf4a83ffc5d66a3268707980&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WOD3AYZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDgMPf1n1luZXdKc0hLwx0cyxKn0PBAQTeZUcO9awcu4AIgAgpNcpS5tQPAHe85Tp2Ss2lnSbu1Su%2B%2Fw70daTrjq10q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOwwLsx9vE%2BRe8uHzircAzqT%2FmEjB3jnTvhrQ13cb9t%2Flrr03tGLJ4HIAjBGUR2nBapP%2FEDrM03VphsTjGSR2usM1bRgxqgalerQLlGHYTwzMtuK4naMJx4IpyCET24RP%2FMHESMxWUSawsepWVNCoYoMCDEKjAOv2mzV%2FZy2%2BCeH7m6%2BdUGMUzy1tl9drEY2Bwxs%2BjpyZ6GT6QrYi0wgkv3MyjI7QTApZnWUgcGPVNrdUEA5GT8ChGT5KT1Z7iMvaIcC9Kh5Gd0HiqMQYfKIUehk6%2BZWLDNEMPbwWle00iwECJv2LJrCjmi8iVL2%2BMVGVCBs6NKOWqAbuQFRkEVLnSDcFvEnqv%2BuzUBAXJnmNtlQGh55uiImBkzPMs8uH7Cckqv6DVjGjGXlY8RZQUjXSiVtlzWKxA8kcaKeat42Oa5c4YLxQ9XFJn%2FWfQUALT9lg3Q69HKh32eHs0ESh7ImESl5TNlUzNhlJ2NpFRTno1ZqSkZ9R4%2F6OuimNgZDVPgkzt3Oobekby0rW%2FSL0m0wVYwXfdSNhjTqbeFOy7rBbM03n4OWzOTYYf%2FsRbyQ06WRqEGxrTlC4oFneTD7paCuifGBfhvWep35%2BzlJ66d57q4LFkWKzOsFmltU2%2BwdVnneXR9jNU7vXpnBBGNCMPO8hL0GOqUBtEWcdehWGM9%2B04n6oqH1RXvMZxKuOM72aKNecuctQ1RVHnbYKmsroSYMRuT7n2ksdCXr6g%2B9Ny9y3fPigPQXPUWaQIdhG0%2BH2BD69k5TSSShga9DMkVcdktgqNs2UR9a%2BgXlwraI1GZVhEj5I7AMfD9WZO%2B7uU7TqO%2B1o2AP7iVDQMhaLmAE3rnBcUcsPdQSgkN%2F%2BpUrU6JMt0iVCgFfpb4H7Eaw&X-Amz-Signature=817f84b7e13f253c3f3d093bd558e45f4b9a25cb392f3bc8ce9379157aa7bc33&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WOD3AYZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDgMPf1n1luZXdKc0hLwx0cyxKn0PBAQTeZUcO9awcu4AIgAgpNcpS5tQPAHe85Tp2Ss2lnSbu1Su%2B%2Fw70daTrjq10q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOwwLsx9vE%2BRe8uHzircAzqT%2FmEjB3jnTvhrQ13cb9t%2Flrr03tGLJ4HIAjBGUR2nBapP%2FEDrM03VphsTjGSR2usM1bRgxqgalerQLlGHYTwzMtuK4naMJx4IpyCET24RP%2FMHESMxWUSawsepWVNCoYoMCDEKjAOv2mzV%2FZy2%2BCeH7m6%2BdUGMUzy1tl9drEY2Bwxs%2BjpyZ6GT6QrYi0wgkv3MyjI7QTApZnWUgcGPVNrdUEA5GT8ChGT5KT1Z7iMvaIcC9Kh5Gd0HiqMQYfKIUehk6%2BZWLDNEMPbwWle00iwECJv2LJrCjmi8iVL2%2BMVGVCBs6NKOWqAbuQFRkEVLnSDcFvEnqv%2BuzUBAXJnmNtlQGh55uiImBkzPMs8uH7Cckqv6DVjGjGXlY8RZQUjXSiVtlzWKxA8kcaKeat42Oa5c4YLxQ9XFJn%2FWfQUALT9lg3Q69HKh32eHs0ESh7ImESl5TNlUzNhlJ2NpFRTno1ZqSkZ9R4%2F6OuimNgZDVPgkzt3Oobekby0rW%2FSL0m0wVYwXfdSNhjTqbeFOy7rBbM03n4OWzOTYYf%2FsRbyQ06WRqEGxrTlC4oFneTD7paCuifGBfhvWep35%2BzlJ66d57q4LFkWKzOsFmltU2%2BwdVnneXR9jNU7vXpnBBGNCMPO8hL0GOqUBtEWcdehWGM9%2B04n6oqH1RXvMZxKuOM72aKNecuctQ1RVHnbYKmsroSYMRuT7n2ksdCXr6g%2B9Ny9y3fPigPQXPUWaQIdhG0%2BH2BD69k5TSSShga9DMkVcdktgqNs2UR9a%2BgXlwraI1GZVhEj5I7AMfD9WZO%2B7uU7TqO%2B1o2AP7iVDQMhaLmAE3rnBcUcsPdQSgkN%2F%2BpUrU6JMt0iVCgFfpb4H7Eaw&X-Amz-Signature=81ff428f962e6fd7cb23c468d6c572d414210708ffbfa1145712c60015968d6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUHCKU3R%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQClZuAJQceUfL46XH6ftHdEHHdVCsr52FXGzIrv5Os8VAIhAO51dJLrZ3W5GsqhjhuzhrL6Fq%2F31AQpsOKKTazmNc6vKv8DCB0QABoMNjM3NDIzMTgzODA1IgxwNm1uJ1ekqIgKsewq3AO5Bg8QWpfzeXmR0MpDTUFqOnY3YBR0z8VGXFHVL2nytToMtqVeRDsqZkfK9XAkkwpjgn%2BevphAZyOVwh8Y6xLCypbS%2F6AHTuTyy87ma6KDi4LGc5Rnk%2FYtPFVpd2n4sowWjmhtCKOm9HIXLkmc4mlPA4CCpWyzI5DDIeE09BlPz9E2ww9Iu2OQq0HA8750usOkx8FKuStvSII1fhNjRvek7oE%2FXLIBBE86XD4j7qj9NlhYiHUsdhnBnNMc7Ps1TyyhzVeaQhgtC3gc4rYOvxO8jWWEbF%2F8meOc6kwzMm6KQUe4dlz7LwUUE%2FdeEQH93%2FCwjXaIkJhQde9rccdJN2bxJPuCoEoDd0fgCnM5VLXWI9WlB6FYNLMeNAr41Em4QqN0zLjg6IvEenUv4JKG4JvtYDBoevze2A%2FyAy4OStvbpncuK2LL9xTN34rbf76w%2FtPyKk6aLf%2FpUfB4%2B46BSxDh%2BR8doxIQgDfZIZvNCVZV5HKnSokeDMplRfqHpS7h9EQqnZ1iG4YMVF0l8hnRVadOOvITLzLtqgPK0nTuSklPW6UpE%2B71R83%2B%2BrQNE0teVFdYOTti84Xxx7VpNkYRZFNTn8GCH%2F9h0NX%2FKqYF6t6Rjy48Gs2GJT1UIgm8aDDVvIS9BjqkAc5sYphh4%2FYDsbU2LGJRZ69ZEWR2frPvwcb9YFcO1sGDnEhbdzo8rdfu7L4bh8IfM%2Bh5oaCMyRBGW%2FuDc5s%2F6JNqxx%2B4ZNdIGGNm8paJa0fPZMoz8vUJoPl0GbbzHXK6WsDNI3IYn1EWoFGD3KEtCesYwWAt1qzWo0nnGbs%2BvSD9imCoR2goUNPo481rEmG7W9K6LsjpZnrKeJERzlLBzslY68xX&X-Amz-Signature=15ea5bbe6ec347b9d173edb8b88a0bea667c4ec00d9c9f1a471d22ade91e3274&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUJNVJCJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDEbTZx7oAAOOHo17UeSOxz%2B3%2BCnzvJ7ZLizp1SiYt7ggIhAObqc1fiPSZx1XYKjBGfY3aOflhVcdyX%2FQockTLnCRrCKv8DCB0QABoMNjM3NDIzMTgzODA1Igxw2vMYEmcFuAgYjKgq3ANGglOzzbOgdvzBTtEdysS6CIt3FH2kYDvA1BCfT33Lv0pb3h7r2Xo2EKmAGX84nk%2BOSWmoQ5g1rQVrASO%2FBfTqPvTOY%2Bl%2Bag%2FFoX59lG%2BpXnyV04a5NKeafwgEdXgLNsjvqSakhmwvjmmbddfVhh%2FDi%2B1Tbx6%2BeJf1D14txiy3iCIwIVYxfiiVOxTp07gTUTO3FgYfRvNyQIJk7WWERSgSQXj99%2F7HQsq%2BZ1QDJ0mircVUdO2Sj9XwQViF1slpIwQDqpRlS9V3CVsfOY%2BURod6yezFLTit8sMAahudHFEyJu21E8ZRbfAdatsiGqByAvBU2YFJ07A8Z7d3lxXX5OlOYtweY%2B8txkzjju5aytrSeHz%2BW10EeYhrJNokpOY1HMJdrYGIJfWxcCA1UY%2F%2Fe3qdY7DVBL1NbzCmastgYnxvqT0ZOETqomqapjCkrCyyZuFa8GYQS6DYjtzA7thffEjQjbSL2BsGk29hXKbc54Ah56FSNJWLWEMQ%2BzDbvTxYJiUecPV3vt7XyBqCY9SfyEZivAjonH5C81MqGzeERuMXsvAdMTcXU55NctFK7VbW0gLNXNPqerPS3K%2BzVcO%2B5bq0ufiIsCrSekmc9SjDv2oMLZPBNqsXZjRD31DU4jDrvYS9BjqkAV4AoiQ2Y458FRzQeAM8LGirJRCeS2yxi4O5DON2E6732RYXvQE2hAywYk3nwl3xlPOn76OTr3mWE%2FblX9zCu1%2Fmqo2zKRC1%2Bf7KvpU1kXyQZElDO1r0j%2F02nPxkYK%2BASqiG%2BdNl%2B51eU4TUZv2Afc9O%2FtpaW5P8yCCz0bavqlw31LcRXh3HopZzjM02l4mQC%2FYA5g37HLb2pI2e%2FpKnrmkhZ32A&X-Amz-Signature=827f11b6c4efa7670730e71a1b8ae7787b725fc2725d83ab9850729c46811da9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GJOX7NI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEUTCRjsO%2Fdo2tikBIbhr%2Fr%2FxUDvzSHJfJUPHm6bGjUdAiAaGCYfDKjLk%2FPFUu7B2Wu%2BxBMyWwWazEvBalMTe%2FgdOCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMurq9HGfZH3l6XWCiKtwDzjjwUpj5oBqo6%2FH5djgSO%2FUhiLDD9HsaF5G3ok%2BnGdnnO7LnXZqA8csPvvLOUvNLsXuX5%2BXHsh7xkDojD5NtDwMD9GcSH78RaX7mgzcU%2F7G%2FUHSlnOiVISjqw54qWoCoTQnUYKwPiWvDurDZps2dSLojSxGPWiL%2F65uu%2FWYkzKpjakf%2FDDzoA9yl9BMHx7O9GTQJE%2BMNnbta0MkhT57khsghdYvcKETaMmgxLwzDqvFdKHJPMzywOmxklZm%2BhukOfR8EQjU7lu%2F4u7kqNSljkr6NsDMgxk5Gm7jhi9JCZ5aRZQOu2VLQu2uZh1WMHISCRlizPfkvwqxC789VwH8xzDg21C4qjl0n75Y2eunyrt5WWKL8r1Bc14jCY6c0KfCPzffLUhfS5DFPnKv%2FZt0HcIkMBi7LFegeExsCGcG7amZf8%2BNICsSA1Tm1oLNImX5qJBzVp11G3u%2BChjGjZEWFVNmC0dQdksF%2BVTCvYkXUMGUzqZ8q4Z3Tnq%2BYCObmZEANHa0SDiRZIfL%2Bk7rPq%2BCALwkkxF7YZzFwej4XIf%2FkgvOT1vtTAJ9y9mDJCt5zdZoiz4fMcRIs%2F1D9yyzAhrgcrEdptu5t%2BcuMZmZzZ2oCMyqJASh0NHxChS4vr6Mw4ryEvQY6pgHX2luYEp6yYa5g6QAn57R7x%2FlZ2hPYd%2Frlb5IERFe30Tiab81AsoJPTG28H3QvFaCgyATF6rhTpQav2O5tEMuu3kPiJ0sa2ipIVQjRh4mHRhIotm7b%2B4tk5VQZjBX5eMWDsT4Yy08%2F3%2BjEcPgCsijtK4d1g%2BWcD%2BMaZvvt3GhpYmDuqQxNkZMJEwnuS9qFjVkq2%2BYa%2FoSgoBk5ycPNn03h0D%2FF0XVe&X-Amz-Signature=131bd8db38021a693d1f5f852777ee6a28a0ffeb433f550b054ecc6ed41c7066&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GJOX7NI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIEUTCRjsO%2Fdo2tikBIbhr%2Fr%2FxUDvzSHJfJUPHm6bGjUdAiAaGCYfDKjLk%2FPFUu7B2Wu%2BxBMyWwWazEvBalMTe%2FgdOCr%2FAwgdEAAaDDYzNzQyMzE4MzgwNSIMurq9HGfZH3l6XWCiKtwDzjjwUpj5oBqo6%2FH5djgSO%2FUhiLDD9HsaF5G3ok%2BnGdnnO7LnXZqA8csPvvLOUvNLsXuX5%2BXHsh7xkDojD5NtDwMD9GcSH78RaX7mgzcU%2F7G%2FUHSlnOiVISjqw54qWoCoTQnUYKwPiWvDurDZps2dSLojSxGPWiL%2F65uu%2FWYkzKpjakf%2FDDzoA9yl9BMHx7O9GTQJE%2BMNnbta0MkhT57khsghdYvcKETaMmgxLwzDqvFdKHJPMzywOmxklZm%2BhukOfR8EQjU7lu%2F4u7kqNSljkr6NsDMgxk5Gm7jhi9JCZ5aRZQOu2VLQu2uZh1WMHISCRlizPfkvwqxC789VwH8xzDg21C4qjl0n75Y2eunyrt5WWKL8r1Bc14jCY6c0KfCPzffLUhfS5DFPnKv%2FZt0HcIkMBi7LFegeExsCGcG7amZf8%2BNICsSA1Tm1oLNImX5qJBzVp11G3u%2BChjGjZEWFVNmC0dQdksF%2BVTCvYkXUMGUzqZ8q4Z3Tnq%2BYCObmZEANHa0SDiRZIfL%2Bk7rPq%2BCALwkkxF7YZzFwej4XIf%2FkgvOT1vtTAJ9y9mDJCt5zdZoiz4fMcRIs%2F1D9yyzAhrgcrEdptu5t%2BcuMZmZzZ2oCMyqJASh0NHxChS4vr6Mw4ryEvQY6pgHX2luYEp6yYa5g6QAn57R7x%2FlZ2hPYd%2Frlb5IERFe30Tiab81AsoJPTG28H3QvFaCgyATF6rhTpQav2O5tEMuu3kPiJ0sa2ipIVQjRh4mHRhIotm7b%2B4tk5VQZjBX5eMWDsT4Yy08%2F3%2BjEcPgCsijtK4d1g%2BWcD%2BMaZvvt3GhpYmDuqQxNkZMJEwnuS9qFjVkq2%2BYa%2FoSgoBk5ycPNn03h0D%2FF0XVe&X-Amz-Signature=8c81d4085a8a03e5ff2efa3671463e3388883abfa0e6c137dd1cf78b64b187af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
